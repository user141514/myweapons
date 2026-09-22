---
name: robotics-engineering-sop
description: "Mandatory external execution trajectory for substantive robotics engineering work: ROS2/control/runtime debugging, latency or performance measurement, hardware integration, simulation-to-real, deployment, robot-state diagnosis, and real-device experiments. This skill constrains observable work gates and evidence, not private reasoning. Read it before acting on such tasks. Do not use it for simple conceptual explanations."
---

# Robotics Engineering SOP

This SOP constrains the observable engineering trajectory. It does not prescribe chain-of-thought or tell the model how to reason internally.

The user's explicit task and scope remain authoritative. Do not reopen settled design questions or broaden the task merely to satisfy this SOP.

When global `TEAM_WORK_MODE=ON`, the decoded team contract is an execution invariant: broad robot/system evidence may be inspected, but every mutation must remain inside the Owned Surface and support the current Claim. A newly discovered cross-owner defect is not a new robotics task; preserve the evidence and hand it off unless it is an explicit blocker that the assignment authorizes this contributor to change.

## Gate 0 — Contract

Before acting, establish only what is needed to execute the current task:

- exact target outcome;
- allowed mutation boundary;
- current execution endpoint/workspace when relevant;
- safety or authorization boundary for real hardware.

Reuse requirements already established in the conversation or project. Do not ask again when they are already known.

For a new capability/vertical module or an unresolved owner, consumer, repository, or deployment boundary, first use `system-change-engineering` at `/home/ad/.agents/skills/system-change-engineering/SKILL.md` to derive the minimal change SURFACE. Reuse an existing verified SURFACE on resume; this is not permission to rescan the robot, discover unrelated repositories, or reopen settled work. New cross-boundary evidence reopens only its affected frontier.

## Gate 1 — Ground

Ground the task in authoritative current evidence before changing anything.

Prefer, in order:

1. current runtime / device state for facts that can change;
2. current checkout, deployed binary, configuration, logs, traces, and project-local contracts;
3. direct dependencies actually used by the project;
4. external upstream only when local evidence leaves a material unknown and ownership/compatibility is established.

If the repository is indexed by Graft, use Graft to locate the relevant code path instead of rebuilding repository understanding from broad reads.

Refresh state, not knowledge. Re-check PIDs, modes, devices, network, ROS graph, serial identities, or other volatile prerequisites when they may have changed. Do not re-prove stable source relationships or already-recorded measurements without a concrete invalidation reason.

### State authority and cross-flow race check

When a control, safety, or handoff decision depends on software state, do not equate a stored value with the physical/runtime fact it is meant to represent.

- Identify the authoritative owner of each decisive fact. Treat cross-process cached state as a shadow unless its provenance, freshness, lifecycle/generation, and confirmation semantics are established.
- Default initialization, process restart, timeout/error handling, or an asynchronous request being sent must not silently become proof that the remote operation completed. `UNKNOWN` is distinct from confirmed false/safe.
- Find every control flow that can change the same invariant, even when they write different variables. If one flow can invalidate another flow's checked precondition before commit, treat it as a semantic/TOCTOU race.
- Conflicting transitions need one acceptance/linearization boundary: check the precondition, reserve it against conflicting transitions, then commit. A mutex local to one ROS2 node does not protect an invariant spanning multiple nodes.
- Define the transition interval, not only the before/after states. During controller/owner handoff, actuator output must remain defined; command silence is safe only when the downstream timeout/hold semantics are verified at the owning boundary.

### Operational invariants beyond local code

When inheriting an unfamiliar robot project, or when a surprising system-wide behavior appears, explicitly recover the non-local operating rules before treating nearby source code as the complete system contract.

- Determine the **fault domain and recovery unit**: if one critical node/process fails, what is actually restarted, deactivated, or invalidated — that node, a node group, the control stack, or the whole robot? Supervisor/watchdog/lifecycle policy is authoritative over a local `respawn` flag. Do not infer global recovery semantics from node-local launch settings alone.
- Determine the **lifecycle boundary**: startup order, safe initial state, shutdown behavior, degraded mode, what state survives restart, and which components are assumed to share one lifecycle.
- Search evidence in this order: supervisor/watchdog/lifecycle manager and process manager configuration; bringup/deploy scripts; integration/E2E/acceptance tests; runbooks/safety/commissioning docs; incident logs/postmortems; current operator or subsystem owner. External upstream docs, standards, and mature sibling stacks may suggest candidate patterns, but never prove this project's policy by analogy.
- If a rule appears to be "industry common", first turn it into a candidate invariant, then seek project-local confirmation. Absence of contradictory source code is not confirmation.
- Record each recovered rule as: `scope | trigger | guaranteed behavior | owner | evidence | invalidating counterexample`. A load-bearing unknown stays `UNKNOWN`; do not silently fill it with a plausible convention.

## Gate 2 — Establish the evidence boundary

Identify the strongest transition already proven by current evidence and the next observable transition required by the user's claim.

Do not repeat completed gates merely because a new session began. Repeat only the prerequisite whose authoritative state has become stale or whose evidence was invalidated.

For a measurement or debugging task, name the endpoint before perturbing the system. If the requested endpoint is not observable yet, instrument it first.

## Gate 3 — Probe

Choose the smallest reversible operation that can distinguish the live hypotheses or advance the evidence boundary.

- Prefer read-only observation before mutation.
- Prefer one bounded change or stimulus at a time.
- For real hardware, establish the current operating mode and other action-specific preconditions immediately before mutation.
- Do not increase motion magnitude, permissions, architectural scope, or destructive impact to compensate for poor observability.
- Do not treat repeated retries as a debugging method. If a probe contradicts the prediction, update the causal model before another mutation.

If the same class of failure repeats because the agent cannot observe or enforce something, treat that as a harness gap: add or request the smallest missing tool, trace, guardrail, or deterministic check instead of adding more exhortative instructions.

## Gate 4 — Execute and observe

Execute the approved bounded step and capture the evidence needed to correlate cause and effect.

For latency/control experiments, preserve timestamps and identity across the relevant boundary. For software changes, preserve the exact diff and runtime/build identity. For hardware, preserve the command/stimulus identity and downstream observation.

Acceptance, publication, syscall entry, log emission, or command submission proves only that boundary. Do not silently promote it to execution, physical response, or task completion.

## Gate 5 — Verify and close

Validate the outcome at the same level as the claim.

- Source claim -> source evidence.
- Runtime claim -> fresh runtime evidence.
- Protocol/wire claim -> packet/interface evidence.
- Physical claim -> physical/device feedback or an explicitly justified physical measurement endpoint.

Use proportional verification. Run the checks needed for the actual change or claim; once they pass, broaden or repeat testing only when new failures, changes, or unresolved risk justify it.

When a result contradicts the prediction, stop at the first contradicted/unsupported transition and continue from there. Do not restart the whole task.

At completion or handoff, preserve a compact checkpoint containing:

- proven boundary;
- concrete evidence/result;
- current unresolved boundary, if any;
- only the volatile prerequisites that must be refreshed next time;
- failed approaches that must not be repeated when they are materially likely to recur.

Claim completion no further than the evidence supports.

## External reference fallback

`robotics-upstream` is a late fallback, not a default robotics step. Use it only when Gates 1-2 leave a material unknown and a specific external source is proven to own or compatibly define that unknown. Cross-company similarity is analogy, not evidence.

## Human escalation

Escalate only when the next step requires user judgment, authorization, inaccessible physical evidence, or a risk decision that cannot be resolved from the available contract and observations. Do not escalate routine gaps that can be resolved by existing tools and evidence.
