---
name: lifetime
description: Use when a local command or OMP agent may outlive a tool call, work appears stalled, a result may have been lost, a running execution needs cancellation, or a durable agent session needs continuation from DevSpace or another shell-capable host.
---

# Lifetime

Use the independent `lifetime` CLI through the host's existing shell tool. This is not a new MCP tool and does not modify DevSpace. Start identification with `lifetime doctor` and `lifetime --help`.

## Platform and installation

Implementation 0.2 supports Linux and Windows 10+. Linux scopes execution to a process group; Windows atomically assigns the child to an owned Job Object. No OS sandbox, brokered-process guarantee, forced parent-job escape, or automatic provider fallback is provided.

Install from a stable checkout, **not a disposable worktree**: `python scripts/install.py` (`python3` on Linux). Installed entrypoints reference the checkout; deleting it breaks them. Linux installs `~/.local/bin/lifetime` plus a skill link. Windows installs `~/bin/lifetime.cmd`, a Git Bash `lifetime` entry, and a checksum-marked copy of this skill without symlink/admin rights. Reinstall after source updates to refresh the copied skill; refuse unrelated/edited files. Do not edit PATH or restart DevSpace. A full executable path works when the user bin is not in PATH.

Windows PowerShell: `& "$HOME\bin\lifetime.cmd" doctor`. Use native `omp.exe`. Batch commands as managed targets require explicit `cmd.exe /d /c`; never implicitly turn ordinary argv into CMD shell text. Use UTF-8 `--prompt-file` for complicated/large text and `--tools=` to disable tools across shells.

## Submit once, observe many times

Choose a stable request key before submission. Lost responses must not cause a new key or another model run. Repeat the same arguments and key to recover the original receipt, or use `list` / `status`.

```text
lifetime start --workspace . --key build-check-01 --max-wall 600 -- python -m unittest discover -s tests
lifetime status TURN
lifetime wait TURN --max-wait 10
lifetime events TURN
```

Use this machine's Python executable (`python3` where appropriate). Replace TURN with the actual returned `turn_id`, not `agent_id`. `ok:true` means the CLI operation succeeded; check `data.phase`, `data.outcome`, `data.quiescent` and `data.result` separately. Success of process backend means exit zero plus owned-scope quiescence, not verified business-goal completion.

Start ACK proves durable acceptance. Bounded waits return within 20 seconds and do not cancel work. Never keep one MCP request waiting for the whole agent task. The tool does not wake a stopped ChatGPT turn or promise later delivery.

## Official OMP and continuation

```text
lifetime start --workspace . --key review-01 --backend omp --thinking low --max-wall 300 --prompt "Read-only review of current code; do not edit."
lifetime start --workspace . --key review-followup-01 --backend omp --agent AGENT --thinking low --max-wall 300 --prompt "Recheck the previously reported defects."
```

AGENT is the returned `agent_id`. The second command creates a new Turn and reuses the native session. Default tools are glob/grep/read; `--tools=` disables all. Broader tools need explicit write access and authorization. Provider tool selection / read access are not an OS sandbox. Do not silently change provider/model on failure.

The runtime inherits the caller's environment. A service shell may lack an interactive terminal's proxy settings. Inspect relevant variables/listeners only; use an existing authorized proxy per invocation when evidence requires it. Never change VPN nodes, global configuration, auth files, or official services to make a test pass.

## Interpret evidence

`stalled` is a gap in progress evidence, not proven deadlock. Supervisor heartbeat, provider responsiveness, output activity, and native milestones differ. Silent compilation may still progress. OMP prompt ACK and partial agent_end never prove completion.

`unknown` requires observation, not automatic retry. Inspect status and then `reconcile`. Reconcile probes exact owned identities; it does not launch replacements. Lease expiry is not proof of death.

```text
lifetime cancel TURN
lifetime wait TURN --max-wait 10
```

Cancel ACK is intent only. Report stopped only after terminal outcome and `quiescent:true`. On Windows, Job termination replaces Unix process-group signaling. If a supervisor disappears and its named Job cannot be queried, preserve unknown even though kill-on-close initiates cleanup. Never kill an arbitrary PID or restart DevSpace as a cancellation mechanism.

Recovery is explicit: `lifetime recover TURN --revision N --ack-effects`. Use only after the old scope is proven gone and the user accepts possible prior effects. Unknown ownership blocks recovery. A terminal Turn is not resurrected; a new task needs a new key.

## Persistence / discovery boundaries

State is under `LIFETIME_STATE_DIR` / `--state-dir`, otherwise Linux `~/.local/state/lifetime` or Windows `%LOCALAPPDATA%\lifetime\state`. Never share a provider/DevSpace DB. Raw native logs and sessions may contain sensitive prompt/code data and remain local, outside Git.

Linux commands must not daemonize/escape the declared process group. Windows work stays within the permitted host Job hierarchy; killing that hierarchy can also kill lifetime. No security-sandbox claim is implied.

A newly opened DevSpace workspace can discover the installed skill. Already-loaded metadata may be cached; do not repeatedly reopen the active workspace just to refresh it. Installed command paths can be used directly regardless of the metadata cache.
