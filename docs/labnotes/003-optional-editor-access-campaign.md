# Labnote 003: Optional editor-access campaign

Date: 2026-08-23

## Hypothesis

Giving a model optional access to constrained revision after a matched direct
rewrite may improve judged output without forcing a mutation. Finalizing the
initial candidate unchanged is a first-class treatment outcome.

## Frozen protocol

- Experiment: `labnote_003`
- Agent Runtime run: `9e55ef72-4817-4b2a-b07f-b51102e425aa`
- Campaign digest: `6728008926b7d896ced277199b03748c3beda1400a0ea1a152a6dd8f879fadd3`
- Repository revisions: `9a57f28`, corrected by `fd4c02f`
- Model: `qwen3:8b`
- Arms: matched direct rewrite and optional editor access
- Planned trials: 48
- Blinded pairs: 24
- Accelerator ownership: one non-preemptive roostd experiment lease

The optional arm receives the same deterministic initial rewrite as its matched
direct arm, followed by one editor decision. It may finalize unchanged or apply
bounded revision operations. Invalid editor output is recorded as a protocol
failure and transactionally falls back to the unchanged initial candidate, so
failure cannot selectively remove a difficult case from human review.

Raw prompts, drafts, generated texts, editor operations, telemetry, review
pairs, and the arm-reveal key remain in owner-only private state.

## Runtime result

The authoritative campaign completed all 48 trials successfully at the
execution layer and released its accelerator lease normally.

| Arm | Completed | Protocol success | Transactional fallback |
| --- | ---: | ---: | ---: |
| Direct rewrite | 24 | 24/24 | 0 |
| Optional editor access | 24 | 12/24 | 12 |

All 24 matched comparisons remain in the blinded review set. The public review
bundle digest is
`534755a72c09fcc375f580bb0afbb36bd6801b8db35a575ea1371c999fdd6f8e`.

The original pilot retained only valid optional-editor trials and would have
created survivor bias. It is preserved as diagnostic evidence but is not an
inferential campaign. The authoritative rerun uses the frozen
`transactional-fallback-v1` protocol revision.

## Blinded review status

A fresh owner-only review session has been prepared with deterministic
counterbalancing and append-only judgments. It begins at 0/24. Treatment labels
and aggregate results remain unavailable until all 24 judgments are durably
committed. Human review is intentionally not supervised by the experiment
runner.

## Pending interpretation

After the reveal gate opens, evaluate overall preference, voluntary edit rate,
preference conditional on editing or leaving unchanged, cost, and protocol
failures. Do not treat mechanical success or fallback behavior as evidence of
output quality, and do not rescue the hypothesis if the blinded result is
negative.
