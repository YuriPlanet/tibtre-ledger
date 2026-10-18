# Tibtre grading rubric — v1.5

*(v1.5: the AI reviewer's value is the grant, the same way for everyone, at a fixed
scale; no priority board or bounties. v1.4, used once on 2026-10-18: one scale set by
the owner's own value. v1.3: added `recruit`. v1.2: human and AI values averaged.
v1.1: added worth to the project. Forward-only: each ledger note names the version it
used.)*

## How work is valued

The project's AI reviewer values every accepted contribution with this rubric, the
same way for everyone, maintainers included:

```
tibtre = base × difficulty × quality
```

The value is what the work does for the project. It never depends on who made it,
the hours claimed, AI assistance, line count or the number of PRs: splitting work
into more PRs adds nothing. The AI follows the public
[evaluation prompt](ai-evaluation-prompt.md) and shows every factor, so anyone can
recompute it.

A maintainer checks the factors. A factor that is factually wrong, such as a missed
rework or the wrong subsystem, is corrected openly with the reason recorded. Nobody
adds a personal value on top.

Each update publishes the per-contribution values in `valuations/YYYY-MM-DD.csv`.
Each person gets one ledger row per update and category: their total, rounded to the
nearest 0.5 (ties round up; minimum 0.5).

Contributors never apply, claim, or pre-register anything. Do the work, submit it,
get valued.

## Base — by category and size

Size is the work's **worth to the project**: its scope, and how much players or
contributors feel it. A player-visible feature or fix weighs more than an internal
change of similar scope. Never raw line count: padding a diff doesn't move the size
class.

### Code
| Size | Definition | Base |
|---|---|---|
| XS | Typo, one-liner, config tweak | 0.5 |
| S | Contained fix, one file/subsystem | 1.5 |
| M | Feature or fix within one subsystem, incl. tests | 4 |
| L | Multi-subsystem feature or new module | 8 |
| XL | New system end-to-end | 16 |

### Reverse-engineering research
| Work | Base |
|---|---|
| Single verified fact (address/constant/formula, with evidence) | 1 |
| Focused note — one mechanic, verified claims, implementation handoff | 3 |
| Full system doc — verified, with implementation handoff | 8 |

### Art (RA2 assets are countable — frames, facings, damage states)
| Work | Base |
|---|---|
| Cameo/icon | 1 |
| UI element, loading screen, promo art | 3 |
| Building SHP (frames + damage states) | 5 |
| Voxel unit (+turret) | 6 |
| Full unit SHP set (8 facings × walk/attack/die) | 10 |

### Maps
| Work | Base |
|---|---|
| Small skirmish map, playtested | 3 |
| Large or multiplayer-balanced map, playtested | 6 |

### Playtesting
| Work | Base |
|---|---|
| Reproducible bug report (steps + expected vs actual) | 1 |
| Structured session report (following the template) | 2 |

### Docs, translations, community
| Work | Base |
|---|---|
| Guide/wiki page | 2 |
| Translation, per 1000 words | 1.5 |
| Community event organized | 3 |
| Sustained moderation, per month | 2 |
| Recruited a contributor who ships | 2 |

**Recruit rule:** paid only when the recruited person's *first grant is recorded* —
never on the invite itself (invite spam mints nothing). The newcomer names their
recruiter during ID assignment; one recruit grant per new contributor; no
multipliers. If the recruit becomes a major contributor, the recruiter's upside is
handled by the normal impact-bonus machinery.

## Difficulty multiplier — take the single highest that applies

| × | Applies to |
|---|---|
| 1.0 | Routine work |
| 1.5 | Hard domains: deterministic sim internals, renderer/GPU, netcode, RE of unlabeled binary code |

## Quality multiplier

| × | Applies to |
|---|---|
| 0.75 | Accepted, but needed significant rework by others |
| 1.0 | Solid — accepted as-is |
| 1.25 | Exceptional — beyond-scope tests/docs/polish |

## Impact bonuses

At milestones (a release, a player or contributor influx, a donation spike),
maintainers may grant bonus tibtre for what demonstrably drove it, as category
`impact`, each citing its observable evidence (e.g., *"replay system — named in the
posts that brought 200 new members"*). No bonus without named, public evidence.

## Consistency mechanics

- **Show your work.** A grant without its computation is invalid.
- **Comparables.** Each valuation cites the most similar past values; deviating more
  than ~30% needs an explanation.
- **Versioned, forward-only.** Rubric changes get a new version number and apply only
  to future grants — the ledger is never repriced retroactively.
- **Disputes.** Raise them with a maintainer. The valuation is redone openly, and any
  correction is appended as a new ledger row.

## Worked examples

1. Contained pathfinding bug fix, in the hard sim domain, accepted as-is:
   `1.5 (S code) × 1.5 (hard domain) × 1.0 = 2.25`
2. Loading screen, routine, exceptional polish:
   `3 (art) × 1.0 × 1.25 = 3.75`

## What the rubric promises

Identical work earns identical tibtre, whoever made it, and you can price your
contribution before you start. The constants are calibrated judgment, tuned openly
through rubric versions, not objective truth. The maintainer check stays because
fully automated scoring gets gamed: the rubric disciplines the check, and the check
catches the AI's mistakes.
