# Labnote 005: Stochastic deduplicated optional editor campaign

Date: 2026-08-23

## Hypothesis

A modest nonzero sampling temperature can produce enough distinct optional
editor outcomes to support a useful conditional blind review, provided exact
duplicate answer pairs are removed before operator intake and remain visible as
multiplicity telemetry rather than independent samples.

## Frozen protocol

- Experiment: `labnote_005`
- Agent Runtime run: `c7537f90-1641-45fc-b198-fae9d87132e0`
- Campaign digest: `0927d8781e5e5bc262a72bf52e8d4840c5196f02389f50969608b9269825f002`
- Repository revision: `73c9f2e`
- Model: `qwen3:8b`
- Temperature: 0.35
- Base seed: 20260825, varied by repetition
- Matched assignments: 120
- Execution trials: 240
- Protocol revision: `stochastic-deduplicated-review-v1`
- Accelerator ownership: one non-preemptive roostd experiment lease

Each optional result is self-matched against its exact pre-editor candidate.
Normalized-identical outputs become automatic ties. Normalized unordered
changed pairs are content-hashed globally, and exactly one representative from
each unique group enters blinded review. Duplicate multiplicity is retained as
aggregate telemetry but cannot inflate the manual sample.

Raw prompts, drafts, generated text, edit operations, pair hashes, mappings,
and review artifacts remain in owner-only private state.

## Runtime and uniqueness result

The campaign completed 240/240 execution trials with no campaign failures,
empty stderr, and a normal accelerator-lease release.

| Measurement | Count |
| --- | ---: |
| Matched assignments | 120 |
| Automatic ties | 92 |
| Changed trials | 28 |
| Unique changed answer pairs | 21 |
| Duplicate changed trials removed from review | 7 |
| Optional editor protocol success | 73/120 |
| Valid unchanged decisions | 44 |
| Voluntary edit decisions | 29 |
| Transactional fallbacks | 47 |

The changed-pair multiplicities were sixteen singleton groups, three groups of
two, and two groups of three. One voluntary edit normalized to no textual
change, leaving 28 changed trials. The 21 unique pairs span seven task/style
cells. The private operation aggregate contains one append, two deletes, and 61
replacements.

The public blinded bundle digest is
`3628dae66aeb0ed93fe4e7f575f1f6f6b4f3e42a3178534c6d00c6fe75057929`.

## Blinded review status

A fresh owner-only session is ready at 0/21. Candidate ordering is
deterministically counterbalanced, judgments are append-only, and treatment
labels and preferences remain reveal-gated until all 21 unique judgments are
durably committed. The 92 automatic ties and seven removed duplicate changed
trials remain part of the final frequency analysis but not separate review
questions.

## Pending interpretation

Report preference among the 21 unique changed pairs without treating duplicate
multiplicity as independent evidence. Separately report the all-assignment
effect with 92 automatic ties and the observed intervention, duplicate,
protocol-failure, latency, and token costs. Compare diversity against Labnote
004, but do not promote optional editing from the conditional subset alone.
