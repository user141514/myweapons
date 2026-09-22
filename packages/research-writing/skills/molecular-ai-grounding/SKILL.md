---
name: molecular-ai-grounding
description: Use when designing, auditing, or advancing AI/ML methods whose states, interventions, or outputs are molecules, biomolecules, molecular graphs, 3D conformations, complexes, or reactions, especially when an algorithmic abstraction may silently violate chemistry, geometry, physics, symmetry, or molecular identity semantics.
---

# Molecular-AI Grounding

## Principle

Treat the molecule as an **object with a contract**, not as an arbitrary graph/vector/point cloud. Before accepting an AI operation, state what molecular object the model variable represents and which constraints the scientific claim actually requires.

The goal is early prediction and cheap proof of dead nodes — **not premature route switching**.

## Required loop

For every new representation, corruption, transition, intervention, loss, decoder, or causal probe, write:

`state semantics -> required molecular constraints -> AI operation -> predicted failure -> cheapest discriminator -> continue/revise/kill rule`

Classify every concern as:

- **KNOWN**: established molecular/physical/data constraint;
- **PREDICTED**: plausible dead node not yet observed;
- **OBSERVED**: measured evidence from the current system.

A PREDICTED risk must trigger a bounded test, **not a direction change**. Kill or redirect only when evidence activates a preregistered stop rule.

## Constraint ladder

Require only the level needed by the claim:

1. **Identity / graph** — atom identity, bond semantics, formal charge, valence, aromaticity, connectivity, stereochemistry.
2. **Geometry** — bonded geometry, torsions, chirality, nonbonded clashes, graph-coordinate consistency.
3. **Physical accessibility** — energy/forces, environment, protonation/tautomer state, kinetics or pathway plausibility.
4. **Biological context** — protein/complex state, interface, cofactors/metals, solvent/pH, experimental state.

Do not equate graph validity with physical accessibility. Do not demand physical accessibility from a deliberately nonphysical latent/noisy state.

## Hard gates

- Declare whether a state is `latent/noisy`, `decoded molecule`, `conformer`, `physical ensemble`, `complex`, or `reaction state`.
- Preserve atom-index/permutation semantics and the required rotation/translation/reflection symmetry; check chirality before using reflection-equivariant assumptions.
- Separate **raw generator output** from sanitization, reconstruction, minimization, or repair.
- A Cartesian perturbation is a physical intervention only after molecular-admissibility checks; otherwise label it an **OOD model probe** and forbid physical causal interpretation.
- When graph and coordinates are jointly modeled, test whether the operation destroys required graph-coordinate dependence.
- If a method relies on chemistry being repaired afterward, measure how much of the claimed gain comes from repair.

## Early dead-node protocol

Before an expensive experiment, list at most three molecular failure modes that could invalidate the algorithmic claim. For each, define the cheapest decisive check. Continue the active route while those checks are unresolved.

If a check fails, first ask whether the intervention can be corrected **without changing the hypothesis**. Only kill the route when the required molecular semantics are incompatible with the mechanism or the corrected intervention fails its scientific gate.

Read `references/object-contracts.md` for object-specific constraints and `references/acceptance-scenarios.md` when deploying or auditing this skill.
