---
name: software-engineering-review
description: Use for ANY real software-engineering task where you are about to inspect, modify, integrate, debug, test, deploy, recover, or make a readiness/completion claim about a codebase or running system. Trigger from the engineering behavior you are about to perform, not from the user naming this skill. Before proposing a fix or changing code, establish the claim, causal model, invariant, counterexample, smallest decision, and evidence. For cross-component, ownership, identity, lifecycle, persistence, completion, synchronization, repeated-fix, or new-service/protocol work, first run the composition gate in this skill so locally correct changes cannot accumulate into an incoherent system. Do not use for purely conceptual programming questions with no real codebase/system or intended engineering action.
---

# Software Engineering Review

## Trigger contract

Treat this as a **behavior-triggered process skill**. Do not wait for the user to say "use the software-engineering skill."

Invoke it before acting whenever the next meaningful step would operate on a real software artifact or runtime state—for example: reading code to locate a bug, editing implementation, changing an interface, integrating components, running tests to establish correctness, deploying, recovering a service, or declaring work complete/ready.

The trigger is the intended engineering behavior, not specific wording in the request. A user can describe the symptom, desired change, or system state without mentioning this skill at all.

Do not trigger it for a purely conceptual programming explanation, toy example, or general knowledge question where no real codebase/system is being inspected or changed.

Build the smallest causal model that supports a decision. This is a practical engineering lens, not a new controller, a substitute for authorization, or a guarantee of correctness.

## Size the work

For an isolated edit, use a short note and focused checks. For interface, persistence, security, or lifecycle changes, expand the affected boundary. Use an existing spec or plan; do not create parallel paperwork.

## Composition gate — only when structure can interact

Local correctness is not assumed to be closed under composition. Before local design, run this gate when **any** of these signals is present:

- two or more components/processes/hosts can accept, derive, or act on the same identity, authority, lifecycle, completion, retry, ordering, or persistent state;
- the change adds or changes a registry, grant, cache with behavioral effect, reconciliation/synchronization path, fallback writer, adapter-owned state, service, protocol, or cross-boundary persistence;
- a state transition gains another writer/acceptance path, or ownership/source-of-truth is moving;
- several individually reasonable fixes have accumulated around the same boundary, or a new fix compensates for another component's behavior;
- the task changes a shared interface/contract such that multiple locally correct components may disagree after the change.

Skip this gate for a genuinely isolated edit with one owner, no shared contract/state transition, and no evidence of repeated boundary failure. Multiple files alone do not trigger it.

When triggered, answer only what is needed to choose the architecture:

1. **System outcome.** What user-visible capability must remain true after the change?
2. **Overlap.** Which existing components already own, derive, cache, observe, or mutate the same concept? Distinguish authority from read-only replicas/projections.
3. **Closure.** What combined state can be illegal even if every component satisfies its own local invariant? Write the smallest interaction/composition invariant that excludes it.
4. **Common primitive.** Is the proposed addition genuinely independent, a projection of an existing owner, or evidence that both old and new behavior should be expressed through one upstream primitive/interface? Do not abstract merely because code looks similar.
5. **Ownership.** For every relevant transition, name the acceptance authority/writer or the explicit consistency protocol. Avoid a second independently effective truth source.
6. **System counterexample.** Construct one path where focused/unit tests for each component pass but the user's end-to-end outcome is still wrong. If no plausible path exists, do not invent architecture work.
7. **Decision.** Prefer, in order: reuse an owner interface → derived/rebuildable projection → extract a real shared primitive → add an independent component only when its responsibility is actually independent.

A repeated need for `sync`, `reconcile`, `mirror`, `fallback`, cross-component compensation, or duplicate lifecycle/authority is a signal to re-check the decomposition, not automatic proof that centralization is correct. Legitimate caches, logs, replicas, quorum systems, and orthogonal state dimensions must remain possible.

After the composition decision is clear, continue with the local proof below. The composition gate decides **whether this structure should exist and how it fits**; the local proof decides **how to implement the chosen boundary correctly**.

## Claim → Model → Invariant → Counterexample → Decision → Evidence

**Claim.** State the observable user outcome, scope, non-goals, and constraints: safety, disruption, resources, and compatibility. First validate that the proposed requirement serves that outcome.

**Model.** Identify objects, stable identities, permitted transitions, and who accepts each state change. Draw only relevant dependencies:
`A --[phase, required operation, evidence]--> B`.
Separate build/install/startup dependencies from ongoing runtime dependencies and optional integrations. Mark each edge confirmed, hypothesized, or unknown. Co-occurrence and an unsuccessful source search prove neither dependence nor independence.

**Invariant.** Specify the precondition, postcondition, failure semantics, and property that must survive change. Distinguish the state dimensions relevant here: process existence, service readiness, target binding, progress, completion, authorization. An ACK proves only its documented contract. A timeout leaves remote effects unknown. Prompt guidance is not enforcement.

**Counterexample.** Challenge the decisive assumption with an alternative explanation or adverse sequence. Ask what observation would disprove the current model. Reason about loss, duplication, stale evidence, restart, or a dependency failure where relevant. Do not inject faults into production to answer a design question.

**Decision.** Choose the smallest authorized change at the owning boundary, including no change. Prefer existing interfaces after checking their preconditions; source inspection is diagnostic, not routine invocation. Consider coupling, information hiding, operational cost, and rollback. Preserve identity and uncertain work; retry only under the actual idempotency contract. Put enforceable safety constraints in owning code, not another hand-maintained truth table.

**Evidence.** Select the cheapest check that distinguishes the hypotheses and matches the claim. Bind evidence to host, target, version/instance, and observation time. Re-observe after relevant state changes. Keep source, build, installation, running instance, and user-visible outcome separate. Check both contract conformance and intended use. Missing or truncated evidence stays unverified.

## Working output

Maintain one compact note:
`Outcome | causal model + unknown | invariant | counterexample | smallest action + rollback | evidence + next decision`.

Expose only the conclusion, decisive evidence, and real blocker to the user. Reuse authorized test objects and respect the shared send/resource budget. Stop expanding analysis once an authorized, reversible discriminating action is available.

## Existing workflows and references

Use this lens within Superpowers brainstorming or systematic-debugging, not as another approval ceremony. Use TDD for implementation and verification-before-completion before success claims.

Read only the relevant section of [the engineering model](references/engineering-model.md). Provenance and limits: [sources](references/sources.md). Behavioral acceptance: [scenarios](references/acceptance-scenarios.md).
