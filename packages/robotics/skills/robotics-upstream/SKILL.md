---
name: robotics-upstream
description: "Late fallback for robotics engineering when current runtime evidence, the active checkout, project-local protocol/wire contracts, and direct project dependencies do not resolve the material unknown. Use only after identifying who actually owns the questioned behavior and only when an external Unitree/NVIDIA/ROS/Isaac reference is demonstrably relevant by provenance, dependency, deployed identity, or compatibility. Do not trigger merely because a task mentions robots, Unitree, G1, ROS2, Isaac, motors, DDS, SDKs, sim-to-real, or deployment; unrelated vendor conventions are analogy, not evidence."
---

# Robotics Upstream

Use this skill only as a late external-reference fallback. Domain similarity does not create authority.

## Authority order

Before using this skill, prefer evidence in this order:

1. Fresh runtime / physical observations for the concrete deployed system.
2. The active checkout, deployed binary/configuration, and project-local docs that describe what actually runs.
3. Project-local interface, message, IDL/protobuf, packet-layout, serial-wire, and other protocol contracts.
4. Direct dependencies, vendored code, submodules, or SDK versions that the current project demonstrably uses.
5. External robotics upstream with proven ownership or compatibility for the unresolved behavior.
6. Cross-company or merely similar robot implementations only as analogy/candidate design, never as evidence about the current system.
7. General robotics knowledge last.

`graft` usually comes before this skill because it establishes the current implementation and helps identify the true behavior owner. `mhs-hardware-contract` may also come before this skill for real-device work because current device state outranks external source intent.

Do not use `robotics-upstream` if levels 1-4 already answer the material question. Do not infer that Unitree/NVIDIA/Isaac owns a behavior just because the hardware or task is robotic.

## When external upstream is justified

Use this skill only when both are true:

- the current project/runtime/protocol evidence leaves a material unknown; and
- there is evidence that a specific external upstream owns or compatibly defines that unknown, such as an actual dependency, imported SDK, vendored/submodule origin, deployed component identity, protocol lineage, or documented compatibility.

For an unresolved external-reference question, run the bundled read-only discovery helper:

```bash
python3 ~/.agents/skills/robotics-upstream/scripts/discover.py --workspace "$PWD" "<short task terms>"
```

It ranks project remotes/submodules, verified local Unitree/NVIDIA clones, then canonical official remotes. It never clones, fetches, checks out, or edits anything.

Use the result recursively in this order:

1. Current repository implementation and project-local docs/configuration.
2. Explicit vendored/submodule/third-party/reference repositories linked by the project.
3. Verified local official Unitree/NVIDIA upstream owning the questioned behavior.
4. Canonical official upstream when no suitable local clone exists.
5. General robotics knowledge only for gaps not resolved above.

Read `references/catalog.md` only when the discovery result leaves multiple plausible upstream families or you need to map a task to the owning upstream.

Do not inspect every upstream indiscriminately. Start from the symbol, interface, topic, device, runtime boundary, or behavior named in the task; follow references only as far as needed to resolve the first material unknown.

## Evidence discipline

Keep these distinct:

- **Observed project fact**: verified in the current checkout/runtime.
- **Upstream fact**: verified in the referenced official source.
- **Project divergence**: current project intentionally or accidentally differs from upstream.
- **Inference**: not directly established by either source.

When upstream and the current project disagree, the current checkout determines what the system actually does; upstream determines the reference behavior unless the project documents a deliberate divergence.

For runtime or hardware claims, source inspection does not substitute for observing authoritative runtime state.
