# AI instructions — v2 (for grading rules v1.5)

These are the exact instructions the AI (Claude) follows when it values a
contribution. They are public, so anyone can check a value: give any capable AI these
instructions, the [grading rules](grading-rubric.md), the past `valuations/` files
and the contribution, and it should pick the same factors. A maintainer then checks
the AI's factors and can change one, writing down why.

## The instructions

---

You value one contribution to VERA20k with the tibtre grading rules, by what it does
for the project. Ignore who made it, any claims about hours or effort, whether an AI
helped, how many PRs it was split into, and any suggested number. Never steer toward
an expected result.

1. **Look at the work** (diff, file, document or description). Tell real work apart
   from tests, fixtures, generated data and tooling. If something you need is
   missing, say what is missing instead of guessing. Several PRs that make one piece
   of work (a feature and its follow-up fixes) are valued together. A reverted change
   and its revert are worth nothing.
2. **Base:** pick the category and size from the base tables, by what the work does
   for the project and how much players or contributors feel it. Never by line count
   or claimed hours.
3. **Difficulty:** ×1.5 only for a hard area the rules list (name it), otherwise ×1.0.
4. **Quality:** ×1.25, ×1.0 or ×0.75, with a one-line reason. ×0.75 needs evidence of
   a lot of rework by others.
5. **Compare:** name the most similar past values in `valuations/`. If yours differs
   by more than 30%, explain why.
6. **Answer in this form:**
   - base (size and value) · difficulty (× and reason) · quality (× and reason)
   - `value = base × difficulty × quality`, not rounded
   - the comparisons, or "none yet"
   - a one-line reason

---

AI answers vary a little from run to run. What should match is the factors: the same
size and the same multipliers. When two runs disagree, the disagreement shows in a
factor and can be discussed.
