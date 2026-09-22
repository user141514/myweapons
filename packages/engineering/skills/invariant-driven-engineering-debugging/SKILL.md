---
name: invariant-driven-engineering-debugging
description: Use when a bug survives repeated fixes, tests pass but the user still fails, stateful systems behave differently across environments, or debugging is expanding into explanations without converging on a reproducible root cause.
---

# Invariant-Driven Engineering Debugging

## Core idea

Stop accumulating explanations. Convert the user's failure into a **state-transition contract**, identify the invariant being violated, and validate through independent evidence domains.

The final test must reproduce the user's control plane, not the engineer's privileged environment.

## Phase 1 — Define the real capability

Write the user's requirement as:

`Initial reality → user action → required final reality`

Do not substitute a weaker capability such as “works when the app was already running.”

Keep explicit:
- Actual / Claimed / Observed / Verified / Authorized capability
- Reality–Model gap
- Intent–Specification gap
- Local Legality–Global Outcome gap

## Phase 2 — Recover authoritative state

Before mutation, collect facts from the lowest independent layers available:
- OS/process/filesystem/network state
- command resolution
- version/hash/profile identity
- persistent metadata
- Git/worktree state

After every external mutation or timeout, reacquire state before the next mutation.

Never turn “failure history” into progress by itself.

## Phase 3 — Find the invariant

Prefer one invariant over many patches.

Examples:
- `START(target) ⇒ no incompatible prior owner exists`
- `one physical path ⇒ at most one logical workspace owner`
- `prompt written but unacknowledged ≠ safe to replay`
- `same instance identity must connect process, profile, runtime, and transport`

Ask:
1. What real state is missing from the model?
2. What legal actions compose into an unintended capability?
3. What metric can pass while the user goal fails?
4. What state expands future option/control?
5. What composition creates an emergent failure?
6. What sequence is locally legal but globally wrong?

## Phase 4 — Use orthogonal validation

Repeated checks are not independent evidence.

Use different models:

### Temporal/OS evidence
Process start/stop events, executable path, command line, creation time.

### Metamorphic evidence
Run the same action from:
- zero state;
- wrong pre-existing state;
- correct pre-existing state;
- concurrent callers.

### External functional oracle
Use a nonce/sentinel/result the verifier can independently validate.

If the system under test is the orchestration layer, launch independent reviewers directly from the system shell.

## Phase 5 — TDD against the real failure shape

Before production code:
1. reproduce the real failure;
2. capture the exact return/error shape;
3. write a regression test using that shape;
4. watch it fail;
5. implement the smallest invariant-preserving change.

A mock that models the wrong layer is not a regression test.

After mocks pass, repeat the exact user-path live gate.

## Phase 6 — Isolate without inventing product constraints

Use an isolated worktree for risky source changes when the authoritative checkout is dirty.

But do **not** make “must already be inside a Git worktree” a product requirement. If the product only needs a filesystem workspace, use a unique temporary folder workspace.

Do not silently select a random existing repo.

## Phase 7 — Promote only after user-equivalent acceptance

Promotion requires:
- deterministic tests;
- static/type/lint gates;
- user-shell live test;
- cold-start test;
- warm/reuse test;
- wrong-state replacement test;
- concurrent test when ownership is shared;
- rollback anchor.

Then fix the public entrypoint so the user's future command takes the same path as the validated artifact.

## Common failure patterns

- Warm-path success presented as cold-start success.
- Old processes hide a broken new build.
- A new binary launches with an old/default profile.
- Multiple verifies all query the same stale authority.
- The verifier mutates the system while “observing” it.
- Retry creates duplicate effects after an ambiguous acknowledgement.
- A reviewer times out and the timeout is treated as a code finding.
- A passing internal harness uses environment variables the user will never have.
- Fixing a wrapper instead of the shared lifecycle primitive.

## Stop condition

Stop investigation when one causal model explains all observed facts and a minimal change restores the invariant across the acceptance matrix. Do not keep expanding the search tree after that point without new contradictory evidence.
