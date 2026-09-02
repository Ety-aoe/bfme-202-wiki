# Deployment / update workflow

## Public release

GitHub Pages should serve the `main` branch from the repository root.

1. Put the validated standalone wiki build at `index.html` in the repository root.
2. In **Settings → Pages**, choose **Deploy from a branch**.
3. Select branch **main** and folder **/(root)**, then save.
4. Future validated updates only require replacing `index.html` on `main`.

## Safe updates

For larger changes, work on a separate branch (for example `dev`), test the standalone HTML locally, and merge it into `main` only after validation. The current public build remains available while work is happening on the other branch.

If a regression reaches production, use Git history to restore the previous `index.html` commit.

## Target

BFME II: The Rise of the Witch-king — Patch 2.02 v9.7.7.
