---
name: robotics-work-router
description: Use when a robotics task is underspecified, the starting point is unclear, or the work likely depends on reusing or migrating an existing simulation, controller, runtime, evaluation, deployment, or sibling task.
---

# Robotics Work Router

Route before solving. The goal is to shrink the search space until one concrete unknown blocks progress.

Use this before `robotics-engineering-sop` while the task is too ambiguous to know what deserves attention. Once the frontier is concrete, hand execution to that SOP.

When global `TEAM_WORK_MODE=ON`, route only inside the assigned contribution contract. References and dependency tracing may cross repositories to understand the path, but they do not authorize edits outside the Owned Surface. If the FRONTIER lands in another owner's surface, return a handoff/blocker or an owned-side workaround rather than silently absorbing that work.

## Unknown ownership / vertical capability trigger

When the request adds a capability or vertical module and the owner, consumers, repositories, or execution boundary are not established, read `system-change-engineering` at `/home/ad/.agents/skills/system-change-engineering/SKILL.md` before choosing where to implement. Do not ask the user to enumerate repositories that provenance and project evidence can reveal. One repository is not an exemption; every robot layer is not a mandatory target.

Keep the five fields below and attach the returned SURFACE to DELTA. Once it is sufficient, hand off to the existing engineering SOP rather than starting another discovery loop. Previously proven slices stay frozen except for invalidated evidence.

## State

Maintain only five fields:

- **TARGET** — the observable result requested; preserve uncertainty instead of inventing requirements.
- **REFERENCE** — the nearest already-working task or artifact that could satisfy most of TARGET.
- **DELTA** — `TARGET - REFERENCE`, partitioned into `KEEP / CHANGE / UNKNOWN`.
- **FRONTIER** — the first unresolved transition that prevents REFERENCE from becoming TARGET.
- **PROBE** — the cheapest reversible action that can resolve or narrow that FRONTIER.

## Routing loop

1. **Recover TARGET.** Extract the requested observable outcome and constraints already known. Do not design yet.
2. **Find the nearest executable REFERENCE.** Prefer, in order: current-task history → current repo sibling → same-project sibling repo → local prior project/history → same-runtime internal example → direct upstream/vendor example → external repo/paper → from scratch.
3. **Rank references by operational similarity, not topic similarity.** Prefer matching hardware, runtime, inputs/outputs, environment, and acceptance criterion.
4. **Compute DELTA.** Freeze `KEEP`; do not reopen or re-research it without contradictory evidence. Search only `CHANGE` and `UNKNOWN`.
5. **Locate FRONTIER.** Pick the earliest unknown transition whose resolution changes what to do next. Ignore downstream unknowns until this one is crossed.
6. **Choose PROBE.** Maximize expected search-space reduction per cost and reversibility risk. A probe must answer a discriminating question; broad “research the topic” is not one. For requirement, authorization, or acceptance ambiguity, retrieve the task contract or ask the owner; do not experiment to choose human intent.
7. **Update and repeat.** Observation must change TARGET, REFERENCE, DELTA, or FRONTIER. If it changes none of them, stop that search branch.

## Search discipline

- For **behavior precedent**, prefer the nearest working sibling.
- For **API/contract semantics**, prefer the deployed owner/direct dependency/official source.
- Do not read the whole repository for orientation. Load only target/reference artifacts and evidence needed for the current frontier.
- Do not modify code while the frontier is still “I do not know where the behavior lives.”
- If no useful reference survives comparison, explicitly switch to `NEW_BUILD`; do not pretend a weak analogy is evidence.

## Stop conditions

Stop searching when the frontier is a reality question existing evidence cannot answer: runtime state, timing, simulation behavior, physical response, or another observable outcome. Hand it to `robotics-engineering-sop`. If it requires human intent or authority, request only that decision.

At handoff, state only: `TARGET | REFERENCE | KEEP | CHANGE | FRONTIER | next PROBE`.
