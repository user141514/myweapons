## Optimization / review-admission gate

Optimization is bounded work, not an open-ended approach toward an imagined perfect system. Before accepting any optimization, reviewer finding, child-conversation suggestion, subagent recommendation, or "while here" improvement into the main task, the coordinator/main conversation must adjudicate it.

Treat external/child review output as **advisory evidence**, never as mutation authority. A reviewer may discover a real defect and still be outside the current task. No child worker, auditor, review tool, test failure, benchmark result, or model recommendation may directly create new scope.

For each proposed follow-up classify:

`ACCEPT | DEFER/HANDOFF | REJECT | BLOCKER`

using:

- **Claim relevance** — does it materially improve or unblock the requested outcome?
- **Ownership** — is this contributor authorized to mutate that surface?
- **Invariant necessity** — does the current system violate a required invariant without it?
- **Evidence quality** — is the issue demonstrated, or only a plausible improvement?
- **Marginal value** — what concrete user/system benefit remains after the current acceptance target is already met?
- **Cost/risk** — review burden, regression surface, compatibility, time, and coordination cost.
- **Stop condition** — has the requested capability already reached its agreed acceptance threshold?

"Cleaner", "more robust", "more elegant", "future-proof", "one more optimization", "the reviewer suggested it", or "we can make the score slightly better" are not sufficient admission reasons by themselves.

Once the Claim and required invariants are proven, default to **STOP**. Additional optimization requires a new concrete deficit, acceptance target, or explicitly authorized objective. Perfect correctness, maximum hardening, and exhaustive optimization are not implicit goals.

A child/subagent audit must return findings to the main conversation. The main conversation decides which findings enter the task; rejected/deferred findings remain notes or handoffs and must not be silently implemented by the child or by the next worker.

<!-- BEGIN SYSTEM-CHANGE-ENGINEERING -->
