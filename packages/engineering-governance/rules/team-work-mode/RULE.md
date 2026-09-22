## GitLab team-work entry gate

Before any substantive engineering action in a Git repository, establish the repository's authoritative upstream once. Prefer the current branch's configured upstream remote, then `origin`, then other configured remotes. If that upstream URL's remote host identifies a GitLab host (case-insensitive `gitlab` in the host name), set **TEAM_WORK_MODE=ON** for the whole task. This gate runs before system-change discovery, robotics/domain skills, local design, or mutation. A remote that has not been observed is `UNKNOWN`, not "not GitLab".

When TEAM_WORK_MODE is on, treat the agent as an assigned contributor, not the project owner:

1. Recover current authoritative state: upstream/base, HEAD, worktree/dirty state, and already-proven task frontier.
2. Decode the assignment into `Role | Owned Surface | Claim | Forbidden Delta | Handoff Boundary`. Infer negative space from task verbs: migration preserves behavior unless explicitly changed; additive work does not authorize shared-infrastructure cleanup; audit is read-only unless mutation is assigned.
3. Read dependencies broadly but mutate narrowly. Dependency or call-path reachability grants inspection context, never ownership.
4. Run the relevant domain/robotics workflow inside that contract, then apply `software-engineering-review` for implementation correctness and proportional verification.
5. At every `problem discovered -> mutation proposed` transition, re-run the ownership gate. Classify the candidate as `EXPLICIT | NECESSARY | OBSERVED-UNOWNED`. A new problem is not a new assignment. Cross-owner findings become evidence + handoff/blocker unless the task explicitly reassigns that surface.
6. Verify both the requested capability and the forbidden-delta/regression invariants.
7. Before completion, audit every changed hunk back to both the current Claim and Owned Surface. Remove overreach with the smallest revert/compatibility patch; do not launch a cleanup/refactor to undo an over-broad change.
8. Report unowned findings separately instead of paying down adjacent debt.

TEAM_WORK_MODE has precedence over system discovery and optimization. No downstream skill, composition analysis, test failure, code smell, or reviewer suggestion may silently widen mutation authority.

