# Fortress upgrade source map — RotWK 2.02 audit

This file is an audit manifest for rebuilding the wiki fortress-upgrade section from engine/source truth. It intentionally separates **purchased upgrade**, **internal trigger upgrade**, **prerequisites**, and the **actual CommandButton image key**.

Source basis: RotWK `commandset.ini`, `commandbutton.ini`, project `upgrade.ini`, `gamedata.ini`, fortress object INIs and `attributemodifier.ini`. Do not replace this table with guessed tooltip text or generic icons.

## Men of the West

| Order | Upgrade | Purchased/internal upgrade | ButtonImage | Prerequisite |
|---|---|---|---|---|
| 8 | Fortress Banners | `Upgrade_MenFortressBanners` | `BGFortress_Banner` | — |
| 9 | House of Healing | `Upgrade_MenFortressHouseOfHealing` | `BGFortress_HouseofHealing` | — |
| 10 | Flaming Munitions | `Upgrade_GoodFortressFlamingMunitionsTrigger` | `BGArcheryRange_FireArrows` | — |
| 11 | Boiling Oil | `Upgrade_MenFortressBoilingOil` | `BGFortress_BoilingOil` | — |
| 12 | Numenor Stonework | `Upgrade_MenFortressNumenorStoneworkTrigger` | `BGFortress_NumenorStonework` | — |
| 13 | Ivory Tower | `Upgrade_MenFortressIvoryTower` | `BGFortress_IvoryTower` | `Upgrade_MenFortressNumenorStonework` |

Notes: House of Healing is a `CASTLE_UPGRADE`. Current 2.02 patch notes state its healing radius is 300. Ivory Tower is gated behind Numenor Stonework.

## Elves

| Order | Upgrade | Purchased/internal upgrade | ButtonImage | Prerequisite |
|---|---|---|---|---|
| 7 | Enchanted Anvil | `Upgrade_ElvenFortressEnchantedAnvil` | `BEFortress_EnchantedAnvil` | — |
| 8 | Blessed Mist | `Upgrade_ElvenFortressBlessedMist` | `SBGood_EnshroudingMist` | — |
| 9 | Crystal Moat | `Upgrade_ElvenFortressCrystalMoat` | `BEFortress_CrystalMoat` | — |
| 10 | Mystic Fountains | `Upgrade_ElvenFortressMysticFountains` | `BEFortress_MysticFountains` | — |
| 11 | Encasing Vines | purchase command uses `Upgrade_ElvenFortressEncasingVinesTrigger` | `BEFortress_EncasingVines` | — |
| 12 | Eagle's Nest | `Upgrade_ElvenFortressEaglesNest` | `BEFortress_EagleNest` | `Upgrade_ElvenFortressEncasingVines` |

Current project gamedata values already verified: Enchanted Anvil 500/15s; Blessed Mist 800/15s; Crystal Moat 800/15s; Mystic Fountains 800/30s; Encasing Vines 1500/30s; Eagle's Nest 500/20s. Encasing Vines' current expansion armor macro is 40% and its old health bonus is disabled (0). Eagle recruitment is separate from the fortress improvement (1500/60s in current project gamedata).

## Dwarves

| Order | Upgrade | Purchased/internal upgrade | ButtonImage | Prerequisite |
|---|---|---|---|---|
| 8 | Fortress Banners | `Upgrade_DwarvenFortressBanners` | `BDFortress_Banners` | — |
| 9 | Siege Kegs | `Upgrade_DwarvenFortressSiegeKegs` | `BDFortress_SiegeKegs` | — |
| 10 | Flaming Munitions | `Upgrade_GoodFortressFlamingMunitionsTrigger` | `BDFortress_FlamingMunitions` | — |
| 11 | Oil Casks | `Upgrade_DwarvenFortressOilCasks` | `BDFortress_OilCasks` | — |
| 12 | Dwarven Stonework | `Upgrade_DwarvenFortressDwarvenStoneworkTrigger` | `BDFortress_DwarvenStonework` | — |
| 13 | Mighty Catapult | `Upgrade_DwarvenFortressMightyCatapult` | `BDFortress_MightyCatapult` | `Upgrade_DwarvenFortressDwarvenStonework` |

Mighty Catapult is explicitly gated behind Dwarven Stonework.

## Isengard

| Order | Upgrade | Purchased/internal upgrade | ButtonImage | Prerequisite |
|---|---|---|---|---|
| 7 | Murder of Crows | `Upgrade_IsengardFortressMurderOfCrows` | `SBEvil_Crebain` | — |
| 8 | Burning Forges | `Upgrade_IsengardFortressBurningForges` | `BIFortress_BurningForges` | — |
| 9 | Excavations | `Upgrade_IsengardFortressExcavations` | `BIFortress_Excavations` | — |
| 10 | Orcfire Munitions | `Upgrade_IsengardFortressOrcfireMunitionsTrigger` | `BMOrcPit_FlamingArrows` | — |
| 11 | Iron Plating | `Upgrade_IsengardFortressIronPlatingTrigger` | `BIFortress_IronPlating` | — |
| 12 | Wizard's Tower | `Upgrade_IsengardFortressWizardsTower` | `BIFortress_WizardTower` | `Upgrade_IsengardFortressIronPlating` |

Current project gamedata values already verified: Murder of Crows 500/15s; Burning Forges 1000/30s; Excavations 600/15s; Orcfire Munitions 1500/30s; Iron Plating 1500/30s; Wizard's Tower 1500/45s. Iron Plating current keep/expansion armor macros are 40%; old health bonuses are disabled (0). Wizard Tower lightning data includes 300 main + 100 FLAME and range 1500; presentation still needs the exact weapon/ability resolution rather than simply adding these numbers blindly.

## Mordor

| Order | Upgrade | Purchased/internal upgrade | ButtonImage | Prerequisite |
|---|---|---|---|---|
| 8 | Doom Pyres | `Upgrade_MordorFortressDoomPyres` | `BMFortress_DoomPyres` | — |
| 9 | Lava Moat | `Upgrade_MordorFortressLavaMoat` | `BMFortress_LavaMoat` | — |
| 10 | Fire Arrows | `Upgrade_MordorFortressFireArrowsTrigger` | `BMOrcPit_FlamingArrows` | — |
| 11 | Magma Cauldrons | `Upgrade_MordorFortressMagmaCauldrons` | `BMFortress_MagmaCauldrons` | — |
| 12 | Morgul Sorcery | `Upgrade_MordorFortressMorgulSorceryTrigger` | `BMFortress_MorgulSorcery` | — |
| 13 | Gorgoroth Spire | `Upgrade_MordorFortressGorgorothSpire` | `BMFortress_GorgonothSpire` | `Upgrade_MordorFortressMorgulSorcery` |

Note the engine asset key is actually spelled `Gorgonoth` in `ButtonImage`; preserve/match the real asset key. Current project gamedata values already verified: Doom Pyres 500/15s; Lava Moat 800/15s; Fire Arrows 1200/30s; Magma Cauldrons 1000/30s; Morgul Sorcery 1500/30s; Gorgoroth Spire 2000/45s. Morgul Sorcery current keep/expansion armor macro is 40% and health bonus is disabled (0). Spire weapon macros expose range 1500 and separate 333 rock + 333 flame components; exact ability resolution must be rendered as components, not a made-up single number.

## Goblins / Wild

| Order | Upgrade | Purchased/internal upgrade | ButtonImage | Prerequisite |
|---|---|---|---|---|
| 7 | Bat Cloud | `Upgrade_WildFortressBatCloud` | `SBEvil_CaveBats` | — |
| 8 | Razor Spines | `Upgrade_WildFortressRazorSpines` | `BWFortress_RazorSpines` | — |
| 9 | Fire Arrows | `Upgrade_WildFortressFireArrowsTrigger` | `BMOrcPit_FlamingArrows` | — |
| 10 | Web Cocoon | purchase command uses `Upgrade_WildFortressWebCocoonTrigger` | `BWFortress_WebCocoon` | — |
| 11 | Dragon Nest | `Upgrade_WildFortressDragonNest` + `Upgrade_DragonNestFireDrakeButtonEnable` | `BWFortress_DragonNest` | `Upgrade_WildFortressWebCocoon` |

Verified object wiring: Razor Spines uses a `DamageFieldUpdate`, radius 100, enemy filter, and fires `RazorSpinesBasicWeapon`; this should be described as an actual proximity damage field, with damage taken from the weapon definition. Web Cocoon's trigger passes the real `Upgrade_WildFortressWebCocoon`, and the fortress then applies `WebCocoonKeep_Bonus`; use the modifier/gamedata macro for armor rather than an editorial HP claim. Dragon Nest is gated behind Web Cocoon and separately enables Fire Drake purchase.

## Angmar

| Order | Upgrade | Purchased/internal upgrade | ButtonImage | Prerequisite |
|---|---|---|---|---|
| 8 | Fortress Banners | `Upgrade_AngmarFortressBanners` | `KUTorchesIcon` | — |
| 9 | Spikes | `Upgrade_AngmarFortressSpikes` | `KUSpikeMoatIcon` | — |
| 10 | Ice Munitions | `Upgrade_AngmarFortressIceMunitionsTrigger` | `KUIceShotIcon` | — |
| 11 | House of Lamentation | `Upgrade_AngmarFortressHouseOfLamentation` | `KUHouseOfLamIcon` | — |
| 12 | Ice Walls | `Upgrade_AngmarFortressIceWallsTrigger` | `KUIceWallsIcon` | — |
| 13 | Sanctum | `Upgrade_AngmarFortressSanctum` | `KUSanctumIcon` | `Upgrade_AngmarFortressIceWalls` |

House of Lamentation is a `CASTLE_UPGRADE`. Ice Walls eventually drives `AngmarStoneworkKeep_Bonus` / `AngmarStoneworkExpansion_Bonus`; use the current gamedata macro values when rendering the player-facing effect. Sanctum is gated behind Ice Walls.

## Rendering rules for the wiki rebuild

1. Show the **real CommandButton image**, never a generic `⬆️` placeholder when a verified asset is mapped.
2. Store both purchase-trigger and applied/internal upgrades when they differ.
3. Resolve costs and build times from current project `gamedata.ini`, not old vanilla comments in the INIs.
4. Describe effects from fortress object behaviors + `attributemodifier.ini` + weapon/special-power definitions. Tooltips are useful localization, but are not the gameplay source of truth.
5. Show prerequisite chains visibly: Numenor Stonework → Ivory Tower; Encasing Vines → Eagle's Nest; Dwarven Stonework → Mighty Catapult; Iron Plating → Wizard's Tower; Morgul Sorcery → Gorgoroth Spire; Web Cocoon → Dragon Nest; Ice Walls → Sanctum.
6. When an armor modifier is stored as engine `ARMOR 40%`, do not silently relabel it as “+40% armor” without applying the wiki's established engine-vs-effective-durability semantics.
7. Active fortress abilities unlocked by an upgrade (Ivory Tower vision, Bat Cloud ability, Wizard Tower strike, Gorgoroth Spire, Sanctum, etc.) should be displayed separately from the passive purchase effect.
