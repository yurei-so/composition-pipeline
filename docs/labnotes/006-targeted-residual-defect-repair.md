# Labnote 006: Targeted residual-defect repair

Date: 2026-08-23

## Hypothesis

A second model pass may justify its cost when restricted to repairing one
explicit residual defect in an otherwise complete direct rewrite, even though
unrestricted optional editing showed no preference advantage in Labnote 005.

## Frozen protocol

- Model: `qwen3:8b`.
- Temperature: 0.35 for baseline diversity; diagnosis, repair, and verification
  are deterministic.
- Corpus: 12 task families, two prompt styles, five repetitions (120 trials).
- Frozen defect taxonomy: omission, unsupported addition, instruction
  violation, awkward structure, tone mismatch, ambiguity, redundancy, or none.
- A diagnosis names one primary defect and anchors non-omission evidence to an
  exact candidate substring.
- Repair uses bounded exact-buffer operations and must make at least one change.
- An independent pass must confirm the defect was fixed without regression.
- Unchanged and duplicate pairs are excluded before review.
- Human review opens only with 12 unique verified pairs across six task families.

Raw prompts, candidates, evidence, operations, hashes, and mappings remain in
owner-only state. Public output contains only aggregate campaign telemetry.

## Status

Frozen implementation awaiting the coordinated Agent Runtime / roostd run.
