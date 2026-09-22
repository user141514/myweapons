# Molecular object contracts for AI research

Use this reference only to determine whether an algorithmic operation is semantically compatible with the molecular object and scientific claim. It is not a requirement to enforce every physical law at every latent step.

## 1. State-semantics table

| State type | What it is allowed to violate | What must be preserved before making a claim |
|---|---|---|
| Latent / noisy diffusion state | Valence, bond geometry, energy, even recognizable molecular identity if the model definition permits it | Tensor/index semantics, corruption/reverse-process contract, symmetry assumptions, recoverability of the target endpoint |
| Decoded molecular graph | 3D energetic plausibility if no 3D claim is made | Element identity, bond order semantics, formal charge/valence policy, aromaticity convention, connectivity scope, stereochemistry required by task |
| 3D conformer | Global minimum energy; a conformer need not be the dominant ensemble member | Same molecular identity, bonded geometry, chirality, nonbonded sanity, coordinate-frame/symmetry semantics |
| Physical ensemble | Individual members may be rare | Defined thermodynamic/environmental state, meaningful weighting/sampling, protonation/tautomer policy, no arbitrary post-selection hidden from denominator |
| Protein / nucleic-acid structure | Exact experimental coordinates | Covalent chain connectivity, stereochemistry, bonded geometry, plausible backbone/side-chain or nucleotide conformations, clash policy; model-state context as required |
| Protein-ligand / biomolecular complex | Exact binding free energy unless claimed | Component identities, interface geometry, clashes, relevant protonation, metal/cofactor/solvent assumptions when they affect the claim |
| Reaction state / transformation | A transition-state path if only products are generated | Atom bookkeeping/mapping, element conservation, charge/valence policy, bond-change semantics, stoichiometric scope; conditions/mechanism only if claimed |
| Physical trajectory / causal perturbation | Nothing that breaks the intended physical interpretation without explicit relabeling | Admissible coordinates/internal degrees of freedom, environment, forces/energy or kinetic semantics required by the claim |

## 2. Small-molecule graph contract

Before treating a generated graph as a molecule, resolve:

- allowed elements/isotopes and implicit/explicit hydrogens;
- formal charge and radical policy;
- bond types/orders and aromaticity convention;
- element-dependent valence policy;
- single molecule vs salts/multifragment outputs;
- stereochemistry/chirality and whether it is represented, ignored, or evaluated;
- tautomer/protonation canonicalization policy if identity comparisons depend on it.

A toolkit sanitization pass is a **validator/transformer**, not evidence that the generator produced a valid raw molecule. RDKit sanitization explicitly checks properties such as valence and aromatic/kekulization consistency; preserve pre- and post-sanitization denominators separately.

## 3. 3D small-molecule contract

A set of Cartesian points is not automatically a molecular conformer. Check at the level needed by the claim:

- bond lengths for the decoded graph;
- bond angles and planarity constraints where relevant;
- torsions / ring conformations;
- chirality preservation or intentional inversion;
- nonbonded clashes;
- graph-coordinate consistency after bond edits;
- energy/force or minimization only when claiming physical accessibility or realistic conformers.

**Intervention rule:** a Cartesian displacement along an ML gradient is an algorithmic perturbation until molecular admissibility is measured. If the claim is physical, either use molecular internal coordinates/manifold-aware motion or demonstrate that the Cartesian move remains within the allowed molecular contract. Projection/minimization must be checked for whether it erases the intended intervention.

## 4. Protein and macromolecular contract

For protein-like structures, useful geometry checks include:

- covalent bond lengths/angles;
- chirality and planarity;
- close-contact/clash statistics;
- backbone torsion/Ramachandran plausibility;
- side-chain rotamers;
- chain breaks/disulfides and residue chemistry;
- metal coordination, cofactors, ligands, alternate states when relevant.

wwPDB validation reports explicitly separate standard covalent geometry, chirality/planarity, clashes, backbone torsions and side-chain rotamers. An ML score improvement does not replace these object-level checks when the output is claimed as a structure.

For complexes, additionally specify whether the model is allowed to change rigid-body placement, internal conformations, protonation, water/ion state, metal coordination, or covalent connectivity.

## 5. Symmetry and indexing contract

Molecular AI frequently fails before chemistry because representation symmetry and molecular semantics disagree.

- Atom ordering is arbitrary unless the task defines mapped identities; require permutation invariance/equivariance as appropriate.
- 3D coordinates normally require translation/rotation invariance or equivariance.
- Reflection symmetry is not harmless when chirality matters. A model equivariant to reflections can treat mirror-related configurations according to its parity design; verify that stereochemical information needed by the task is representable.
- A graph-coordinate pair must use the same atom indexing. Shuffling either side can create a fake joint-information signal.
- For periodic/crystal systems, cell and periodic-image semantics are part of the object contract.

## 6. Diffusion / flow / generative-transition contract

Do not apply endpoint chemistry rules blindly to every intermediate state.

Ask, for each timestep/state:

1. Is this state meant to be a valid molecule, or merely an algorithmic noisy variable?
2. Does the transition preserve the sufficient information required by the reverse process?
3. Are graph and coordinates conditionally coupled at this stage?
4. Does a coarse step or branch skip a regime where a required variable can still change?
5. Does a decoder/repair step create validity that the stochastic process itself did not produce?

A valid research claim must match the level at which the constraint applies. Example: nonphysical Gaussian coordinate noise is not itself a reason to reject diffusion; using an OOD Cartesian displacement as evidence about real molecular motion is a reason to require an additional admissibility gate.

## 7. Reaction / edit contract

For graph-edit or reaction-generation algorithms, distinguish:

- arbitrary graph edit;
- chemically valid product transformation;
- plausible reaction under a specified condition;
- mechanistically/kinetically plausible pathway.

These are increasingly strong claims. Do not require the strongest level unless the paper claims it; do not infer a stronger level from a weaker validator.

## 8. Dead-node forecast template

For each candidate method, fill no more than three rows before the expensive experiment:

| Algorithmic claim | Molecular constraint that could break it | Status | Cheapest discriminating test | If failed |
|---|---|---|---|---|
| ... | ... | KNOWN / PREDICTED / OBSERVED | ... | correct intervention / kill mechanism / narrow claim |

Rules:

- **PREDICTED is not OBSERVED.** Keep the current research route alive until the test returns evidence.
- Prefer an upstream object-validity test over a late endpoint failure if it can falsify the same claim more cheaply.
- If the object constraint is violated but the experiment was explicitly an OOD model probe, do not convert that violation into a chemistry claim.
- If fixing the molecular validity also removes the algorithmic effect, that is evidence the original mechanism was an artifact.

## 9. Practical evidence hierarchy

From weakest to strongest:

1. abstract plausibility;
2. toolkit rule / known molecular constraint;
3. object-level diagnostic on current states;
4. intervention with matched controls;
5. endpoint survival under the real pipeline;
6. independent seed/system confirmation;
7. cross-dataset/checkpoint/model-family generalization.

Do not jump from 1-2 to a route switch, or from 3 to a method claim.

## Reference anchors

- RDKit Book: molecular sanitization includes valence checking, kekulization/aromaticity, radicals, hybridization and chirality cleanup; use it as a concrete example of graph-level semantic validation, not a universal chemistry oracle.
- IUPAC Gold Book: conformation distinguishes spatial arrangements interconvertible primarily by rotations about formally single bonds; this is useful when separating conformational diversity from chemical-identity diversity.
- wwPDB validation: standard macromolecular geometry, chirality/planarity, close contacts, Ramachandran and rotamer checks provide a concrete object-level validation decomposition.
- EGNN / E(n)-equivariant model literature: translations, rotations, reflections and permutations are explicit symmetry choices; verify their compatibility with the task's stereochemical semantics.
