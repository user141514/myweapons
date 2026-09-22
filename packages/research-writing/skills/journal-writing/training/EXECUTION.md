# Asset-to-prose execution model — candidate v0.2

Status: **stable execution v1**
Derived from asset-blind Rounds 030–044, then validated on two unseen post-distillation holdouts (Rounds 046–047).
Detailed failure-derived observations are preserved in `EXECUTION_OBSERVATIONS.md`.

This layer sits below journal structural rules S1–S8 and adapters A1–A6.

- S1–S8 / adapters answer: **what must be proven and how the paper is globally organized**.
- This execution model answers: **given author assets, which facts become Results prose, in what local order, at what claim strength and density**.

The detailed E-rules are training evidence, not the runtime interface. Runtime writing should use the invariants below.

---

## X0 — Blind-test integrity

For training, physically separate the asset channel from the prose channel.

Before a blind draft is locked, permit only:
- figure/table images and captions;
- Extended/Supplementary assets;
- source/raw data;
- experiment inventory and denominators;
- minimal method metadata required to interpret an asset;
- explicit author design rationale when supplied as an asset.

Do not expose:
- the target title when Title is part of the blind evaluation;
- Abstract;
- Main/Results/Discussion prose;
- article summaries;
- search snippets;
- section headings when running a strict blind prose test.

For an independently constructed literature-state graph, freeze retrieval to publications available before the target paper and explicitly exclude the target PMID/DOI/PMCID. If the target record appears and leaks its title or prose, abort the blind target.

If prose leaks, abort that target rather than pretending it remained blind.

For target Supplementary files, use an isolated asset-extractor worker when title/prose leakage is otherwise unavoidable. The worker may inspect the file but must return only sanitized evidence assets (experiment, control, direction, value, denominator, branch); it must not return title, Abstract/Main/Results/Discussion prose, or author section headings.

X0 governs **training validity**, not manuscript prose.

---

## X1 — Evidence authorization contract

Before drafting, build a **claim-centric author-asset manifest** rather than a figure list.

For each local claim/state transition, record:

`scope -> observation -> comparator/control -> direction -> quantitative anchor -> claim authorized -> alternative closed -> next decision enabled`

The manifest may need:
- main figures;
- Extended/Supplementary figures and tables;
- raw/source data;
- unplotted experimental outcomes;
- cohort/sample denominators;
- negative and null groups;
- baseline/pre-intervention state;
- design/search funnel counts;
- experiment rationale and rejected alternatives;
- method-state facts that define what was actually tested.

For **end-to-end manuscript generation**, the author-asset manifest has two coordinated layers:

1. **evidence graph** — experiments, observations, controls, denominators, source data and causal boundaries;
2. **literature-state graph** — established mechanisms, competing models, unresolved controversies, adjacent exemplars and the references that authorize the prerequisite/background state.

Results can often be reconstructed from the evidence graph alone. Introduction and Discussion cannot be fairly evaluated if the literature-state graph is absent.

### Hard authorization rules

1. **No decisive sign, no draft.**
   If the local state transition depends on direction, ordering, magnitude or responder identity and the asset package does not authorize it, acquire the missing asset or narrow the claim.

2. **Preserve scope exactly.**
   Whole tissue ≠ purified organelle; bulk ≠ subtype; in vitro ≠ in vivo; computational pass ≠ experimental success; histology ≠ metabolite state.

3. **Do not invent missing author assets.**
   If a fact existed only in published prose and was absent from the supplied asset package, failure to reconstruct it is an asset-contract failure, not automatically a writing failure.

4. **Baseline equivalence is evidence.**
   When groups could differ before intervention, balancing/stratification belongs in the manifest because it authorizes later causal comparison.

---

## X2 — Local decision graph

Write Results from **decision transitions**, not from figure order or assay order.

Canonical local transition:

`licensed state -> active unknown / alternative -> discriminating action -> observation -> updated state`

### Paragraph unit

One paragraph should normally close **one decision debt**.

A paragraph may combine many assays when they triangulate the same proposition:
- necessity;
- sufficiency;
- time course;
- orthogonal validation;
- negative control.

Start a new paragraph when:
- the next experiment consumes the new state as an input;
- the active unknown changes;
- the design operation changes;
- a new independently falsifiable boundary opens.

### Sentence unit

A sentence should normally complete **one inferential move**.

High information density means:
- multiple facts converge on one update;

not:
- observation + mechanism + design choice + significance are packed into one sentence.

### Reader state

Do not re-explain context already licensed by the immediately preceding Results state unless the value itself is part of the new transition.

---

## X3 — Trust and causal localization

A result is usable only after the premise it depends on has earned enough trust.

Ask for each local claim:

1. **What does the assay actually measure?**
2. **What alternative explanations remain?**
3. **What evidence localizes the causal layer?**
4. **What level of causal wording is authorized?**

### Measurement models

For a trap, reporter, proxy, sensor or surrogate track:

`native state -> measurement intervention -> observed state`

Validate the minimum positive/negative/specificity controls needed to interpret the signal.

Do not equate:
- a trapped conformation with an unperturbed native state;
- proximity with collision;
- a reporter signal with a biological state;
unless the controls authorize that mapping.

### Causal levels

Keep distinct:
- association;
- requirement / loss-of-function;
- positive causal closure / rescue / gain-of-function;
- direct biochemical/physical edge;
- downstream phenotype causality.

Target binding + exposure does not prove that a behavioural phenotype is target-mediated; effect-level blockade/rescue/genetic dependence is needed for that upgrade.

### Localization controls

Negative results deserve prose space when they place the defect at the correct layer, for example:
- RNA-processing defect with normal global transcription;
- target phenotype with normal global translation;
- downstream signalling failure despite intact upstream signal.

Also distinguish:
- candidate-family specificity;
- whole-system integrity.

They close different alternatives.

---

## X4 — Decision-value compression

Results prose should contain the **smallest evidence subset that changes reader state**.

Prioritize assets that provide one or more of:

1. **identity** — named examples that make a broad pattern auditable;
2. **scale** — one quantitative anchor that defines the physical state;
3. **reliability** — funnel denominator/pass rate rather than survivor examples;
4. **causal discrimination** — control, negative result, rescue, blockade;
5. **competitive position** — difference versus a strong benchmark;
6. **cross-layer linkage** — exposure/Kd, occupancy/EC50, dose/threshold;
7. **boundary** — where the effect stops, weakens or changes;
8. **surprise** — an explicit expected failure mode that the result defeats.

### Quantitative selection

Prefer **quantitative salience**, not exhaustiveness.

A number deserves prose space when it changes:
- effect scale;
- success/failure decision;
- baseline or state-of-the-art comparison;
- operating boundary;
- representativeness;
- temporal interpretation.

One state-defining value often beats five descriptive values.

### Design/search claims

For engineering/screening/design methods, preserve the funnel:

`generated -> filtered -> experimentally tested -> physically/functionally validated -> selected`

Keep computational, experimental and functional gates semantically distinct.

---

## X5 — Preserve asymmetry and residual structure

Do not average away scientific structure.

Track separately when decision-relevant:
- receptor/pathway components with different causal weights;
- systemic versus mucosal outputs;
- acute versus durable effects;
- molecular kinetics versus cellular state versus phenotype;
- treatment components with different localization/half-lives;
- whole-tissue versus subtype responses;
- histological versus biochemical versus functional layers.

### Partial explanation

`most rescued` is not `mechanism complete`.

Retain residuals when they are structured:
- one molecular subclass remains unexplained;
- one output persists while another disappears;
- one time point differs;
- one subgroup resists rescue.

A structured exception is prose-worthy when it predicts the next unknown.

### Near-threshold results

Do not convert:
- trend -> positive result;
- non-significant -> definitive no-effect.

Keep the boundary exactly as the evidence supports it.

### Claim-level words

Do not promote:
- local success -> platform;
- one target -> general method;
- association -> mechanism;
- laboratory result -> field/deployment claim.

Reuse/generalization language requires reuse/generalization evidence.

---

## X6 — Decision rationale is part of the scientific state

Author assets must include **why this experiment/design choice was made** when that rationale is necessary to understand the next action.

Decision rationale can include:
- why this target was selected;
- why a competing component was rejected;
- why this tissue/delivery route/model was chosen;
- what known constraint the design addresses;
- what failure mode the next experiment tests;
- why one search space or optimization objective is appropriate.

Method facts belong in Results when removing them would make the scientific decision uninterpretable.

Reproduction-only implementation detail remains in Methods.

### Diagnostic order

When a negative result eliminates one route and determines the next candidate, preserve that search order if removing it would turn discovery into a misleading retrospective textbook story.

---

## X7 — Results realization

### Claim language

Use the strongest statement authorized by X1–X6.

Avoid unsupported evaluative adjectives:
- robust;
- dramatic;
- substantial;
- meaningful;
- modest;

unless a threshold, benchmark or domain convention authorizes them.

Prefer the actual comparison or number.

### Unsupported outputs

Do not write meta-prose such as:
- “the direction cannot be inferred”;
- “this value was not available”.

If an output is decision-relevant and unavailable: stop and acquire it.
If it is not decision-relevant: omit it silently.

### Ending

Stop when the final local Results state is closed.

A concise synthesis is appropriate if it names exactly the newly closed state.
Broader significance, future promise and field-level extrapolation belong in Discussion.

---

# Draft gate

A blind Results draft may begin only if:

1. the local claim/state transition is explicit;
2. decisive sign/value/responder identity is authorized;
3. scope tags are compatible;
4. baseline equivalence is known when required;
5. model-changing controls/negative results are present;
6. measurement/proxy interpretation is calibrated when required;
7. decision rationale is available when required;
8. paragraph-level decision debts are enumerated;
9. one minimal set of quantitative/identity-bearing anchors has been selected;
10. structured residuals/boundaries are marked rather than averaged away.

If a required item is missing, do not draft the claim.

---

# Reveal evaluation order

After the blind draft is locked, reveal published prose and compare in this order:

1. factual integrity;
2. scope integrity;
3. evidence/alternative closure;
4. causal level and claim calibration;
5. decision-graph / paragraph boundaries;
6. quantitative and comparator selection;
7. residual/boundary retention;
8. sentence information density;
9. lexical/style realization.

Do not optimize wording similarity before 1–7 are acceptable.

---

# Compression map

The detailed observations E0–E43 remain archived in `EXECUTION_OBSERVATIONS.md`.

Runtime mapping:
- asset sufficiency / sign / source / baseline / scope -> **X1**
- local experiment order / paragraph and sentence boundaries -> **X2**
- controls / proxies / necessity-sufficiency / causal layer -> **X3**
- numbers / funnels / comparators / identity examples -> **X4**
- divergent axes / exceptions / partial rescue / overclaim -> **X5**
- experiment rationale / rejected alternatives / design logic -> **X6**
- prose strength / stopping rule / no meta-writing -> **X7**
- strict blind isolation -> **X0**

No new execution invariant should be added unless an unseen holdout produces a failure that cannot be generated from X0–X7.
