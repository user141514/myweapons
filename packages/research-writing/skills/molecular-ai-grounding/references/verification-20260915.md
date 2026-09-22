# molecular-ai-grounding verification — 2026-09-15

## Deployment checks

- Skill path: `C:/Users/Administrator/.agents/skills/molecular-ai-grounding/SKILL.md`
- YAML name: `molecular-ai-grounding`
- Description starts with `Use when` and contains trigger conditions rather than a workflow summary.
- Frontmatter length: 367 characters.
- Main body: ~415 words.
- References present: `object-contracts.md`, `acceptance-scenarios.md`.
- Actual DevSpace `open_workspace` discovery returned the skill by name and path. This is loader evidence, not just a filesystem check.

## RED evidence

Historical project failure: the MolDiff mechanism line proposed a Cartesian posterior-boundary perturbation before first establishing whether the manipulated coordinate state had a valid molecular/model-state interpretation. Physical/molecular admissibility was added only after the algorithmic mechanism had already been narrowed. This is the exact late-discovery failure pattern the user asked to prevent.

A blind pressure turn was also sent to the reused old `subagents` child before the skill existed. That child terminated with heading-only / truncated output, so it is recorded as an unusable behavioral RED, not as evidence about its scientific judgment.

## GREEN behavior test

Because the old child repeatedly terminated with truncated bodies, the user-authorized fallback was used: one new child was created inside the canonical `subagents` Project and is now the sole reusable child.

- Local conversation id: `conv_092719bf-a129-4fa7-930e-284b578230df`
- ChatGPT child UUID: `6aa8a0dc-ec20-83e8-9cc7-eddd01a288cf`
- Project: canonical `subagents`
- Thinking-strength readback before first send: `Extra High -> Extra High`
- Completion evidence: exact live DOM finished with marker `MOLAI_NEW_CHILD_GREEN_DONE`.

Pressure scenario: audit a MolDiff p750 coordinate-only intervention toward an actual edge-posterior boundary while graph/log states are frozen.

Observed required behaviors:

1. Classified p750 as a joint diffusion latent state, not a physical conformer.
2. Required representation/index/gauge/joint-state support while explicitly declining unnecessary equilibrium chemistry constraints at the latent stage.
3. Labeled coordinate-only joint-state OOD and distant-boundary concerns as `PREDICTED`, with no `OBSERVED` dead node yet.
4. Proposed a native-null calibration from the model's own coordinate transition before expensive suffix rollouts.
5. Explicitly said predicted risk does not authorize route switching; failure should first revise/kill the probe/claim, not the MolDiff research line.
6. Kept raw output separate from repair/sanitization.

GREEN result: PASS for scenario M1 and the central anti-premature-switch invariant.

## M7 anti-overconstraint GREEN

A second pressure test was sent to the same canonical child at verified `Extra High` to ensure the skill does not overcorrect by demanding physical-molecule validity from deliberately nonphysical diffusion states.

- Sidecar turn: `turn_1789440367976_e07d7867`
- Sidecar ledger later timed out, so completion was verified from the exact child UUID live DOM instead.
- Live DOM: `phase=finished`, substantive assistant body present, marker `MOLAI_M7_GREEN_DONE`.

Observed behavior:

1. Treated the intermediate state as an algorithmic diffusion/noisy state, not a physical conformer, Boltzmann sample, or chemical intermediate.
2. Required representation integrity, graph-coordinate identity, permutation/equivariant/gauge semantics, and consistency with the model's native forward/noisy-state family.
3. Explicitly did **not** require ordinary valence, equilibrium bond lengths/angles, clash-free geometry, energetic plausibility, sanitizability, or physical accessibility from that deliberately nonphysical intermediate state.
4. Reinstated molecular constraints at the decoded endpoint; latent-state freedom was not allowed to excuse invalid final molecules.
5. Identified joint graph-coordinate OOD relative to the native forward process as a `PREDICTED` dead-node risk and proposed a cheap native-noise distribution check rather than a route change.
6. Preserved the rule: revise/kill the construction only after evidence; do not kill the research direction from an unobserved risk.

M7 result: PASS. This closes the main reverse-failure mode of the skill: `molecule grounding != force every latent/noisy tensor to be a physical molecule`.

## Known transport issue

The previous child exposed two independent transport/completion defects: Sidecar ledger can remain `generating` after the browser has stopped, and a browser-terminal turn can contain only a truncated heading/body. Future child completion therefore requires: exact live DOM terminal + substantive body + expected marker. Ledger state alone is insufficient.
