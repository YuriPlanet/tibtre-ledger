"""Regenerate BALANCES.md from LEDGER.csv + CONTRIBUTORS.csv + valuations/.

The ledger is keyed by contributor ID (random, like T-83DE). Display names live
in CONTRIBUTORS.csv and are optional - an ID with no display name is shown as
the ID itself (pseudonymous contributor). If a contact URL is set, the display
name renders as a link.

The Work column names the kinds of work each balance was granted for, largest
first: the `type` of each valued item in valuations/*.csv, then the category of
each ledger row whose note cites no valuations file (grants from before itemized
valuations). Correction rows count against their kind, and a kind is shown only
while its total is positive, so a correction can move work to another kind.

Usage: python tally.py
"""

import csv
import re
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
LEDGER = HERE / "LEDGER.csv"
CONTRIBUTORS = HERE / "CONTRIBUTORS.csv"
BALANCES = HERE / "BALANCES.md"
VALUATIONS = HERE / "valuations"

# How BALANCES.md names each valuation `type` and each ledger category.
WORK_NAMES = {
    "gameplay": "gameplay",
    "triggers": "map triggers and AI scripts",
    "graphics": "graphics",
    "interface": "menus and controls",
    "sound": "sound and video",
    "multiplayer": "multiplayer",
    "maps": "maps and terrain",
    "cleanup": "code cleanup and speed",
    "tools": "tests and tools",
    "docs": "docs",
    "research": "research",
    "art": "art",
    "playtesting": "playtesting",
    "community": "community",
    "legal": "legal",
    "recruit": "recruiting",
    "impact": "impact",
    "other": "other",
}
# Ledger categories of grants made before itemized valuations.
EARLIER_NAMES = {"code": "earlier code", "maps": "map making"}


def fmt(amount: float) -> str:
    return f"{amount:g}"


def load_contributors() -> dict[str, dict[str, str]]:
    info: dict[str, dict[str, str]] = {}
    with CONTRIBUTORS.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            cid = row["id"].strip()
            if cid:
                info[cid] = {
                    "name": row["display_name"].strip(),
                    "contact": (row.get("contact") or "").strip(),
                }
    return info


def load_valued_work() -> dict[str, dict[str, float]]:
    """Each contributor's valued items and their corrections, summed by work type."""
    work: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
    for path in sorted(VALUATIONS.glob("*.csv")):
        with path.open(newline="", encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                kind = (row.get("type") or row["category"]).strip()
                work[row["id"].strip()][kind] += float(row["value"])
    return work


def work_cell(valued: dict[str, float], earlier: dict[str, float]) -> str:
    names: list[str] = []
    for kind, total in sorted(valued.items(), key=lambda kv: -kv[1]):
        if total > 0:
            names.append(WORK_NAMES.get(kind, kind))
    for kind, total in sorted(earlier.items(), key=lambda kv: -kv[1]):
        if total > 0:
            names.append(EARLIER_NAMES.get(kind) or WORK_NAMES.get(kind, kind))
    return ", ".join(dict.fromkeys(names))


def main() -> None:
    info = load_contributors()
    valued = load_valued_work()
    earlier: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
    balances: dict[str, float] = {}
    grants = 0
    with LEDGER.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            cid = row["id"].strip()
            if not cid:
                continue
            balances[cid] = balances.get(cid, 0) + float(row["tibtre"])
            grants += 1
            cited = re.search(r"valuations/([\w.-]+\.csv)", row["notes"])
            if not (cited and (VALUATIONS / cited.group(1)).is_file()):
                earlier[cid][row["category"].strip()] += float(row["tibtre"])

    def shown(cid: str) -> str:
        entry = info.get(cid, {})
        name = entry.get("name") or cid
        contact = entry.get("contact", "")
        if contact.startswith("http"):
            return f"[{name}]({contact})"
        if contact:
            return f"{name} ({contact})"
        return name

    ranked = sorted(balances.items(), key=lambda kv: (-kv[1], shown(kv[0]).lower()))

    lines = [
        "# Tibtre balances",
        "",
        f"Generated from [`LEDGER.csv`](LEDGER.csv) - {grants} grant(s), "
        f"{fmt(sum(balances.values()))} tibtre in circulation. "
        "Do not edit by hand; run `python tally.py`.",
        "",
        "| # | Contributor | Tibtre | Work |",
        "|---|---|---|---|",
    ]
    if ranked:
        for i, (cid, balance) in enumerate(ranked, start=1):
            work = work_cell(valued.get(cid, {}), earlier.get(cid, {}))
            lines.append(f"| {i} | {shown(cid)} | {fmt(balance)} | {work} |")
    else:
        lines.append("| - | *no grants yet* | 0 | |")
    lines.append("")

    BALANCES.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Wrote {BALANCES.name}: {len(ranked)} contributor(s), {grants} grant(s).")


if __name__ == "__main__":
    main()
