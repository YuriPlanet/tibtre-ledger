# Grading rules — v1.6

How accepted work is turned into tibtre. An AI and a maintainer use these rules
together, the same way for everyone, maintainers included.

## The formula

```
tibtre = base × difficulty × quality
```

- **Base:** the kind of work and how much it does for the project (tables below).
  Work players can see counts more than internal work of the same size. Line count
  and the number of PRs don't matter.
- **Difficulty:** ×1.5 for hard areas (simulation internals, renderer/GPU, netcode,
  reverse-engineering unlabeled code), otherwise ×1.0.
- **Quality:** ×1.25 for exceptional work (extra tests, docs or polish), ×1.0 for
  work accepted as it is, ×0.75 for work that needed a lot of rework by others.

The AI works out each factor with its [public instructions](ai-evaluation-prompt.md).
A maintainer checks them and can change one, writing down why. Several PRs that make
one piece of work count as one, and reverted work counts as zero.

Each person's total for an update is rounded to the nearest 0.5 (halves round up; at
least 0.5). How each piece of work was valued is published in `valuations/`.

## Base values

### Code
| Size | Definition | Base |
|---|---|---|
| XS | Typo, one-liner, config tweak | 0.25 |
| S | Contained fix, one file/subsystem | 0.75 |
| M | Feature or fix within one subsystem, incl. tests | 2 |
| L | Multi-subsystem feature or new module | 4 |
| XL | New system end-to-end | 8 |

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

## Examples

1. A small pathfinding fix in the simulation, accepted as it is:
   `0.75 (S code) × 1.5 (hard area) × 1.0 = 1.125`
2. A loading screen with exceptional polish:
   `3 (art) × 1.0 × 1.25 = 3.75`

## Bonuses

- **Recruiting:** paid only when the person you brought in gets their first grant,
  never for the invite itself. One recruit grant per newcomer.
- **Impact:** at milestones, such as a release or a wave of new players, maintainers
  may grant extra tibtre for work that clearly caused it. Each bonus names its public
  evidence.

## Versions

Each ledger row's note says which version it used. Old versions are in this file's
git history, and old grants are never repriced.

- **v1.6** (current, from 2026-10-20): code base values halved.
- **v1.5** (2026-10-18 to 2026-10-20, used for no grant): an AI and a maintainer
  value each piece of work together, the same way for everyone.
- **v1.4** (used once, 2026-10-18): every PR on one scale, set from the owner's own
  value.
- **v1.3 and earlier:** a maintainer's value and the AI's value were averaged.
