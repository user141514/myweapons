# Molecular-AI Grounding Acceptance Scenarios

These are process tests, not scientific results. A scenario passes only when the agent separates anticipated risk from observed evidence and keeps molecular semantics aligned with the AI operation.

| ID | Pressure scenario | Required behavior | Fail behavior |
|---|---|---|---|
| M1 | A 3D molecular diffusion causal probe moves Cartesian coordinates along an edge-logit gradient | Ask whether the displacement is a physically/chemically admissible molecular perturbation or only an OOD model probe; gate bond lengths/angles/torsions, chirality, clashes and energetic plausibility before a physical interpretation; keep the route alive until the gate is measured | Treat any finite Cartesian vector as a valid molecular intervention, or abandon the route merely because invalidity is possible |
| M2 | Graph diffusion independently edits bonds and atom types | Freeze valence/formal-charge/aromaticity/stereo/connectivity semantics and raw-vs-repaired endpoints; identify which invalid states are allowed latent states versus claimed molecules | Assume a generic graph edit is chemically meaningful, or let sanitization/repair hide generator failures |
| M3 | Joint graph-coordinate model perturbs the two channels independently | Check whether the method requires graph-coordinate consistency at that stage, what conditional dependence is lost, and whether the state is latent/noisy or decoded molecular state | Demand physical validity at every noisy step, or ignore coupling when the state is claimed as molecular |
| M4 | Protein/complex model moves atoms freely to improve a score | Identify covalent backbone/side-chain geometry, chirality, rigid-body/interface degrees of freedom, clashes and environment-dependent states before interpreting the move physically | Treat protein coordinates as unconstrained Euclidean vectors |
| M5 | Reaction generator proposes arbitrary graph edits | Require atom mapping, element/mass/charge bookkeeping, bond-change semantics and reaction-condition scope before claiming a reaction | Treat reactions as arbitrary before/after graph differences |
| M6 | A candidate may fail because of a molecular constraint, but no measurement exists yet | Register the dead-node risk, derive a cheap discriminating probe, continue the current route until evidence triggers its stop rule | Switch direction on speculation, or ignore the risk until an expensive endpoint failure |
| M7 | A diffusion forward process intentionally creates nonphysical noisy states | Permit them if they are explicitly algorithmic states and the training/reverse semantics are well-defined; apply molecular feasibility gates at decoded/interpreted states and at physically claimed interventions | Reject diffusion because intermediate states are not molecules |
| M8 | A model produces diverse coordinates but identical molecular graphs | Distinguish conformational diversity from chemical-identity diversity and identify which endpoint the claim needs | Count coordinate separation as new molecules without checking identity semantics |
| M9 | A repair pipeline turns invalid raw generations into valid molecules | Report raw and repaired denominators separately and test whether the claimed mechanism acts before or after repair | Redefine generator validity using repaired outputs |
| M10 | An algorithm respects valence but claims a physically accessible transition | Add energy/kinetic accessibility only if the claim requires a physical path; do not require kinetics for a purely generative latent transition | Equate chemical validity with physical accessibility, or impose unnecessary physics on a nonphysical latent process |

## Behavior-record format

For each scenario record: `object semantics -> molecular constraints -> AI operation -> predicted dead node -> cheapest proof -> evidence status -> continue/kill rule -> unsupported claim`.

A GREEN agent must explicitly distinguish:

- **known constraint**: established chemistry/physics/data semantics;
- **predicted risk**: a reason a candidate might fail;
- **observed blocker**: measured evidence that activates a stop/revision rule.

Prediction is not permission to switch research direction. Ignorance until failure is also not acceptable.
