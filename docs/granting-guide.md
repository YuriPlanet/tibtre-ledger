# Granting guide (for maintainers)

How to record a tibtre update, step by step.

## 1. Value the work

1. List everything accepted since the last update: merged PRs from everyone,
   maintainers included, and other work (art, maps, playtests, community).
2. Have the AI value each piece of work with its
   [instructions](ai-evaluation-prompt.md) and the [grading rules](grading-rubric.md).
   Several PRs that make one piece of work are valued together.
3. Check every factor. Keep it, or change it and write down why.
4. Save the values as `valuations/YYYY-MM-DD.csv`, one line per piece of work:

   ```csv
   item,id,category,size,base,difficulty,quality,value,note
   #1990+#1994,T-9C41,code,M,4,1.5,1.0,6,pathfinding fix and its follow-up
   ```

   `item` is a PR number (several joined with `+`) or an `assets/` path. `size` is XS
   to XL for code, or the matching table row for other work. When a maintainer
   changed a factor, `note` says why.

## 2. New contributor? Give them an ID

1. Make a random ID, and make a new one if `CONTRIBUTORS.csv` already has it:
   `python -c "import secrets; print('T-'+secrets.token_hex(2).upper())"`
2. Make their identity commitment: `python identity.py new discord:<numeric id>`
   (or `github:<numeric id>`). The commitment goes in `CONTRIBUTORS.csv`. The salt
   goes in the private registry and in your DM to them. If they'd rather keep the only
   copy of the salt, they can run `identity.py new` themselves and send you just the
   commitment; then leave the registry's salt empty.
3. Add a row to the private registry (`../vera20k-tibtre-private/`): ID, Discord
   numeric user ID (Developer Mode → right-click the user → Copy User ID; handles
   change, the number doesn't), current handle, salt and date.
4. DM them their ID and salt, and tell them to keep the message.
5. Ask how they want to appear: their handle, another name or only the ID, and
   whether to show a public link. Add their row to `CONTRIBUTORS.csv`
   (`id,display_name,contact,commitment`).
6. Ask who brought them to the project. Note the recruiter in the registry, and grant
   the recruiter 2 tibtre (`recruit`) in the update with the newcomer's first grant.

A later name change is an edit to `CONTRIBUTORS.csv`. Never touch the ledger for it.

## 3. Keep a lasting link to the work

- **Code, research, docs:** the merged PR or commit.
- **Art, maps, media, playtest reports:** save the file in `assets/` as
  `YYYY-MM-DD_T-XXXX_short-title.ext` (always the ID, never a name) and point to that
  path. Discord messages can be deleted, so never use one as the only link.

Before committing a file, remove personal information: names or usernames in
screenshots, image metadata (EXIF), real names in reports and identifying paths in
logs. Git history is permanent.

If the contributor hasn't seen the licensing rule in `RULES.md`, point them to it.

## 4. Add the ledger rows

Add one row per person and category at the end of `LEDGER.csv`. Never edit old rows.

```csv
date,id,tibtre,category,notes
2026-10-25,T-9C41,12.5,code,7 PRs (#1990 #1994 #1998 #2003 #2007 #2011 #2015); value 12.25 (valuations/2026-10-25.csv; rubric v1.5)
```

- `tibtre`: the person's total for that category, rounded to the nearest 0.5 (halves
  round up; at least 0.5). Negative only for corrections.
- `category`: `code`, `research`, `art`, `maps`, `playtesting`, `docs`, `community`,
  `recruit`, `impact` (its note names the public evidence) or `other`.
- `notes`: what the work was, the unrounded value, the valuations file and the rubric
  version. No commas, and no names for contributors who show only their ID.

## 5. Update the balances and commit

```
python tally.py
git add -A
git commit -m "grant: update 2026-10-25"
git push
```

Commit straight to `master` (see [AGENTS.md](../AGENTS.md)).

## 6. Announce

Post the update in the Discord: IDs, amounts and a link to the valuations file. Use a
name only for contributors who show one publicly, and congratulate the others by DM.

## Corrections

Wrong amount or wrong ID? Add a new row that fixes it (a negative amount or a new
grant), with a note naming the date and ID of the wrong row. The old row stays.
