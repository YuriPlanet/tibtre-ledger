# Tibtre rules

Tibtre are points that record who helped build VERA20k, and how much.

## Earning tibtre

- **Anyone can earn it.** Code, research, art, maps, playtesting, docs, translations and community work all count. Send code as a GitHub pull request, or post your work on [Discord](https://discord.gg/kmjRUn5m5F) or in the QQ group (1097193563). You don't need a GitHub account.
- **There is nothing to apply for.** A maintainer will most likely pick up your work, and you get tibtre automatically.
- **It is for accepted work, not for time.** One tibtre is about one hour of good work on something the project needs. You never report your hours.
- **An AI and a maintainer value it together**, with the public [grading rules](docs/grading-rubric.md). What counts is what the work does for the project, not who made it, how many lines it has or how many PRs it took.
- **The same rules apply to everyone**, maintainers and founders included.
- **Bringing people in counts.** When someone you brought to the project gets their first grant, you get 2 tibtre. They name you when they join.
- **You can opt out.** If you'd rather not be scored, say so. Your work is just as welcome.

## The ledger

- Each grant is a row in [`LEDGER.csv`](LEDGER.csv): the date, your contributor ID, the amount, the kind of work and a note on what it was.
- Rows are never changed or deleted. A mistake is fixed with a new row.
- Everyone's total is in [`BALANCES.md`](BALANCES.md).
- How each update was valued, piece by piece, is published in `valuations/`.

## What tibtre is worth

1. **Recognition.** Your balance is public.
2. **A say in the project.** Roadmap polls and feature votes are weighted by tibtre. No one person counts for more than 25% of a vote ([`voteweight.py`](voteweight.py) does the math).

**Tibtre has no monetary value and no promise of future monetary value.** It is the founders' good-faith intention that **if this project ever forms a legal entity or shares out money, such as donations, this ledger guides the allocation.**

## Your name

- Your first grant gives you a random contributor ID, like `T-9C41`. The ledger only ever shows IDs.
- You choose how you appear in [`CONTRIBUTORS.csv`](CONTRIBUTORS.csv): your username, another name, or only your ID. You can also show a public link, like a website. A link is safer than an email address, because everything here is public and stays in the history.
- Ask a maintainer to change or remove your name or link at any time. Your balance doesn't change.
- Only the maintainers know who is behind each ID.

**If you want to disappear later:**

- **Right away:** ask a maintainer to blank your name. Every page then shows only your ID.
- **From the history too:** old versions of the contributors file stay in this repository's history. On request we rewrite that history to remove your name, and ask GitHub to clear its caches. We can't remove copies other people made before your request.
- **Your work:** we remove your name from it on request. Work already in the game or merged stays there, but we stop showcasing it where we can.

## Licensing

By submitting work to VERA20k you license the project to use, modify, and distribute it under the project's license (or CC-BY 4.0 with attribution for standalone art). You keep ownership of your work; the project keeps the right to ship it.

## Disputes

Think a grant is wrong, yours or anyone's? Tell a maintainer. It is valued again openly, and any fix is added to the ledger as a new row.

## Changes

Rule changes are announced on Discord and in the QQ group.
