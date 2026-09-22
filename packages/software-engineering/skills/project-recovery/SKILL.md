---
name: project-recovery
description: For ANY project-recovery task where prior project state must be reconstructed before acting — including "继续之前的项目", "接着上次", "对齐进度", "恢复断点", old conversation URLs, memory/checkpoint recovery, or continuation after a conversation, session, machine, worktree, or runtime switch — read this skill before graft, mymem, conversation-history search, grep, source inspection, or mutation. Do not trigger for ordinary same-thread continuation when the current authoritative state is already present.
---

# Project Recovery

## Purpose

Recover the **correct execution frontier**, not the most recent-looking note.

The recovery target is always this pair:

```text
latest accepted transition
+
first unresolved transition
```

Do not rebuild the entire project history unless that pair cannot be established.

## Core invariant

```text
No resume before identity and authority are established.
```

A newer timestamp, a semantically similar note, a memory summary, or an agent saying "done" must never override a mismatched project/workspace/runtime identity or stronger current evidence.

Recovery is read-only until the resume frontier is proven.

## Trigger behavior

Use this skill when the task is behaviorally a recovery, even if the user does not name the skill. Typical triggers include:

- "继续之前那个项目"
- "接着上次"
- "对齐进度"
- "恢复上次工作"
- "从这个对话继续"
- "根据本地 memory 恢复"
- "别重新调研，从断点继续"
- "看看之前做到哪里"
- continuation after a conversation, machine, worker, daemon, browser, or runtime switch

Do not trigger merely because a repository has history. Trigger when the model must decide **what prior state is safe to resume from**.

### Routing precedence

If a request matches both project recovery and another retrieval/work skill, read `project-recovery` first. It determines the target control path and resume frontier; only then hand off to `graft`, `mymem`, `research-convergence`, debugging, or other skills. If the current thread already contains the authoritative state and no reconstruction is needed, skip this skill.

## Recovery contract

Run the following gates in order. Do not reorder them by convenience.

### Gate 1 — Establish project identity

Identify the smallest set of identity fields that can distinguish the intended project from nearby lookalikes.

Possible identity fields:

- project/repository root
- remote/repository identity
- branch
- checkout/worktree
- HEAD/commit
- dirty-tree state
- candidate/card/experiment ID
- conversation/project URL or conversation ID
- runtime/installation/profile
- hardware/device/robot target
- external registry/watch/task ID

Only require fields relevant to this project.

**Rule:** recency is allowed to rank candidates only *after* project identity matches.

If two candidates remain identity-compatible, keep both until stronger evidence separates them.

### Gate 2 — Identify the state owner

Determine which source actually owns current truth for the transition being recovered.

Examples:

| Transition | Typical authority |
|---|---|
| code state | current checkout/worktree + Git state |
| deployed/runtime behavior | live runtime/process/service state |
| Watchdog mount | live registry + exact conversation identity |
| browser binding | current URL/DOM/binding state |
| research decision | frozen decision/card + exact experiment evidence |
| experiment completion | manifest/result aggregate/hash/validator output |
| cross-host memory | current memory archive/runtime records with provenance |
| hardware state | current device/runtime telemetry, not an old log |

Use project-specific authoritative files when repository instructions define them.

A checkpoint, summary, chat, or memory can point to the authority; it does not automatically replace the authority.

### Gate 3 — Re-read current authoritative state

Before accepting an old checkpoint, read the current state owner when accessible.

After any external or asynchronous mutation, re-read it again before accepting success. This includes:

- browser navigation or reload
- daemon/service restart
- extension reload
- remote registration
- worker/agent execution
- GUI interaction
- hardware action
- long-running/asynchronous job

```text
mutation receipt != final state
agent claim != final state
```

If live state conflicts with an older checkpoint, live authoritative state wins unless there is concrete evidence that the live state belongs to the wrong identity.

### Gate 4 — Find the latest accepted transition

Search for **state-changing evidence**, not merely recent files.

Prefer this retrieval order:

1. exact project identity
2. exact anchors from the user's request: IDs, filenames, candidate names, commit hashes, quoted phrases
3. state-transition evidence: Git log/reflog/status/diff, decision files, manifests, registries, test/live-gate results
4. recency within identity-compatible evidence
5. semantic search to fill remaining gaps

Use `rg`/`grep`/`find`/Git or project-native retrieval tools only inside bounded roots whenever possible. Exclude generated/cache/build noise unless it is itself evidence for the transition.

An accepted transition must have evidence that the relevant authority moved from one state to another.

**Do not require the cause or actor to be known before accepting an observed state change.** If a previously verified authority was in state A and a later authoritative read proves state B, then `A -> B` is an accepted transition even when *why* or *who* caused it remains unresolved. Record the causal gap separately; do not downgrade the observed transition to "no transition".

When multiple accepted transitions exist, `LATEST ACCEPTED TRANSITION` is **exactly one transition**: the newest authoritative transition on the target control path the user is trying to resume. A successful transition in another worktree, checkout, runtime, conversation, device, candidate, or side branch is **off-path evidence** and must go under `CONFLICTS`, never in `LATEST ACCEPTED TRANSITION`. If no accepted transition exists on the target control path, write `NONE on target control path` and state the latest verified target state instead.

Examples:

```text
FAIL -> verified PASS
unregistered -> registry contains exact target
old HEAD -> intended commit present in actual working checkout
CARD -> PILOT because frozen gate passed
pending -> completed because aggregate/manifest exists and validates
```

Do not promote these to accepted transitions by themselves:

- "assistant said fixed"
- "worker said done"
- a directory exists
- a build artifact is newer
- a memory summary says the next step changed
- a chat ended after a proposed action

Treat them as observations that may lead to proof.

### Gate 5 — Locate the first unresolved transition

Starting from the latest accepted transition, identify the first edge whose outcome is not yet proven.

Model recovery as:

```text
S0 --accepted--> S1 --accepted--> S2 --unresolved--> S3
                                      ^
                               resume frontier
```

Resume at the unresolved edge, not by replaying S0..S2 and not by jumping ahead to S3.

If an apparent later state exists but its transition evidence is incomplete, keep the frontier before it.

### Gate 6 — Check for contradictory newer evidence

Before resuming, ask:

- Is there a newer authoritative state that invalidates the checkpoint?
- Did the project move to another worktree/branch/runtime/conversation?
- Did a later failure reopen a transition previously thought closed?
- Did the user explicitly supersede the old direction?
- Is a "done" claim missing independent verification?
- Is the newest file only generated/cache/log noise?

If any answer is yes, update the recovered model before acting.

### Gate 7 — Stop searching and resume

Stop recovery once all are true:

```text
project identity is unique enough
AND current authoritative state has been read
AND latest accepted transition is identified
AND first unresolved transition is identified
AND no newer contradictory authoritative evidence remains
```

Then continue the task from that frontier.

Do not keep doing historical archaeology merely because more history exists.

## Fast path: verified recovery checkpoint

If a project has a structured recovery checkpoint, use it as an **index** first.

A useful checkpoint records:

- project/workspace identity
- authoritative root/state owner
- last accepted transition
- verification evidence
- first unresolved transition
- next safe action
- timestamp and relevant hashes/IDs

Fast path:

```text
read checkpoint
-> verify current identity
-> re-read current authority
-> if consistent, resume its unresolved transition
```

If identity or authority conflicts, abandon the fast path and use forensic recovery. Never force current reality to fit an old checkpoint.

## Forensic fallback

Use when no valid checkpoint exists or the checkpoint conflicts with current state.

Bound the search before scanning.

Preferred mechanical evidence collection:

- `git status --short`
- `git log --date=iso --name-status`
- `git reflog --date=iso`
- exact-ID / exact-phrase `rg` or `grep`
- recent modification times only inside identity-compatible roots
- current decision/card/manifest/result files
- current runtime/registry state

Do not scan an entire disk when a repository root, memory root, or project root is already known.

Semantic retrieval is a fallback for missing links, not the primary authority-selection mechanism.

## Evidence classes

Keep these classes distinct:

- **Claim** — someone or an agent says something happened.
- **Observation** — evidence was seen, but may not prove the target transition.
- **Verified state** — the relevant authority was independently checked.
- **Accepted transition** — verified evidence proves movement from the prior state to the new state.
- **Unresolved transition** — the next state change lacks sufficient proof.

Do not silently upgrade one class into another.

An unverified claim is **UNKNOWN**, not FALSE. Lack of verification proves only that the transition is unresolved; it does not prove that the claimed action failed.

## Conflict rules

Use these rules before inventing a weighted score:

1. Identity mismatch disqualifies a candidate.
2. Current authoritative state outranks stale remembered state.
3. Independent verification outranks an agent completion claim.
4. Exact transition evidence outranks semantic similarity.
5. Recency breaks ties only among identity-compatible evidence.
6. If strong authorities genuinely disagree, expose the conflict and recover to the last state that is still jointly supported.

Do not average contradictory authorities into a synthetic state.

## Read-only rule during recovery

Before the frontier is proven, do not:

- edit files
- checkout/reset/clean/rebase
- restart services
- remount/register external state
- rerun expensive experiments
- launch new worker branches
- delete or overwrite checkpoints

Read-only commands and queries are allowed.

If recovering the state itself requires a mutation, first report why read-only evidence is insufficient and identify the smallest reversible mutation.

## Output contract

Keep the recovery report compact:

```text
PROJECT
<identity>

AUTHORITY
<current state owner and current identity>

LATEST ACCEPTED TRANSITION
<what is actually proven>

FIRST UNRESOLVED TRANSITION
<the exact edge where work should resume>

CONFLICTS
<none, or concrete stale/conflicting evidence>

NEXT SAFE ACTION
<one imperative sentence naming exactly one bounded action that advances or verifies the unresolved edge>

`NEXT SAFE ACTION` is the final field. End the recovery report immediately after that one sentence.

If the unresolved edge can still be checked with a read-only query, that read is the entire next action. Do not combine it with a contingent mutation such as "query, then mount if absent". Observe first; mutation belongs to a later step after the new evidence exists.
```

Do not narrate the entire project history unless the user explicitly asks.

## Common recovery failures

| Failure | Correction |
|---|---|
| newest file treated as newest work | look for accepted state transition |
| related memory from another project wins | apply identity gate first |
| old checkpoint treated as truth | re-read current authority |
| correct repo, wrong worktree | verify checkout/worktree/HEAD/dirty state |
| agent says "done" | find independent authority evidence |
| command returned success | re-read external state |
| semantic search returns a plausible old note | search exact anchors + transition evidence |
| recovery becomes endless archaeology | stop at latest accepted + first unresolved |

## Handoff to other skills

After recovery identifies the frontier, use the skill appropriate to the actual next behavior.

Examples:

- use `graft` for indexed code localization after the frontier is known
- use `mymem` for cross-host memory archive operations
- use `research-convergence` for choosing the next scientific discriminator
- use debugging skills when the recovered frontier is an unresolved defect

Those skills may provide evidence; this skill decides **which prior state is safe to resume from**.
