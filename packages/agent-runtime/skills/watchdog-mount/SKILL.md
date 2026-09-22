---
name: watchdog-mount
description: >-
  Use whenever a task needs to mount, attach, register, move, verify, diagnose,
  or remove Watchdog supervision for an exact ChatGPT conversation, especially
  requests like “挂上 watchdog”, “挂当前对话”, “把 watchdog 切到这个对话”,
  “确认是否真的挂载成功”, or “删除旧的 watchdog 注册”. Behavior-triggered:
  the user does not need to name this skill. Dynamically discover the running
  Watchdog and prove an operational exact-conversation binding; never trust a
  hard-coded path, a register ACK, a UI badge, a title, an active tab, or list
  presence alone.
---

# Watchdog Mount

## Purpose

Complete one Watchdog control-plane binding transaction and prove it.

Do not equate any of these with success:

- a Watchdog process exists;
- a URL appears in a registry or UI;
- POST /register returned 200;
- the active browser tab looks like the requested conversation;
- a page title or Project name matches;
- a DOM symptom looks healthy.

The success claim is stronger:

exact target identity
+ live Watchdog runtime discovered
+ exact relay attachment possible
+ authoritative owner accepts and discovers the target
+ registry mutation accepted
+ registry read-back matches
+ post-poll state remains coherent

If any required layer is unavailable, report the precise partial state instead of saying “mounted”.

## Core model: control flow != message flow

Control flow:

resolve exact conversation
-> discover live Watchdog runtime and protocol
-> read-only authority preflight
-> register or unregister
-> read-back
-> post-poll verification

Message flow:

Watchdog policy
-> authoritative state
-> continuation Intent
-> Sidecar admission
-> browser effect

Mount verification must not inject a test continuation or any synthetic user message.
Do not prove control-plane health by mutating the message plane.

## Non-negotiable invariants

1. Runtime truth > source assumption. Discover the running process and protocol first. A development checkout, old command, remembered port, installed CLI, or cached path is not authority.
2. Exact conversation identity > title/tab heuristics. Use the exact ChatGPT /c/<uuid> identity.
3. Self means self. A request to watch this/current conversation may target only the caller’s exact conversation. Never substitute another visible ChatGPT tab.
4. No silent managed -> legacy downgrade. If the live Watchdog is managed by Sidecar and Sidecar cannot authoritatively resolve the target, fail closed.
5. Registration ACK is not operational proof.
6. List presence is not operational proof.
7. Observation is not permission.
8. Do not delete unknown registrations. Remove only an exact target the user identified, a target already established by current conversation context, or a registration created by this transaction during rollback.
9. A bounded child or worker may not mount a parent or arbitrary external conversation from an agent-supplied URL unless the user or trusted runtime explicitly authorized that exact target.
10. Do not repair product code while mounting. If runtime/source drift or protocol failure is found, classify it; do not opportunistically patch Watchdog or Sidecar unless the user asked for repair.

## Phase 0 — Establish requested scope

Determine whether the user wants:

- mount current/self conversation;
- mount an explicit exact URL;
- replace a known old registration with the current/exact target;
- verify an existing mount;
- remove a known registration.

If an exact target was provided, preserve it.

If the request says current, this conversation, itself, or equivalent, resolve self identity using the rules below. If no trusted self hook exists, request the exact URL rather than guessing from browser observations.

## Phase 1 — Discover the live runtime

Do not begin from a repository path.

### 1. Find the running Watchdog

Inspect live processes and listeners and identify the process whose command line owns Watchdog registry mode.

Capture:

- PID;
- executable/runtime environment;
- registry host/port or control URL;
- poll interval;
- managed intent/state owner endpoint, if any;
- whether legacy direct send is explicitly enabled.

Then correlate the advertised registry socket back to the operating-system listener owner.

Required:

- the discovered host/port is actually LISTENING;
- the listener PID is the same Watchdog runtime process, or the listener child process is explicitly identified and becomes the runtime PID used for the rest of this transaction;
- the listener process command line/runtime identity is consistent with Watchdog registry mode.

A process merely advertising "--registry-port" is not evidence that it owns that port.

Current command-line strings such as "-m chat_watchdog" and "--registry-port" are discovery hints only, not permanent contract.

If endpoint ownership cannot be correlated, or more than one plausible registry is live and ownership cannot be disambiguated, stop with AMBIGUOUS_RUNTIME.

### 2. Verify the discovered control protocol

Read the running runtime’s installed package or release, not an arbitrary dev checkout, when protocol details are needed.

A source/runtime mismatch is evidence, not permission to choose the source tree.

Probe the discovered registry read surface. For a runtime that exposes the current V1 adapter, GET /watches returning the expected JSON object is the control-plane read gate. If the live runtime exposes a different protocol, inspect that runtime and follow it.

### 3. Determine writer mode

Classify the live Watchdog as:

- managed: policy/intent client, Sidecar owns effects;
- legacy_direct: Watchdog may write browser state directly.

Never silently switch modes to make a target mountable.

## Phase 2 — Resolve the exact target

### Preferred identity sources, in order

1. Explicit exact URL supplied by the user in this conversation, or an exact URL already established by trusted task context.
2. A trusted caller/self-identity hook that cryptographically or structurally binds this tool invocation to one ChatGPT conversation UUID.
3. If neither exists, stop with SELF_ID_UNRESOLVED and request the exact conversation URL.

There is currently no approved heuristic that can turn “current conversation” into mutation authority.

### Candidate discovery is not identity authority

Relay inspection, latest-user-message matching, title matching, active-tab state, Project membership, recent logs, and registry contents may be used only to produce diagnostic candidates.

Even an exactly unique current-turn text match does not prove caller identity. Another conversation can contain the same content while the actual caller is unavailable or hidden.

A candidate discovered heuristically may be shown to the user for confirmation, but it must not be registered, unregistered, or used to claim “current/self” without an explicit URL or trusted self hook.

### Forbidden self-resolution fallbacks

Never choose a target for mutation solely because it is:

- the active tab;
- the newest tab;
- the only visible ChatGPT tab;
- the current page title;
- the Project title;
- a current-turn or prior-turn text match;
- the URL most recently mentioned in logs;
- the only existing Watchdog registration.

## Phase 3 — Read-only preflight before registry mutation

### Relay gate

Prove the exact /c/<uuid> page can be attached and read through the same live relay surface used by Watchdog.

A registration API that internally creates the watcher may also prove this during registration, but perform a read-only check first when possible.

### Managed-mode Sidecar gate

When the live Watchdog is managed, derive or discover its authoritative state-owner endpoint from the live runtime configuration.

Before trusting that endpoint, correlate its listening socket to the live Sidecar runtime process. When available, also read Sidecar health/release identity. A stale or unrelated service on the expected port is not an authoritative owner merely because it speaks compatible JSON.

Read the exact target from Sidecar.

Required:

- endpoint listener ownership is correlated to the live Sidecar runtime;
- the owner responds with its valid protocol;
- found == true;
- returned target identity resolves to the same ChatGPT conversation UUID;
- writer mode is compatible with managed Watchdog operation.

If Sidecar returns target_unavailable, ambiguous_local_binding, protocol-invalid state, or an identity mismatch:

NOT_MOUNTABLE_MANAGED

Do not register merely to make the URL appear in Watchdog.

Do not synthesize or adopt a Sidecar conversation by directly editing stores or calling undocumented internals.

### Legacy mode

If the live runtime is explicitly legacy_direct, Sidecar authority may not apply. Verify exact relay attachment and clearly classify the result as LEGACY_MOUNTED, not as managed correctness.

## Phase 4 — Register as a transaction

Only after read-only preflight passes:

1. submit the exact target to the live registry using its actual protocol;
2. require the returned conversation identity to equal the target UUID;
3. record whether this transaction created a new registration or reused an existing one;
4. immediately read the registry back;
5. require exactly one entry for that UUID.

Do not trust created=false as proof that the submitted URL replaced an old entry. Current V1 registries may deduplicate by UUID and retain older metadata.

Compare by stable conversation UUID first. Record raw URL differences as metadata drift and continue only if the operational target identity still proves the same conversation.

## Phase 5 — Prove operational mount

A real mount must survive re-observation.

### Immediate gates

Require all applicable evidence:

- exact target UUID resolved;
- relay attachment/read succeeded;
- managed Sidecar state preflight succeeded;
- registration response identity matched;
- registry read-back contains the same UUID.

### Post-poll gate

Discover the live poll interval from the runtime, then re-observe after at least one Watchdog poll cycle.

Check:

1. registry entry still exists for the exact UUID, or the completion record proves it was mounted and then completed;
2. watcher state is a recognized runtime state;
3. managed Sidecar authoritative state is still readable and identity-consistent.

Valid watcher states such as active, waiting, need_input, delivery_uncertain, or blocked describe task/control state; they do not by themselves mean the mount failed.

If the watch disappeared without a corresponding completion record, verification failed.

### Rollback

If this transaction created the registration and later verification fails, remove that exact newly created registration when safe.

If the registration pre-existed, do not unregister it automatically; report the mismatch or blocker.

## Phase 6 — Report evidence, not a vague success claim

Use one of these outcomes.

### WATCHDOG_MOUNTED

All managed-mode gates passed.

Report:

target UUID
resolved exact URL
runtime PID or runtime identity
registry control endpoint
mode = managed
relay attachment = verified
Sidecar authoritative state = verified
registry write = created or existing
registry read-back = verified
post-poll watcher state = ...

### WATCHDOG_MOUNTED_PAUSED

Mount is operational but current state intentionally prevents continuation, for example:

- need_input;
- delivery_uncertain;
- a valid non-continuable waiting state.

### WATCHDOG_MOUNTED_COMPLETED

The target was successfully mounted and reached completion before or at post-poll verification.

### LEGACY_MOUNTED

Explicit legacy-direct mode only. State that Sidecar single-writer guarantees were not part of this proof.

### NOT_MOUNTABLE_MANAGED

The registry or relay may be healthy, but Sidecar does not authoritatively own or discover the target. Do not call this mounted.

### REGISTERED_BUT_NOT_OPERATIONAL

Use only when diagnosing a pre-existing or externally created partial registration that appears in the registry but fails authority or operational gates.

### Other blockers

- NO_WATCHDOG_RUNTIME
- AMBIGUOUS_RUNTIME
- LISTENER_OWNER_MISMATCH
- SELF_ID_UNRESOLVED
- RELAY_TARGET_UNAVAILABLE
- REGISTRY_REJECTED
- REGISTRY_READBACK_MISMATCH
- STATE_PROTOCOL_INVALID
- POST_POLL_VERIFICATION_FAILED

## Replacement / moving Watchdog

“Move Watchdog to current conversation” is not permission to clear the registry.

Safe sequence:

resolve + fully verify new target
-> establish new registration
-> identify old target from explicit user instruction or already-authoritative task context
-> unregister only that exact old target
-> re-read registry to prove new remains and old is gone

If the old registration cannot be identified exactly, keep it and report that cleanup is unresolved.

Never remove all watches as a convenience.

## Current V1 adapter — use only after runtime confirmation

A currently observed V1 runtime has exposed operations equivalent to:

GET  /watches
POST /register
POST /unregister
POST /completion
POST /completion/ack

and managed Watchdog reads a localhost Sidecar conversation-state owner paired with its intent owner.

These endpoints are not the Skill’s source of truth. Before using them, verify that the live runtime actually exposes this adapter.

Important current semantics:

- register is keyed by ChatGPT conversation UUID;
- current register construction attaches the watcher to the exact relay conversation;
- existing UUID registration may return success without replacing stored target metadata;
- registry state alone does not prove Sidecar can operate on the target;
- managed Watchdog must fail closed when Sidecar authoritative state is unavailable.

## What to ignore

Do not spend mount time:

- rebuilding Watchdog;
- rebasing repos;
- repairing unrelated Sidecar bugs;
- improving frontend indicators;
- rewriting lifecycle architecture;
- sending a test continuation;
- cleaning unrelated stale registrations.

Those are separate engineering tasks.

## Upstream architectural direction

This Skill is intentionally a development-stage adapter around the current registry.

As the Sidecar–Watchdog control protocol matures, replace URL-centric success gates with:

TaskExecution
+ ExecutionBinding
+ SupervisionGrant
+ authoritative ConversationControlState

The Skill should then become thinner, but its invariant remains:

Never claim supervision exists until the exact target, authority, registration, and read-back state all agree.
