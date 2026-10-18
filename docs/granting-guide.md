# Granting guide (for approvers)

How to record a tibtre update, start to finish.

## 1. Value the work

1. List what was accepted since the last update: merged PRs from everyone,
   maintainers included, and any non-PR work (art, maps, playtests, community).
2. Have the AI reviewer value each contribution with
   [ai-evaluation-prompt.md](ai-evaluation-prompt.md) and the
   [grading rubric](grading-rubric.md).
3. Check the factors. Correct a factor only when it is factually wrong, and record
   why. When the AI is torn between two size classes, pick the one whose definition
   fits better and say so.
4. Save the values as `valuations/YYYY-MM-DD.csv`, one line per contribution:
   `item,id,category,class,base,difficulty,quality,value,note`, where `item` is a PR
   number like `#1234` (`#1234+#1240` when several PRs are one piece of work) or an
   `assets/` path.

## 2. First-time contributor? Assign an ID

1. Generate a random ID: `python -c "import secrets; print('T-'+secrets.token_hex(2).upper())"`
   — re-roll if it already exists in `CONTRIBUTORS.csv` (format `T-XXXX`).
2. Generate their identity commitment: `python identity.py new discord:<numeric id>`
   (or `github:<numeric id>` for GitHub-based contributors) — commitment goes in
   `CONTRIBUTORS.csv` (space-separated if they already hold one), salt goes in the
   registry AND the DM. If the contributor prefers to hold the only copy of their
   salt, they may run `identity.py new` themselves and send just the commitment —
   record it verbatim and leave the registry's salt field empty.
3. Add their row to the **private registry** (see `../vera20k-tibtre-private/`):
   ID, Discord **numeric user ID** (Developer Mode → right-click user → Copy User ID —
   handles change, the number never does), current handle, salt, date.
4. **DM them their ID and their salt** and tell them to keep the message — it's
   their receipt, and the salt makes their identity claim publicly provable via
   `identity.py` without trusting anyone.
5. Ask how they want to appear publicly: their handle, a pseudonym, or nothing
   (ID only) — and whether they want a public contact shown (portfolio/site link
   preferred over raw email; warn that committed values persist in history). Add
   `id,display_name,contact,commitment` to `CONTRIBUTORS.csv` — leave fields
   empty as chosen.
6. Ask **who, if anyone, brought them to the project**. Record the recruiter in the
   private registry notes — and when this newcomer's first grant is recorded, grant
   the recruiter 2 tibtre (`recruit`) in the same batch.

Display-name changes later are just an edit to `CONTRIBUTORS.csv` — never touch the
ledger for a naming matter.

## 3. Secure the artifact

The ledger row must link to something durable:

- **Code / research / docs** — link the merged PR or commit.
- **Artwork / maps / media** — save the file into `assets/` as
  `YYYY-MM-DD_T-XXXX_short-title.ext` (always the ID, never the name — filenames are
  public and forever), then reference that path. Discord message links die
  (deletable, members-only) — don't use them as the only reference.
- **Playtest reports** — paste the report into a file under `assets/` too if it only
  exists as a Discord message.

Check the licensing line applies (it's in RULES.md — submitting = licensing the
project to use the work). If the contributor hasn't seen it, point them to it.

**Privacy scrub before committing — history is forever:** check every file for
personal information before it enters git. Usernames or real names visible in
screenshots, embedded image metadata (EXIF), real names in report text, identifying
paths in logs. Redact first, commit second — an erasure request later is a
history-rewrite; a scrub now is ten seconds.

## 4. Append the ledger rows

One row per person and category, at the END of `LEDGER.csv` — never edit existing rows:

```csv
date,id,tibtre,category,notes
2026-10-25,T-9C41,12.5,code,7 PRs (#1990 #1994 #1998 #2003 #2007 #2011 #2015); value 12.25 (valuations/2026-10-25.csv; rubric v1.5)
```

- `date` — ISO `YYYY-MM-DD`
- `id` — contributor ID from `CONTRIBUTORS.csv`
- `tibtre` — the person's total for that category, rounded to the nearest 0.5
  (ties round up; minimum 0.5); negative only for corrections, with an explanatory note
- `category` — `code` / `research` / `art` / `maps` / `playtesting` / `docs` / `community` / `recruit` (paid on the recruit's first grant) / `impact` (retrospective value bonus — evidence required in notes) / `other`
- `notes` — what the work was (PR numbers or assets filenames), the value, the
  valuations file and the rubric version. Required for corrections. Keep names out
  of notes for pseudonymous contributors.

## 5. Regenerate balances and commit

```
python tally.py
git add -A
git commit -m "grant: update 2026-10-25"
git push
```

Commit straight to `master` (see [AGENTS.md](../AGENTS.md)).

## 6. Announce

Post the update in the Discord: IDs, amounts, and a link to the valuations file. Name
a contributor only if they have a public display name; pseudonymous contributors are
congratulated by DM, and the announcement carries the ID only.

## Corrections

Wrong amount or wrong ID? Append a compensating row (negative amount or a new grant)
with a note pointing at the mistaken row's date+ID. The old row stays.
