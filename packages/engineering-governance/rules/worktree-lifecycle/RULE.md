## Worktree lifecycle and freshness

A Git worktree is a bounded execution surface, not a durable placeholder or a speculative cache for possible future work. Every non-infrastructure worktree must have an active owner, an unresolved purpose, and an explicit exit condition.

Before starting any new engineering task in a repository:

1. Read the repository's authoritative worktree state first (prefer `git worktree list --porcelain`; use the Orca-managed view when Orca owns the worktree).
2. Inspect candidate worktrees before creating another one. Prefer, in order: reuse the current compatible worktree → reuse an existing available worktree → create a new worktree only when real isolation or parallelism requires it.
3. Never create or retain a worktree merely because it might be useful later. Prefer freshness over speculative compatibility.
4. When a new worktree is created, record at least: base, branch/HEAD, purpose, owner/task, and exit condition. For Orca-managed work, bind the worktree lifecycle to the owning task/run rather than to a CLI process or terminal.

Freshness rule:

- If a non-infrastructure worktree has had no meaningful new work for 24 hours, it must enter resolution immediately and be closed.
- "Meaningful work" means intentional task progress such as a new authorized task, code/design changes, commits, reviewed dirty progress, or an explicitly active owner. Automated polling, logs, an open terminal, a surviving CLI process, idle agents, or mere filesystem timestamp churn do not reset the 24-hour clock.
- Resolution is `integrate | archive | discard`. Before removal, preserve any unique commit, valuable dirty change, or non-reconstructible artifact with an appropriate branch/ref/commit/patch/bundle/archive. Then remove the worktree and prune stale worktree metadata.
- Worktree cleanup and branch cleanup are separate decisions. Do not delete remote branches automatically.
- A primary/common-dir checkout, an actively deployed/runtime-coupled checkout, or another proven infrastructure dependency is an explicit exception to automatic 24-hour removal; document why it exists and do not treat it as a speculative development worktree.

For Orca, the worktree is the primary lifecycle object. CLI processes, terminals, and worker sessions may be reclaimed independently and never justify keeping an otherwise idle worktree alive. Task completion must trigger worktree resolution; an idle worktree without a current owner/purpose should not remain open.

