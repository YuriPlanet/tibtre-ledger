# Agent notes

- Commit straight to `master` and push. This repo uses no branches, pull requests or
  squash merges. Never force-push.
- Record grants with [docs/granting-guide.md](docs/granting-guide.md): append rows to
  the end of `LEDGER.csv`, never edit or delete past rows, then run `python tally.py`.
- Never commit salts or anything else from the private registry.
