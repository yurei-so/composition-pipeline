# Runtime Roost experiment contract

Composition Pipeline experiments run through Agent Runtime's one-shot experiment
manager. They are not roost members, handoffs, agents, or independent accelerator
clients.

The ownership boundary is:

1. An operator registers a fixed definition in Agent Runtime using an absolute
   repository root and the absolute `scripts/run-experiment` path.
2. Agent Runtime owns request persistence, revision-bound approval, the complete
   non-preemptive roostd accelerator lease, timeout enforcement, output limits,
   private logs, audit, and restart recovery.
3. The repository runner validates a fixed experiment identifier and executes
   only `experiments/<identifier>/run.py` from this repository.
4. The experiment writes bounded machine-readable results to standard output and
   diagnostics to standard error. Agent Runtime captures both privately.

The runner deliberately provides no shell mode, arbitrary executable option,
network setup, scheduler integration, or accelerator ownership. Definitions
must keep arguments and environment fixed and reviewable.

Copy `config/agent-runtime.experiments.example.json`, replace `USER` with the
deployment account, and merge its definition into Agent Runtime's managed
experiment definition file. The checked-in `contract_smoke` entry is CPU-only
and exists solely to verify admission and execution wiring; real composition
experiments may use the accelerator only while Agent Runtime holds their lease.
