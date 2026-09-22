## Resume / recovery frontier gate

When a task is a continuation, handoff, retry after interruption, new conversation over existing work, or recovery from a tool/runtime failure, restore the **evidence frontier before rediscovery**. Read the latest authoritative handoff/checkpoint and only the live state that can have become stale. Use `reanchor` when available.

Maintain:
`Claim | Proven boundary | Invalidated evidence | First unknown frontier | Next discriminating action | Stop condition`.

Previously verified gates, source relationships, measurements, rejected routes, and negative results stay frozen unless a concrete new observation invalidates them. A new session, different worker, daemon reconnect, or desire for extra confidence is not invalidation. Do not repeat side-effectful tests merely to rebuild context.

If the checkpoint says `G0-G3 PASS; G4 unknown`, work starts at G4. If later evidence moves the frontier further downstream, do not fall back to G3. If the next unknown requires a new owner, authorization, physical observable, or inaccessible runtime, hand off / request that boundary instead of substituting broader research or larger stimulation.

Recovery refreshes **volatile state**, not settled knowledge. The first action after recovery must either validate a stale prerequisite or advance the first real unknown; otherwise it is duplicate work.

