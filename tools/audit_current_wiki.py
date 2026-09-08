#!/usr/bin/env python3
import json, re
from pathlib import Path

HTML = Path('index.html')
OUT = Path('fortress_audit.json')
text = HTML.read_text(encoding='utf-8')

m = re.search(r'<script\s+id=["\']db["\'][^>]*>(.*?)</script>', text, re.S | re.I)
if not m:
    raise SystemExit('Could not find <script id="db"> JSON payload')
db = json.loads(m.group(1))

report = {
    'top_level_keys': list(db.keys()),
    'meta': db.get('meta'),
    'fortress_entities': [],
    'fortress_related_top_level': {},
    'string_hits': []
}

# Surface top-level containers whose names are likely relevant.
for k, v in db.items():
    lk = k.lower()
    if any(t in lk for t in ('fortress', 'building', 'structure', 'upgrade')):
        if isinstance(v, (list, dict)):
            report['fortress_related_top_level'][k] = {
                'type': type(v).__name__,
                'count': len(v),
                'sample_keys': list(v.keys())[:30] if isinstance(v, dict) else None,
            }

# Find dict records that look like fortress entities/records.
def walk(obj, path='db'):
    if isinstance(obj, dict):
        # Record-level fortress detection using common identity/name fields.
        identity_parts = []
        for key in ('entity_id','object_id','id','name_en','name_fr','display_name','name','building_id'):
            val = obj.get(key)
            if isinstance(val, str):
                identity_parts.append(val)
        identity = ' | '.join(identity_parts)
        if 'fortress' in identity.lower() or 'forteresse' in identity.lower():
            compact = {}
            for key, val in obj.items():
                if key in ('image_data','data_uri','raw_html'):
                    continue
                if isinstance(val, (str,int,float,bool)) or val is None:
                    compact[key] = val
                elif isinstance(val, list) and len(val) <= 30:
                    compact[key] = val
                elif isinstance(val, dict) and len(val) <= 30:
                    compact[key] = val
            report['fortress_entities'].append({'path': path, 'record': compact})

        for k, v in obj.items():
            walk(v, f'{path}.{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            walk(v, f'{path}[{i}]')
    elif isinstance(obj, str):
        s = obj.lower()
        if ('fortress' in s or 'forteresse' in s) and len(report['string_hits']) < 300:
            report['string_hits'].append({'path': path, 'value': obj[:1000]})

walk(db)

# De-duplicate fortress records by path while preserving order.
seen = set(); dedup = []
for row in report['fortress_entities']:
    if row['path'] not in seen:
        seen.add(row['path']); dedup.append(row)
report['fortress_entities'] = dedup

OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Wrote {OUT}: {len(report["fortress_entities"])} fortress-like records')
print('Top-level keys:', ', '.join(report['top_level_keys']))
