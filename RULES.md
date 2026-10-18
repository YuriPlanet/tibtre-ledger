# Tibtre — the VERA20k contribution currency

VERA20k is built by its contributors, and tibtre is how the project remembers who built it.

## What is one tibtre?

**1 tibtre ≈ the value of one focused hour of high-quality work on something the project genuinely needs.**

Tibtre is granted for *accepted results*, not for time spent. The project's AI reviewer values each accepted contribution with the public [grading rubric](docs/grading-rubric.md), the same way for everyone, by what it does for the project. You never report your own hours.

## What is tibtre worth?

Today, two things:

1. **Recognition.** Your balance is public in [`BALANCES.md`](BALANCES.md).
2. **Governance.** Roadmap polls and feature votes in the Discord are weighted by tibtre. Contributors steer the project — with one fairness cap: no single person's weight ever counts for more than 25% of a vote, so early large holders guide but never rule. (Exact mechanics are executable — [`voteweight.py`](voteweight.py); with 4 or fewer voters the cap makes a poll one-person-one-vote.)

**Tibtre has no monetary value and no promise of future monetary value.** It is the founders' good-faith intention that **if this project ever forms a legal entity or shares out money, such as donations, this ledger guides the allocation.**

## How do you earn it?

**There is nothing to apply for and nothing to claim.** Do work you believe helps, submit it, get valued — that's the whole process. And tibtre itself is **opt-out**: if you'd rather contribute without being scored at all, say so — your work is just as welcome, and nothing about it gets a number. Contribute anything the project needs, through whichever channel suits you:

| Category | Examples | Where to submit |
|---|---|---|
| `code` | Engine features, bug fixes, tooling | GitHub pull request |
| `research` | Verified gamemd.exe research, parity findings | GitHub pull request or Discord |
| `art` | Sprites, UI art, loading screens, logos, videos | Discord `#submissions` |
| `maps` | Maps and scenarios | Discord `#submissions` |
| `playtesting` | Structured playtest reports, reproducible bug reports | Discord `#submissions` |
| `docs` | Guides, wiki pages, translations | GitHub pull request or Discord |
| `community` | Sustained moderation, onboarding, events | Granted by maintainers |
| `recruit` | Bringing in a contributor who ships | Automatic when their first grant lands — they name you when joining |

You do **not** need a GitHub account. Post your work in the Discord and a maintainer records the grant for you.

## How grants happen

1. You submit work (PR, Discord post, however fits).
2. The project's AI reviewer values the accepted work from the public [grading rubric](docs/grading-rubric.md) by what it does for the project, not by line count, PR count or who made it. A maintainer checks the AI's factors and corrects one only openly, with the reason recorded. Each update's values are published in `valuations/`, so you always see how yours was reached.
3. On your first grant you're assigned a **contributor ID** (random, like `T-9C41`). Each update gives you one row per category in [`LEDGER.csv`](LEDGER.csv): date, ID, amount, category, and a note saying what the work was and where its values are.
4. Every grant is public. The ledger is append-only and its full history is auditable.

**The same rules bind everyone — maintainers and founders included.** Their contributions are graded by the same rubric, recorded in the same public ledger, and open to the same disputes as anyone else's.

## Your name is yours to control

The public ledger only ever contains your contributor ID. How you *appear* — in the balances and in credits — is up to you, via [`CONTRIBUTORS.csv`](CONTRIBUTORS.csv):

- Use your Discord handle, a pseudonym, or any name you like.
- Set no display name at all and appear only as your ID.
- Optionally list a public **contact** (portfolio, website, profile link — shown beside your balance). A link is strongly preferred over a raw email: public repos get scraped by spammers, and like everything committed, old values persist in history.
- Change or remove your display name or contact at any time by asking a maintainer — this never touches ledger history, so your balance and grants are unaffected. (GitHub users can also open a PR editing their own row. The ledger itself is never edited via PR.)

Who is behind each ID is known only to the maintainers, recorded privately.

### If you want to disappear later

- **Instantly:** ask a maintainer to blank your display name — every current page then shows only your ID. Your balance and grants are untouched, because the ledger never contained your name.
- **From history too:** old versions of the contributors file live in this repository's public history. On request we will rewrite that history to purge your name and ask GitHub to clear its caches. Honest caveat: public repositories can be copied by anyone at any time — we can purge every copy *we* control, but not copies strangers may have made before your request.
- **Your submitted work:** we remove attribution on request, always. Work that has already shipped in the game or been merged stays licensed and shipped — that can't be undone — but we'll stop showcasing it where practical.

## Licensing of submissions

By submitting work to VERA20k you license the project to use, modify, and distribute it under the project's license (or CC-BY 4.0 with attribution for standalone art). You keep ownership of your work; the project keeps the right to ship it.

## Disputes and corrections

If you think a grant is wrong (yours or anyone's), raise it with a maintainer. The valuation is redone openly, and corrections are appended to the ledger as new rows — history is never rewritten.

## Changes to this policy

Policy changes are announced in the Discord, and every rubric version is listed at the top of the [rubric](docs/grading-rubric.md). The ledger and its rules exist to be boring, predictable, and fair.
