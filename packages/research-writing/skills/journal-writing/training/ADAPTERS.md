# Journal-writing v1 — stable claim-type adapters

These adapters are proof-obligation sets, not section templates. Always apply S1/S2 from `../SKILL.md` first, then route by central claim object and evidence regime.

## Router

| Adapter | Route here when the central paper claim is... | Do not route here when... |
|---|---|---|
| A1 Resource | a reusable dataset/model/reference/biobank/atlas/derived resource | the main claim is a predictive/generative method rather than reuse of the resource itself |
| A2 Generalist method | one primary task generalized across heterogeneous domains/distributions | one platform spans materially different object/task classes (use A3) |
| A3 Unified computational platform | one shared core spans multiple object classes, interaction types, tasks or output modalities | breadth is only dataset/domain shift within one task (use A2) |
| A4 Engineered system | an intentionally modified system reaches a new operating state/capability | the paper mainly identifies a natural causal mechanism (use A5) |
| A5 Molecular causal mechanism | a causal molecular/cellular edge is discovered and mechanistically closed | 'mechanism' is purely descriptive/statistical/historical without meaningful causal intervention |
| A6 Clinical intervention | a human intervention is evaluated under a clinical study/trial evidence regime | the paper is preclinical or primarily mechanistic without a clinical intervention claim |

Hybrid papers may use more than one adapter. Choose one dominant central claim object, then import only the secondary proof modules required by the actual evidence graph.

---

## A1 — Resource

Stable core:
`artifact stack -> scope/coverage -> validity per reusable layer -> interoperability/reproducibility where relevant -> downstream reuse utility -> accessibility/handoff`

Rules:
- Enumerate reusable layers explicitly (for example source asset -> derived representation -> downstream analysis object).
- A derived layer does not inherit trust automatically from its source layer.
- Use subtype-specific validity modules:
  - living derived model: source fidelity, temporal/passaging stability, phenotype/genotype preservation, cross-context validation;
  - atlas/reference: annotation/identity validity, method concordance, coverage/completeness;
  - graph/derived reference: source accuracy, representation precision/recall, downstream analytical fidelity.
- Accessibility is part of the product claim when reuse is central.

---

## A2 — Generalist method

Stable core:
`generalization axis/contract -> breadth-enabling basis -> held-out domain evidence -> appropriate specialist/generalist comparison -> adaptation behavior -> workflow utility if claimed -> failure surface`

Rules:
- Define what counts as a new domain before evaluating generalization.
- Test meaningful held-out domains, not only random samples from the same acquisition family.
- Stratify performance along the claimed generalization axis when aggregate averages could hide failure.
- Characterize adaptation: zero-shot, prompting, few-shot, fine-tuning, retraining cost/data/compute.
- A generalist need not beat every specialist everywhere; expose the trade-off.

---

## A3 — Unified computational platform

Stable core:
`scope-unification contract -> shared core/representation -> stratified cross-category validation -> output-appropriate trust boundary -> operating/failure surface`

Rules:
- Name the heterogeneous object/task classes being unified.
- Establish that the breadth comes from a shared core rather than hidden task-specific systems.
- Validate materially different categories separately enough to expose weak regions.
- Choose trust evidence by output type:
  - prediction: external/temporal benchmarks, confidence/error calibration;
  - generation/design: prospective physical/functional validation;
  - operational platform: scaling, reliability, end-to-end success.
- Calibration, wet-lab validation, scaling/cost analysis and downstream application are modules, not universal requirements.

---

## A4 — Engineered system

Stable core:
`target-state contract -> intervention identity/integrity -> direct state-realization proof -> attribution/provenance proportional to claim -> performance in claimed environment -> operating boundary/trade-offs`

Rules:
- Define the target operating state against a baseline in observable terms.
- Prove the intervention exists in the operating system (assembly, expression/localization, rewiring, installed pathway/module, etc.).
- Demonstrate the whole target state, not merely component activity or proxies.
- Rule out alternative routes in proportion to the causal claim (isotope tracing, mass balance, controls, perturbation/rescue, dynamics, etc.).
- Validate where the paper claims the system matters; lab success does not authorize deployment/field claims.
- Bottleneck-repair loops, adaptive evolution and optimization history are optional development modules.

---

## A5 — Molecular causal mechanism

Stable scope: causal molecular/cellular mechanism papers.

Stable core:
`unresolved causal edge -> mediator identification/provenance -> requirement/loss-of-function -> positive causal closure -> direct biochemical/physical edge when claimed -> mechanism decomposition -> specificity/boundary`

Rules:
- Discovery route can be candidate-driven, unbiased genetics, biochemical purification, proteomics or another route.
- Requirement alone is not direct mechanism.
- Positive causal closure can be gain-of-function, rescue, purified reconstitution, activated fragment/domain or another fit-for-purpose intervention.
- If the paper says X directly does Y, show the relevant direct biochemical/physical/state edge.
- Decompose only as far as required by the central mechanism claim.

---

## A6 — Clinical intervention

Stable core:
`design-authorized claim space -> population/intervention integrity -> prespecified primary inferential hierarchy -> biological/target-engagement layer -> secondary evidence without hierarchy inversion -> safety/harm contract -> confirmatory vs exploratory separation -> design/duration-calibrated conclusion`

Rules:
- Encode phase, population, intervention, comparator, randomization/blinding, prespecified endpoints, analysis population and follow-up before building narrative.
- Preserve primary endpoint priority even when secondary outcomes are more favorable.
- Target-engagement/biomarker evidence does not automatically establish clinical efficacy.
- Keep subgroup, moderator, per-protocol/compliance-adjusted and post-hoc analyses visibly distinct from confirmatory evidence.
- Safety language must follow the study's operational/adjudication contract and expose material imbalances.
- Route evidence-regime modules separately:
  - early phase/single arm: feasibility -> safety -> delivery -> biological activity -> calibrated association;
  - randomized confirmatory: allocation/disposition -> primary endpoint -> key secondary -> safety -> robustness -> calibrated interpretation;
  - pragmatic/implementation-sensitive: add workforce/site generalizability, adherence/completion, routine-care relevance and implementation questions when central.

---

## Adapter invariant

Adapters answer **what must be proven**, not **what headings to use**.

Visible section order, paragraph boundaries, figure allocation, abstract compression, title and Discussion language remain controlled by S1–S8.