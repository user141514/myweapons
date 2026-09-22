# Watchdog V1 Runtime Notes — non-authoritative hints

Last observed: 2026-09-19 on devnbook9.

These notes are only discovery accelerators. The live runtime must be re-observed before use.

## Observed Watchdog runtime

A live process was observed with a command shape equivalent to:

python -m chat_watchdog
--registry-port 9235
--relay-url http://127.0.0.1:9224
--poll-seconds 15
--intent-url http://127.0.0.1:7337/internal/conversation-intents

The actual running implementation came from a deployed runtime/venv, while the development checkout at E:\Dev\chat-watchdog had older source. This is the concrete reason the Skill must prefer runtime discovery.

## Observed registry contract

- GET /watches
- POST /register with an exact ChatGPT conversation URL
- POST /unregister with conversation UUID or URL
- POST /completion with conversation UUID or URL
- POST /completion/ack with conversation UUID or URL

The registry is in-memory in the observed implementation.

## Observed managed semantics

Registry watcher construction was equivalent to:

conversation UUID from target URL
-> exact relay attach for /c/<uuid>
-> Supervisor with observation-only page + intent client + state client

Therefore a successful new register call proves exact relay attachment succeeded, but does not prove Sidecar authoritative state exists.

The managed state owner was the sibling /internal/conversation-state endpoint of the configured /internal/conversation-intents owner.

Observed state-owner lookup uses Sidecar’s local ConversationStore external-URL binding. A relay-visible main ChatGPT conversation that Sidecar has never adopted can therefore return:

found=false, reason=target_unavailable

Such a target must be classified as NOT_MOUNTABLE_MANAGED, even if registry insertion would succeed.

## Current-conversation identity gap

A current-turn text match across relay pages was experimentally able to locate the apparent caller page, but adversarial review rejected this as mutation authority.

Reason: content coincidence is possible. A different relay-visible conversation may contain the same user turn while the actual caller conversation is unavailable, producing a false “self” binding.

Therefore current/self mounting requires either:

- an explicit exact URL supplied by the user/trusted task context; or
- a trusted caller/self-identity hook.

Text/title/active-tab matching is diagnostic only.
