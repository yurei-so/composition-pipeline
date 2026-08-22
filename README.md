# Composition Pipeline

Experimental middleware for model-directed composition, revision, and finalization.

This repository currently contains only the project scaffold. The composition
protocol and experiment design will be developed separately.

## Repository shape

```text
docs/          Architecture, policy, roadmap, and experiment labnotes
examples/      Small runnable examples
experiments/   Isolated experiment implementations
import/        Untracked local experiment inputs
scripts/       Development workflow helpers
src/           Installable Python package
tests/         Automated tests
```

See [DEVELOPMENT.md](DEVELOPMENT.md) for the local workflow.
See [docs/experiment-contract.md](docs/experiment-contract.md) for registration
with Agent Runtime's approval-gated roostd experiment path.
