## Maintain the Why chain in long-running work

For any multi-step task that can drift into local implementation details, keep a compact causal anchor:

```
current action X
→ verifies/resolves Y
→ protects/enables Z
→ final user capability/outcome W
```

Use this as a lightweight invariant, not as another planning framework. Update it only when the goal, causal model, boundary, blocker, or chosen action materially changes. On resume/handoff/recovery restore at least: `user goal → current blocker/unknown → next discriminating action → Why chain → completion condition`. A command, ACK, log line, test, or local fix proves only its own contract unless it also establishes the next link. Stop when the final user capability or explicit completion condition is actually proven.

