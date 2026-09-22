---
name: top-conference-paper-writing
description: Use for drafting, restructuring, compressing, or reviewing short-form top-conference research papers (ML/AI/CV/scientific-ML conference style) where the main text must be dense, selective, evidence-driven, and supported by a deeper supplementary/reproducibility substrate. Do NOT use this skill as the default for Nature/Science/Nature-family/Cell-family or other long-form journal/subjournal writing; those require a separately trained journal-writing skill.
---

# Top-Conference Paper Writing

## Scope

This skill is the learned conference track.

It applies when the main-text communication budget is tight and the paper must compress a large research asset base into:
- one strongest operational organizer, unless a topology check proves that multiple co-primary scientific objects have independent paper-level ownership;
- a few co-primary contributions or, when required, a bounded co-primary ownership graph with explicit coupling relations;
- a small number of decisive evidence roles;
- compact figures/tables;
- a separate supplement/reproducibility substrate.

This skill does not define how major journal/subjournal papers should be written.

## 1. Upstream organizer

Before prose, build exactly three abstraction levels:
1. Problem-level — what scientific/task reformulation owns the paper?
2. Method-level — what intervention family realizes it?
3. Implementation/decision-level — what operator/module/solver/decoder/etc. implements the method?

Rank organizers by explanatory ownership:
- problem ownership;
- method coverage;
- comparator ownership;
- evidence ownership;
- effect ownership;
- claim ownership;
- boundary ownership.

Prefer the most upstream object that owns the largest fraction of the paper **without becoming a generic retrospective umbrella**.

A valid organizer must be **paper-native and evidence-addressable**:
- it should contain the stable scientific nouns that identify the paper's task/method family;
- a headline result should be stateable as “this organizer did X against Y on Z” without translating it back into a lower-level named method;
- it should predict distinctive comparator/evidence objects, not merely classify sections after the fact.

Section-prediction coverage is necessary but not sufficient. A phrase such as “capacity–compute–generalization co-design” can cover an entire paper tautologically while owning neither its title, nearest comparator, nor headline result.
Do not automatically promote the cleanest equation, newest module, largest ablation gain, or easiest component to name.
A correct paper may have one top organizer plus several co-primary contributions beneath it.

### Single-organizer falsification check

Do not assume that paper-level ownership must form a tree with exactly one scientific object as the parent.

After identifying the strongest operational organizer, test every other paper-owned candidate that could be co-primary. **First decompose the organizer into a paper/system-level identity plus candidate method branches. Do not define the organizer by pre-composing the very branches whose independence is being tested.** Each candidate branch must be evaluated outside the organizer definition; only after failing the independence test may it be folded back into the organizer's subordinate tree.

Switch from a single-organizer tree to a bounded co-primary ownership graph only when at least one additional proposed scientific object independently owns all of the following in a way **not entailed by the paper/system-level organizer**:
- a distinct method/scientific responsibility;
- a non-redundant evidence family or decisive result;
- independent visual/explanatory responsibility in the main paper;
- an independent **paper-level** consequence (`C_paper`).

Track within-organizer design-selection consequences separately as `C_design`. A branch can own a real comparator, resource tradeoff, or downstream choice among variants without thereby becoming a second paper-level scientific object.

When this condition holds, retain the strongest operational organizer inside the domain it genuinely owns, but represent the full paper through co-primary objects plus explicit coupling edges. A project/program frame may describe that relation, but it does **not** become a validated scientific object merely because the title, abstract, or authors use broad rhetoric.

Do **not** trigger a co-primary graph merely because:
- the paper has several modules or sections;
- a dataset is large;
- several ablations are strong;
- the abstract enumerates task/model/data;
- benchmark breadth is wide;
- a capability label such as general-purpose or foundation-model is rhetorically prominent.

If removing the candidate would only narrow implementation detail, evidence breadth, or one scoped mechanism sentence while leaving the organizer's paper identity intact, keep the candidate subordinate. If removing it forces a distinct paper-level contribution, evidence branch, visual responsibility, or release consequence to disappear, the single-organizer topology is falsified.

**Anti-absorption rule:** an organizer does not prove a branch subordinate merely because the organizer phrase already names that branch's mechanism. Before topology adjudication, rewrite the organizer to the narrowest paper/system identity that still owns the shared task/interface. Then test matching, decoding, data, architecture, objective, inference, or other method branches independently. A compound phrase such as “X with A and B” may be a faithful executable summary while still being an invalid topology test if A or B is exactly the candidate under review.

**Operational-M gate:** before any candidate can receive `M=PASS`, require it to define an independent scientific operation. Qualifying ownership anchors include an intervention/transformation, objective, state or representation definition, interface/decision rule, data-generation or collection mechanism, algorithmic procedure, or another experimentally manipulated scientific variable whose manipulation constitutes the candidate method itself. **A borrowed application framework does not force `M=FAIL`: if the paper specifies a distinct task-facing integration, adaptation, inference, or fine-tuning procedure and deleting that procedure removes a paper-owned method responsibility, the application branch may receive `M=PASS`.** Record `APPLICATION_METHOD` as an optional subtype for clarity, but do not use the subtype to veto co-primary promotion when the same candidate independently passes `M+E+V+C`. Merely varying **scale, depth, model size, dataset size, population, task breadth, stress regime, evaluation range, or other operating regime** is `M=FAIL` unless that variation is itself the paper's proposed scientific intervention. Evidence volume, visual prominence, model-family naming, or consequence breadth cannot manufacture `M`.

**Ownership-strength precedence:** for every candidate outside the normalized organizer, decide `M / E / V / C_design / C_paper` by counterfactual deletion before scoring evidence quality or causal strength:
- `M`: after passing the Operational-M gate, would deleting the candidate remove a distinct scientific/method responsibility?
- `E`: would deleting its evidence family force a distinct scientific sentence to disappear or materially narrow?
- `V`: would deleting its visual/explanatory object remove an independent main-paper responsibility rather than merely make one shared method harder to read?
- `C_design`: would deleting the candidate remove a dedicated choice among variants of the same normalized organizer, including its comparator, resource tradeoff, or rationale for selecting the retained variant?
- `C_paper`: would deleting the candidate remove an independent task, release, objective, comparator program, retained scientific object, or headline/closing scientific consequence **beyond** within-organizer variant selection?

A downstream decision to use one branch for later experiments is `C_design` unless the selected branch itself remains an independently claimed scientific object or changes a paper-level task, objective, release, comparator program, or headline conclusion.

Record ownership independently from confidence. Weak or qualitative evidence may still yield `E=PASS` when it is the only evidence family supporting a distinct claim, while receiving a low evidence-strength label. A distinct paper-level consequence may still yield `C_paper=PASS` even when its empirical support is weak. Conversely, one section, equation, figure, dataset, qualitative example, or design-selection decision never creates co-primary topology by itself: promotion still requires the same candidate to pass `M+E+V+C_paper`. `C_design` is reported as real ownership but is insufficient for co-primary promotion. Only **after** ownership is fixed should causal/evidence strength be labeled.

**Shared-evidence / shared-visual non-duplication:** participation in one package comparison or one shared figure does not grant independent `E` or `V` ownership to every nested mechanism shown inside it. A candidate receives independent `E=PASS` only when deleting that candidate removes a distinct scientific sentence or non-redundant evidence obligation. It receives independent `V=PASS` only when deleting that candidate removes a distinct explanatory object or main-paper visual responsibility, rather than merely deleting one label, path, or subpart of a shared schematic. Shared evidence/visuals may support several branches, but do not double-count them as independent topology evidence.

### Upstream-rival stress test

Before freezing the organizer, construct the **strongest more-upstream rival** that could plausibly own the paper. Candidate rivals may come from:
- task/problem reformulation;
- generated state or representation choice;
- probabilistic object/process;
- objective or training principle;
- interface/capability definition;
- cross-field program transfer.

Compare the chosen organizer and its rival by explanatory ownership, not by source-file prevalence, implementation elegance, or ablation magnitude. Ask which candidate naturally owns the title/task, nearest comparators, method family, decisive evidence, main boundary, and closing claim.

If a lower-level mechanism wins only because it is easy to point to in code, appears in many files, or has the largest component ablation, keep it subordinate. Conversely, do not replace an evidence-addressable method organizer with a generic upstream umbrella that cannot itself own a headline result.

When reveal shows that the chosen organizer is one level too low, count **dependency structure rather than the number of sections touched**: one upstream organizer rerank may propagate through title, abstract, introduction, figures, and discussion without constituting a different scientific paper identity.

After freezing the operational organizer and running the topology falsification check, run a **second ranking pass** over co-primary candidates. Promote a candidate to co-primary when it owns:
- a distinct scientific sentence;
- a non-redundant evidence object or ablation;
- a `C_paper` consequence not already explained by the organizer alone.

A `C_design` consequence may still deserve a named subordinate contribution, method subsection, dedicated visual, or design decision, but it does not by itself create a second paper-level node.

Subordinate-to-organizer does not mean minor. Conversely, several modules do not become co-primary merely because each has an implementation section or table.

## 2. Comparator axes

A paper-level abstraction is incomplete until it is located relative to strong alternatives.
Ask what prior family is the real comparator and on what shared axes the method changes the problem.
Examples: complexity, sequential depth, path length, information ownership, optimization accessibility, representation state, objective, sampling budget, physical validation layer.

A strong Method often contains:
scientific object + strongest alternative + shared comparator axes + falsifiable consequence.

## 3. Abstract

Default 180–220-word budget:
- Problem / contradiction: 15–20%
- Organizer / method delta: 25–30%
- Strongest results/evidence: 30–35%
- Breadth / consequence: 15–20%
- Boundary: one compact clause/sentence

Avoid spending abstract budget on source provenance, training-file detail, full reproducibility caveats, implementation plumbing, or reviewer-style defensive qualifications.
The abstract should not read like a mini-Methods appendix.

**Evidence identity before mechanism completeness:** once the method object is named, spend abstract budget first on *what was demonstrated*—task/regime, breadth, strongest result class, transfer/application consequence—before explaining secondary mechanism details.

This is a **selection rule, not an enumeration rule**. Choose the smallest evidence set that makes breadth and consequence legible. One memorable anchor result/comparator is often more useful than listing every evidence branch. Exact numbers are optional; evidence identity is not.

An explicit boundary sentence is conditional, not mandatory. If calibrated verbs, named regimes, and concrete comparators already bound the claim, do not spend abstract budget restating a generic limitation.

## 4. Introduction

Use:
field pattern / contradiction
-> upstream organizer
-> co-primary contributions
-> comparator axes
-> evidence preview
-> compact boundary.

Two organizer tests:
1. Upstream ownership — does the framing explain why the problem exists and why the method family is coherent?
2. Section-prediction coverage — does the framing naturally predict every major later contribution/section?

If half the paper feels unrelated to the opening organizer, the framing is too narrow.

Section-prediction coverage should forecast **distinctive evidence families and comparator classes**, not manufacture an exhaustive row-by-row experiment plan. Exact tasks or controls that are not visible in the allowed assets remain source/evidence gaps rather than obligations to hallucinate an ideal paper.

Before committing to an in-domain bottleneck narrative, test a second possibility: **cross-field program transfer**. Some papers are best framed as bringing a successful research program from another field into a new domain, then explaining what historical missing variable (scale, representation, data, compute, interface) previously prevented that transfer.

Treat this as an **internal falsification check by default**, not a mandatory visible two-track narrative. Surface the cross-field frame only when it wins, changes the organizer, or identifies the historical missing variable more sharply than the in-domain story.

## 5. Related Work

Do not organize Related Work by citation chronology or broad conceptual resemblance alone.

First recover the field-native historical/comparator structure, then build a role ledger:
- `DIRECT_COMPARATOR` — solves substantially the same task/object with a competing mechanism;
- `ENABLING_SUBSTRATE` — provides the component/representation paradigm but is not the closest task comparator;
- `ADJACENT_ANALOGUE` — shares a mechanism/interface in a neighboring setting;
- `EVIDENCE_CONTEXT` — defines the regime under which the paper's claim matters (for example, scale/pretraining/data regime);
- `BACKGROUND_ONLY` — useful context but not part of the novelty boundary.

After constructing families, run a **nearest-comparator pass indexed by claim axis**. “Nearest” does not always mean most mechanistically similar.

For each load-bearing claim ask separately:
- who competes on the same task/evidence axis?
- who is closest on architecture/mechanism?
- who is closest on data/compute regime?
- who is closest on a component-level intervention?

A methodologically distant system may be the publication-level nearest comparator when it is the strongest competitor on the headline benchmark. Conversely, a mechanistically similar prior may be only lineage or component precedent. Broadly correct families do not compensate for missing the closest comparator on the claim's actual evidence axis.

Do not infer argumentative membership from the bibliography alone. A citation belongs to the novelty-space story only if it changes one of:
- comparator family;
- enabling dependency;
- adjacent mechanism boundary;
- evidence regime;
- novelty scope.

Field-native organization may be spectral/spatial, CNN/attention, regression/generative, search/inference, etc. It may also be a **causal historical bottleneck chain** such as data scale -> usable model capacity -> compute feasibility -> regularization. Do not force every field into named method families, and do not overwrite the native history with a taxonomy invented only from source-code similarity.

The claim-indexed nearest-comparator pass is an audit layered on top of field-native organization, not a replacement taxonomy. The same prior may legitimately be nearest on several claim axes, and a central claim axis (for example bidirectionality) need not become its own Related Work family. Use the axes to calibrate novelty and comparator proximity; use the field-native history to decide prose structure.

## 6. Method

Before writing, build an Artifact Visibility Map.
Mark each scientific object visible / partially visible / not visible.

Do not invent private training labels, data mixture, curriculum, checkpoint selection, or internal experiments.
Use SOURCE_VISIBILITY_GAP when necessary information was unavailable.
Use MISSING_ABSTRACTION only when the relevant evidence was visible but not elevated.

For each visible intervention build:
problem/failure -> controlled scientific quantity -> operation -> falsifiable consequence -> strongest cheap alternative -> role.

Main-text Method should describe scientific objects and interfaces, not source-file coverage.

## 7. Equations

Include equations when they compress scientific structure.
Good equations define state, reference, responsibility, transition, information relation, decision rule, or controlled trade-off.
They should predict behavior, an ablation, an experiment, or a boundary.
Weak equations merely translate helper functions or tensor operations.

## 8. Experiments / Results

Organize evidence as:
claim -> strongest plausible alternative that would materially narrow/reverse it -> discriminating contrast -> result -> supported sentence -> boundary.

Classify evidence as:
- CLAIM_CHANGING
- FUNNEL
- AUDIT_SUPPORT

### Comparative quantifier contract

Before writing a load-bearing comparative or universal sentence, resolve its full semantic scope:

`population × processing protocol × aggregation × metric set × comparator universe × favorable direction × exceptions`

Words such as **all**, **best**, **across**, **consistently**, or an unqualified comparative are valid only when every result cell semantically entailed by that sentence satisfies the claimed direction. Do not let a true statement about means silently expand to medians, one processing pipeline expand to another, or one comparator subset expand to the full benchmark.

If one cell is an exception, either state the exception or narrow the sentence so it no longer entails that cell. Repeating the same aggregate claim in Abstract, Results, figures, and Compression does not validate it; cross-section consistency can propagate the same factual error.

Build two maps:
Scientific contrast map: performance comparison, mechanism ablation, orthogonal validation, physical/function experiment, counterfactual, experimental structure.
Reproducibility/reporting map: split manifest, hash/container, denominator ledger, exact command, full failure log, artifact receipt.

Reporting infrastructure supports scientific evidence by default.
It becomes main science only when the claim itself concerns reproducibility, leakage-free generalization, calibrated success rate, or deployment reliability.

## 9. Minimal evidence bundle

For a narrow claim, seek minimal decisive evidence.
For a multi-claim paper, seek the minimal non-redundant evidence bundle.

An item belongs only if:
1. deleting it forces a scientific sentence to narrow;
2. no remaining item supports the same sentence;
3. it attacks a distinct strong alternative;
4. it is not merely reporting infrastructure.

Do not equate experiment count with evidence-layer count.

## 10. Task breadth vs evidence independence

Task breadth counts distinct scientific target/decision families.
Evidence independence depends on contrast, data/provenance, target object, adaptation regime, and dominant failure mode.
Multiple metrics, seeds, notebooks, or similar datasets do not automatically create independent evidence.

## 11. Reproducibility

Track separately:
- training reproducibility;
- inference reproducibility;
- benchmark/result reproducibility;
- fixed-output auditability;
- physical/biological validation reproducibility.

Scientific credibility and artifact reproducibility are related but non-identical.
A bounded claim may remain credible despite missing training assets if independent evidence supports that exact claim.
This does not justify stronger causal statements about the missing training process.

## 12. Denominators

Expose denominators in the main paper only when changing the denominator changes the scientific meaning.
Move exhaustive attempt logs to supplement/reproducibility assets unless they are themselves part of the scientific claim.

## 13. Negative boundaries

Use negative results to identify the exact limit of the method.
Do not turn them into generic audit disclaimers.

## 14. Discussion / Conclusion

After building an evidence-calibrated Discussion, run a **closing-section rerank**:
1. restore the upstream organizer;
2. compress result branches into capabilities rather than replaying tables;
3. pay the main qualification cost once;
4. retain one dominant future direction by default, derived from the most claim-changing unresolved mechanism. For platform/foundation papers, allow a **compact ranked portfolio of orthogonal directions** only when each direction extends a distinct paper-level claim axis (e.g. task scope, supervision regime, scale frontier) rather than listing validation chores or unresolved reviewer checks.

Do not write Discussion as `Results + reviewer caveat after every paragraph`.

A useful structure is:
organizer-level synthesis
-> 2–3 capability/consequence statements
-> one scope paragraph containing the main boundaries
-> one unresolved mechanism/question
-> final affirmative takeaway.

Move alternative-by-alternative audits to Limitations, supplement, or rebuttal unless they define the method's operating semantics.

Negative boundaries belong in the main Discussion when they distinguish what the method solves from what it does not solve. Detailed causal-identification gaps, extra matched controls, or benchmark bookkeeping usually do not need equal narrative weight.

Future work should not be a shopping list. Prefer the single unresolved mechanism or regime whose resolution would most change the paper's scientific interpretation. A short multi-direction ending is acceptable only when the paper itself establishes a platform with several non-redundant open axes, and deleting any direction would remove a distinct scientific consequence.

## 15. Figures and tables

Before allocating main-text visual slots, label every proposed evidence object:
- `OBSERVED_MAIN` — already exists and directly supports a headline/co-primary claim;
- `OBSERVED_SECONDARY` — already exists but mainly supports interpretation, robustness, or boundary;
- `UNRUN_IDEAL_AUDIT` — scientifically desirable control/analysis that was not actually run or is not part of the frozen evidence package.

Only observed evidence may occupy a frozen result figure/table plan. An `UNRUN_IDEAL_AUDIT` belongs in a future-experiment/reviewer-risk ledger unless the task is explicitly to design new experiments.

Use figures for spatial/structural organization, causal/process diagrams, trajectories, qualitative morphology, and conceptual distinctions.
Use tables when many discrete interventions share the same metrics or exact numerical comparison matters.
A concept figure is load-bearing if deleting it would make later equations/results difficult to interpret.
Do not overpack Fig. 1.

**Main-visual audit gate:** first rerank and freeze the corrected claim hierarchy. Only then give an audit/reproducibility visual object main-text space when removing the **visual object as a whole** would materially narrow the corrected scientific argument, or when it uniquely explains an enabling design decision that makes the organizer feasible.

Before freezing the visual bundle, classify every proposed evidence object as:
- `OBSERVED_MAIN` — result/contrast actually present and load-bearing;
- `OBSERVED_SECONDARY` — result actually present but refining/secondary;
- `UNRUN_IDEAL_AUDIT` — scientifically attractive control/factorial that has not been run.

`UNRUN_IDEAL_AUDIT` objects cannot occupy a frozen main-result figure/table slot. They may instead narrow causal wording, enter future work, or motivate the next experiment. Evidence-addressability alone is not evidence admission.

Do not let a provisional/overabstract organizer manufacture a matching audit figure that then appears load-bearing by circular reasoning.

A load-bearing visual may contain interpretive/support panels that do not independently change a claim if they reduce the reader's interpretation cost. Conversely, an audit can deserve main-text prose without deserving a main figure; prose admission and visual admission are separate decisions.

**Comparator/evidence-surface guard:** a comparator may own a bounded causal/result sentence and even `C_paper` comparator responsibility without earning a standalone visual slot. Before splitting a comparator from its parent table/figure, ask whether the frozen evidence actually gives it an independent figure/table/panel or independent explanatory object. A row inside one benchmark table remains part of that table's visual responsibility unless the reference/evidence package gives it a separate surface. Conversely, do not demote the method-defining figure/equation object merely because a cleaner causal contrast appears later. Freeze method identity and official evidence-surface granularity before reranking visual slots by causal cleanliness.

`OBSERVED_SECONDARY` is not synonymous with `SUPPLEMENT`. A secondary-looking diagnostic can remain main when it materially bounds the interpretation of a headline claim or reveals the character of the learned representation. Rank observed evidence by scientific ownership and boundary value before allocating space.

An enabling `FUNNEL` visual may be main-text when it explains why a chosen objective/interface unlocks organizer-level scale or feasibility, even if it is not itself the final benchmark result.

This gate does not apply when leakage, denominator validity, numerical correctness, safety, physical validity, or causal identification is constitutive of the headline claim.

## 16. Main text vs supplement

Allocate by **claim ownership, not artifact type**. Equations, ablations, protocol details, figures, and scaling studies have no fixed destination.

Main text owns problem, organizer, co-primary contributions, decisive evidence, capability, and boundary. Keep an object in main whenever removing it would make a contribution sentence, strongest-alternative rejection, estimand, or claim boundary unintelligible.

Supplement/repository owns full training/data details, extended ablations, denominator ledgers, environment, commands, robustness detail, secondary figures/tables, and failure logs only when a visible main-text anchor already preserves their scientific meaning.

Principle: thick substrate, thin surface.

### Claim-defining interface stays visible
If deleting an algorithm/protocol/interface would force the abstract or headline claim to change, keep its **minimal executable/understandable form** in the main paper. Move algebraic closure, coefficient expansion, extended proofs, exact tables, complexity detail, and implementation variants to the supplement.

A new coding/decoding/inference/evaluation capability cannot be supported by a main-text slogan plus a hidden supplemental protocol; the reader must see enough of the protocol to know what the capability means.

### Representative capability in main, coverage in supplement
For breadth claims, use an **anchor + coverage** pattern in main text: show one memorable representative result plus the visible population/signed pattern that establishes breadth. Do not make readers infer broad coverage from an abstract task list alone.

Keep one representative, rule-defined capability/sample/trajectory in the main paper. Use the supplement for:
- uncurated grids;
- more domains;
- nearest-neighbor or extended failure views;
- full trajectories;
- exhaustive variants.

### Claim-sensitive protocol choices remain visible
Even when the full evaluator or selection protocol is supplemental, expose in main text/table notes any choice that materially changes the estimand or scientific interpretation, such as:
- train vs test reference set;
- sample count;
- best-checkpoint selection;
- best-of-N/search budget;
- filtered vs raw denominator;
- transfer head/adaptation regime;
- resolution or positional adaptation;
- recipe exceptions used only for the headline result.

For architecture/transfer papers, also keep visible enough of the model-family definition and controlled comparison population to interpret scaling/efficiency curves. A data-size or model-scale interaction belongs in main when it reverses comparator ordering or resolves the paper's central contradiction, even if it looks like an ablation.

If a task-specific protocol choice materially shifts a headline result, keep the **dependence magnitude and evaluation status** visible in main text even when the exact realization/template/configuration remains supplemental.

### Negative metric boundaries are main-text science
If a method improves one axis while degrading another (e.g. quality vs likelihood/codelength), state the Pareto/boundary in the main paper. The supplement may carry exact decompositions and extended diagnostics.

### Supporting-expansion gate
A supplement may legitimately devote substantial space to a supporting object even when that object does not change the headline claim, if the expansion materially improves one or more of:
- coverage across cases/domains;
- transparency of sample/selection rules;
- phenomenon resolution or qualitative understanding;
- auditability / ability to inspect failure modes;
- robustness of a main-text interpretation.

This expanded support does **not** upgrade the scientific claim by volume alone. Claim strength remains owned by the main-text scientific contrasts and their denominators.

### Supplement thickness is not reproducibility thickness
Evaluate supplement burden by responsibility, not page count. Separate:
- proof burden;
- implementation burden;
- extra evidence burden;
- reproducibility-receipt burden.

A long supplement full of derivations and sample grids may still provide weak machine-level reproducibility.

## 17. Compression

Compress Results by scientific responsibility before deleting by text type:
1. freeze each distinct capability/claim;
2. retain its strongest discriminating contrast;
3. keep one memorable anchor plus the minimum coverage object needed for breadth;
4. preserve any protocol, denominator, selection, adaptation, or search dependence that would materially change the headline interpretation;
5. retain one exact negative boundary for the claim;
6. only then remove repeated metrics, secondary anchors, per-case narration, audit mechanics, framework plumbing, and low-ownership implementation texture.

A protocol detail is removable only if removing it does not change the estimand or meaning of the headline result. Exact realizations may descend while their interpretation-changing dependence magnitude stays visible.

Preserve organizer, comparator axes, decisive evidence, co-primary contributions, and bounded limitations. Do not compress multi-claim papers by collapsing non-entailing capabilities into one generic “transfer” or “performance” sentence.

## 18. Review / rebuttal

Rank reviewer questions by claim-changing power.
For each attack identify attacked claim, strongest alternative, existing evidence, missing evidence, and cheapest valid repair: wording / analysis / replay / new experiment / scope reduction.
Do not respond to every possible concern with a new experiment.

### Claim-index before repair type
Before deciding whether a reviewer found a missing estimand, map the requested quantity to the **actual submitted claim**.

Do not inspect explicit sentences only. Claim ownership can also be carried by the title, method name, abstract framing, figure labels, and whole-paper rhetoric. But implicit ownership must pass a counterfactual test:

1. Does the attacked sentence or paper-level naming actually own this estimand?
2. Is the reviewer requesting evidence for the submitted package/interface claim, or for a stronger component-causal/generalization claim?
3. If the requested component effect were zero, would the paper's title/category/core contribution sentence have to change?
4. Would the paper's central category collapse if the quantity remained unmeasured?

A reviewer-requested quantity is a true missing estimand only when the submitted claim depends on it. A method name can identify an integrated package without claiming every component has an independent positive marginal effect. A cheap component factorial is not automatically decision-sensitive.

### Evidence receipt before revision plan
When the reviewer asks for a fact already present in the supplement, code, logs, or records, put the decisive **number/equation/contract first**, then point to the source. Search receipts across prose, equations, tables, captions, plot axes, curve endpoints, and protocol semantics—not only scalar tables. Do not answer an existing-evidence question with “see Figure X” or a vague promise to clarify/rerun.

Receipt presence is not the same as rhetorical visibility. If a fact was technically present but the reviewer reasonably missed it, reject the factual premise with the exact receipt while still accepting the placement/clarity repair.

Search beyond scalar tables: a decisive receipt may live in a plot axis, the first point of a learning curve, a caption, an equation-interface mapping, or an execution contract. But always verify scope. An epoch-0 task score does not answer a reconstruction-loss question merely because both are “before training”.

After surfacing the receipt, check **receipt scope versus attacked-claim scope**. Receipt-first does not mean receipt-only: evidence from one prompt, task, model, budget, or regime cannot close a reviewer alternative about a broader population simply because the fact already exists.

If claim indexing confirms a true missing estimand—or the existing receipt is materially narrower than the attacked claim—choose among reanalysis/replay, one bounded new result, and scope reduction according to decision sensitivity. New evidence and scope calibration may both be necessary; they are not substitutes. Do not automatically scope-reduce before asking whether a single bounded contrast can preserve a load-bearing central claim.

A receipt must come from an attributable author-side source, submission artifact, log, or result record. Track response provenance explicitly:
- `AUTHOR_RESPONSE_COMPLETE` — attributable author rebuttal/reply text is available;
- `REVISION_RECEIPT_AVAILABLE` — a versioned or otherwise attributable artifact verifies that a requested change occurred;
- `OUTCOME_ONLY` — reviewer/meta-review or camera-ready alignment shows only that something was clarified/changed;
- `DECISION_PROVENANCE_ABSENT` — the archive does not show why the final decision followed.

A reviewer's post-feedback statement that “the authors clarified,” or a camera-ready change without version provenance, verifies only the outcome. Never reconstruct missing rebuttal numbers, experiments, wording, or reviewer persuasion.

### Closest-comparator defense
For “this resembles prior work” attacks, build a **claim-indexed comparator lattice** internally. Different priors may be nearest on different axes: primitive lineage, architecture/state object, optimization regime, empirical frontier, inference protocol, data/compute regime.

Then expose only the minimum decision-sensitive subset:
1. identify the comparator relevant to the attacked claim;
2. compare on shared axes such as state definition, objective, architecture, sampler/inference ownership, data regime, and compute budget;
3. bound novelty/causal ownership to what those differences actually support.

Do not force one global nearest prior when different claims have different nearest comparators, and do not dump the full lattice into the rebuttal unless the reviewer confusion requires it.

Deadline chronology can explain why a post-deadline paper was absent from the submission, but it does not replace scientific comparison.

For **package/interface/integration novelty**, first separate inherited primitives from newly owned integration and consequences. A precise shared-axis comparison plus bounded novelty language may be sufficient when the claim is accessibility, interface, scope, or integration rather than empirical superiority. If a pre-deadline comparator already implements most of the claimed object, or if superiority is load-bearing, add a matched comparison or narrow the claim.

### Bounded new-result gate
A conference rebuttal may justify one contained new result only after the **owned-and-load-bearing gate** passes. A coherent small factorial or breadth check spanning several models/tasks/prompts may still count as one bounded result when all cells answer the same reviewer alternative under one estimand. “One result” does not mean one two-arm scalar comparison. Do not start a new research program during rebuttal.

Decision sensitivity and claim ownership matter more than technical elegance or experimental cheapness. Apply this order:
1. exact receipt;
2. clarification / interface contract;
3. claim-indexed comparator positioning;
4. scope calibration;
5. only then ask whether an actually owned central estimand remains threatened by a discriminating alternative.

Only if step 5 remains true should a bounded new result be authorized. Reviewer curiosity about component attribution is not enough when the submitted contribution is an integrated package/interface. A method name or title may identify an integrated package without claiming that every component has an independent positive marginal effect. If one bounded contrast is genuinely necessary to preserve the paper's central claim category, run it rather than automatically narrowing.

Prefer, in order of cost when scientifically sufficient:
- exact evidence receipt;
- wording/clarification;
- analysis of existing outputs;
- bounded replay;
- one contained new experiment;
- scope reduction.

This is not a rigid ladder: scope calibration may be the first correct action for a non-core overclaim, and a new experiment may be necessary when the paper-level category claim would otherwise collapse.

Separate **method-design scope** from **demonstrated-evidence scope**. A method may be designed for a broad problem class while the submitted evidence covers one domain. Do not needlessly redefine the method as domain-specific; narrow unsupported empirical universality language while preserving the method definition.

## 19. Reveal-time ownership rerank

When previously unavailable official results, run receipts, or trusted experimental outputs become available after a source-only draft, **do not merely fill numeric slots**.

Rerun ownership before finalizing the paper:
1. rerank co-primary contributions by observed effect ownership;
2. rerank which experiment actually owns each scientific sentence;
3. reorder the Results spine around matched / multi-run / claim-changing evidence rather than artifact availability;
4. rebuild the main visual bundle from the corrected observed-evidence hierarchy;
5. rerun Abstract evidence budgeting and S10 compression after the Results rerank;
6. automatically demote conformance/audit evidence when a stronger causal or matched experimental contrast now owns the same claim.

An artifact replay can corroborate an official result, provide an independent receipt, or expose a denominator discrepancy. It cannot replace a stronger matched/multi-run official contrast merely because it was available earlier.

A `RESULT_REQUIRED_SLOT` is therefore not a fixed rhetorical location. When it is filled, its new evidence may change contribution ownership and section ordering. Slot filling without reranking is a cross-stage interaction failure.

This rule is now prospectively validated at the integrated-paper level: a source-only draft was frozen, quantitative results were revealed without author narrative, ownership was reranked, and the later full-paper reveal showed lower cross-section delta without organizer drift.

Before results are allowed to drive ownership, validate the result packet itself. Preserve source provenance/hash and cross-check table structure/column assignment when extraction is automated. A malformed neutral packet can corrupt effect ownership just as surely as author prose can bias it.

## 20. Training provenance

This skill was learned by blind construction -> freeze -> reference reveal -> functional comparison -> diagnosis -> rewrite -> adversarial retest.

## 21. Explicit exclusion: major journals/subjournals

Do not use this skill as the default style/structure authority for Nature, Science, Cell, Nature Methods, Nature Machine Intelligence, Nature Biotechnology, or other major journal/subjournal formats.

Cross-genre scientific reasoning may transfer: claim/evidence discipline, reproducibility decomposition, denominator semantics.

But the following must be relearned from zero for the journal track:
- story length;
- narrative pacing;
- main-text density;
- figure count/panel architecture;
- Methods placement;
- result sequencing;
- discussion style;
- biological/contextual breadth;
- supplementary responsibilities;
- editorial/reviewer expectations.

Use a separate future journal-writing skill once that training corpus exists.