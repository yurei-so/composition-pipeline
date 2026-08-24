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
- Repair returns one bounded complete buffer which the controller applies as an
  exact whole-buffer replacement, and it must make at least one change.
- An independent pass must confirm the defect was fixed without regression.
- Unchanged and duplicate pairs are excluded before review.
- Human review opens only with 12 unique verified pairs across six task families.

Raw prompts, candidates, evidence, operations, hashes, and mappings remain in
owner-only state. Public output contains only aggregate campaign telemetry.

## Status

Protocol v3 is frozen and awaiting its coordinated Agent Runtime / roostd run.

The initial v1 execution completed 120/120 trials with no scheduler failures,
but is invalid for scientific interpretation. It diagnosed 40 residual defects
and then rejected every repair document at the edit-protocol boundary (29
missing finalization operations, 10 invalid delete shapes, and one invalid
replace shape). No repair was applied and no review opened. Version 2 replaces
the unnecessarily expressive edit document with one bounded complete buffer
that the controller applies as an exact whole-buffer replacement. The v1 state
remains preserved and v2 uses a fresh state directory and campaign digest.

The v2 replacement then halted safely after 24 trials because seven transient
`OllamaError` failures exceeded the precommitted 15% failure-rate ceiling.
Ollama remained active with zero service restarts and its API stayed healthy.
No repair reached verification and no review opened, so v2 is also invalid for
scientific interpretation. Version 3 keeps the same trial and review budgets
but permits four bounded retries per trial and again uses a fresh state path and
campaign digest.
