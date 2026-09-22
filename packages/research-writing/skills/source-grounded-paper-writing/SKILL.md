---
name: source-grounded-paper-writing
description: Use when learning or drafting academic papers from real source code, experiment artifacts, configs, figures, or results, especially when the user wants to first reconstruct and write the paper independently and only afterward compare against the original published paper. This is a source-first writing-learning workflow, not a style-summary or polishing skill.
---

# Source-Grounded Paper Writing

## Purpose

Learn scientific writing by reconstructing a paper from the underlying research artifact rather than by imitating summaries, templates, or prose style.

Core loop:

source / experiments -> reconstruct scientific object -> write independently -> reveal original paper -> compare -> diagnose -> rewrite -> distill transferable rule

This skill sits upstream of research-paper-writing.

Use research-paper-writing only after the scientific reconstruction and comparison loop has produced a stable draft.

## 1. Holdout rule

When an original/reference paper exists, do not read its:
- abstract;
- introduction;
- method prose;
- results narrative;
- figure captions;
- supplementary writing;

before the independent draft is frozen for the target section.

Allowed before the reveal:
- source code;
- configs;
- tests;
- dataset/evaluator scripts;
- experiment logs/results;
- figures without captions when useful;
- factual metadata needed to run/understand the artifact.

README text is allowed only if it does not expose the paper story; otherwise treat it as held out.

If the model may already know the paper, label the episode POTENTIALLY_CONTAMINATED and use it only as a workflow smoke test, not as a writing-skill score.

## 2. Reconstruct before writing

### 2.0 Artifact Visibility Map

Before scoring a blind reconstruction, list each paper-level scientific object as `visible`, `partially visible`, or `not visible` in the allowed artifacts, with a source anchor where possible.

Do not penalize the blind writer for missing training-label semantics, objectives, data mixtures, checkpoint-selection rules, curriculum details, or other load-bearing information that is absent from the allowed artifact. After reveal, classify such differences as `SOURCE_VISIBILITY_GAP`, not `MISSING_ABSTRACTION`.

Unknown-boundary discipline is a positive skill: explicitly stating that the source cannot establish a claim is better than inventing author intent.

Build the smallest scientific model needed for the target section:

- task / scientific question;
- input and output objects;
- state representation;
- model or algorithm components;
- information flow;
- training objective;
- inference procedure;
- evaluator and denominator;
- decisive ablations / baselines;
- supported result;
- unsupported boundary.

Do not begin prose until this reconstruction is explicit.

For Method, reconstruct:
problem -> variables/state -> operation -> state transition -> objective -> training -> inference

For Experiments:
claim -> strongest alternative explanation -> comparison -> protocol -> metric -> result -> interpretation -> boundary

During blind experiment design, classify each proposed evidence item as:
- `CLAIM_CHANGING` — directly changes what scientific sentence is defensible;
- `FUNNEL` — explains selection/filtering or how later evidence is reached;
- `AUDIT_SUPPORT` — improves reproducibility, denominator integrity, or bias detection but is not itself the central scientific proof.

Rank these roles before drafting. Audit completeness should support, not obscure, the few pieces of evidence that actually eliminate the major alternative explanations.

For Introduction:
first reconstruct the paper's actual technical contribution from source/results, then use literature context. Do not infer the contribution from the reference paper's introduction during the holdout phase.

## 3. Pre-draft evidence tables

Before prose, build three compact tables when applicable.

### Contribution Candidate Table

For each visible module/intervention, record:
- failure/problem it targets;
- scientific quantity/object it changes;
- operation;
- falsifiable prediction;
- direct evidence;
- strongest cheap alternative explanation;
- classification: core scientific mechanism / implementation carrier / boundary adapter / compute optimization / evaluation-postprocessing contract.

This prevents source-code coverage from becoming the Method outline.

### Abstraction Hierarchy and Ranking

Do not stop after finding one elegant abstraction. Build exactly three levels when possible:

1. **Problem-level abstraction** — what scientific task is being reformulated or newly made possible?
2. **Method-level abstraction** — what mechanism/state/object actually solves that problem?
3. **Implementation/decision-level abstraction** — what architecture, selector, adapter, search, or post-processing realizes the mechanism?

Then rank candidate organizers by **explanatory ownership**:
- problem ownership — does it explain why the research exists?
- method coverage — does it explain several major modules/interventions?
- comparator ownership — does it define the strongest alternative and shared comparison axes?
- evidence ownership — do the decisive experiments naturally organize around it?
- effect ownership — when result assets are visible, does it own the largest/generalizable effect?
- claim ownership — if removed, which headline sentence collapses?
- boundary ownership — does it explain the main negative boundary?

Prefer the most upstream abstraction that still has concrete operational content. Do not choose a lower-level mechanism merely because it has the cleanest equation.

If result assets are held out, mark `EFFECT_OWNERSHIP_UNKNOWN` instead of pretending the source alone reveals empirical importance.

### Comparator Axis Table

For each top contribution candidate, identify the closest alternative formulation and ask **which scientific quantity actually changes**.

Record:
- reference/alternative method;
- comparison axes (for example complexity, path length, information ownership, objective weighting, supervision semantics, noise/information schedule, compute location);
- where each alternative should differ if the abstraction is correct;
- which equation/table/experiment could expose that difference;
- scope where the comparison no longer holds.

This table exists because a correct scientific object may still be the wrong organizing abstraction. Strong papers often become legible only after the method is placed on the comparison axes that explain *why it should exist relative to alternatives*.

### Dual Evidence Maps

Build two maps before deciding what belongs in the paper's main scientific evidence bundle.

#### Map A — Scientific Contrasts
For every candidate claim, record:
- claim;
- strongest alternative explanation;
- comparison/control;
- denominator;
- metric;
- result;
- negative boundary;
- what scientific sentence must narrow if this evidence is removed.

#### Map B — Reporting / Reproducibility Contracts
Track separately:
- split manifest;
- complete denominators;
- hashes/checkpoints;
- environment/container;
- exact command;
- failure logs;
- artifact-to-table reproduction receipts.

Map B is scientifically load-bearing only when the claim itself concerns reproducibility, contamination-free generalization, calibrated success rate, or deployment reliability. Otherwise Map B supports Map A and should not be counted as another scientific experiment.

### Minimal Scientific Bundle Test

An item enters the minimal scientific bundle only if:
1. deleting it forces a scientific sentence to narrow;
2. no remaining scientific contrast can support that same sentence;
3. it removes a distinct major alternative explanation;
4. it is not merely provenance/reporting infrastructure.

### Asset/Reproducibility Matrix

Required for hard-to-reproduce work. Track separately:
- inference reproducibility;
- training reproducibility;
- benchmark/result reproducibility;
- fixed-output auditability;
- wet-lab/physical validation reproducibility.

Do not collapse them into one binary `reproducible` label.

## 4. Independent draft

Write the target section as if the original paper did not exist.

Requirements:
- every technical statement must trace to source/evidence;
- choose the abstraction level yourself rather than translating code line-by-line;
- omit implementation details that do not change the scientific object;
- surface invariants, interfaces, and equations where they compress many implementation details;
- separate what the artifact does from why it may be useful;
- mark unknown intent instead of inventing it.

Freeze this draft before revealing the original paper.

## 5. Reveal and compare

After the independent draft is frozen, read the corresponding section of the original paper.

Compare by function, not by phrase matching.

Evaluate at five levels:

1. Scientific abstraction
   - What object did the authors abstract from the implementation that the draft missed?
   - What did the draft overfit to code details?

2. Information architecture
   - Which concepts are introduced earlier/later?
   - What dependency order does the published paper use?

3. Compression
   - Which implementation details are compressed into notation, equations, modules, or one sentence?
   - Where is the draft verbose because it lacks a higher-level concept?

4. Evidence / claim
   - What claims does the paper make that are supported by the artifact?
   - What claims did the draft overstate or fail to surface?

5. Reader model
   - What background does the paper assume?
   - What does it explain explicitly that the draft incorrectly assumes?

Do not treat different wording as an error by itself.

For each important reference-paper choice, additionally classify it as:
- COPY — clearly better scientific abstraction/evidence communication;
- ADAPT — useful abstraction, but source fidelity or boundary disclosure should be strengthened;
- REJECT — opaque funnel, unfair comparison, reporting inconsistency, unsupported claim, or merely author-specific preference.

The published paper is a comparison target, not an unquestionable gold standard.

Do not copy distinctive phrases from the paper into the rewrite.

## 6. Diagnose the difference

Every important difference must be classified as one of:

- SOURCE_MISREAD — source behavior reconstructed incorrectly;
- SOURCE_VISIBILITY_GAP — the reference relies on load-bearing information that was not present in the allowed blind artifacts;
- MISSING_ABSTRACTION — relevant implementation/evidence was visible but its scientific concept was not extracted;
- WRONG_GRANULARITY — too much or too little detail;
- ORDERING_ERROR — dependency/message order is weak;
- MISSING_MOTIVATION — design appears arbitrary;
- MISSING_EVIDENCE — claim lacks explicit experiment support;
- OVERCLAIM — prose exceeds evidence;
- TERMINOLOGY_GAP — concept named poorly or inconsistently;
- NOTATION_GAP — equations/notation would compress the explanation;
- READER_MODEL_ERROR — assumes the wrong background;
- ORIGINAL_PAPER_CHOICE — a legitimate author choice, not a defect in the independent draft.

## 7. Rewrite from the diagnosis

Rewrite from the reconstructed scientific model plus diagnosed lessons.

Do not paraphrase the original paper sentence-by-sentence.

The rewrite should be explainable as:
same underlying source evidence + better abstraction/order/compression

## 8. Distill transferable rules

### Stable rules from the current transfer corpus

Use these as defaults, not universal laws:

1. **Source correctness is not paper abstraction.** A paper-level Method normally needs the scientific object, the quantity/state/interface it changes, the strongest relevant alternative, shared comparator axes when useful, and a falsifiable consequence.
2. **Scientific abstractions may span modules.** Search across data construction, training stages, interfaces, schedules and comparisons rather than assuming one class/function equals one contribution.
3. **Score blind writing only against visible evidence.** Missing private training labels, hidden data mixtures, internal selection or unreleased objectives is `SOURCE_VISIBILITY_GAP`, not abstraction failure.
4. **Use equations only when they compress scientific dependency.** Good equations define state, reference, responsibility, transition, information relation, decision rule or trade-off; do not mathematize code merely for style.
5. **Calibrate evidence to the exact claim.** Ask which plausible alternative would materially reverse or narrow that claim, and design a contrast against it. Do not turn every reviewer question into a main-paper experiment.
6. **Claim layers need distinct logical contrasts, not necessarily distinct experiments.** One factorial can support several layers; many metrics can still be one evidence modality.
7. **Task breadth is not evidence independence.** Independence depends on contrast, provenance, target object, adaptation regime and dominant failure mode.
8. **Reproducibility is multi-dimensional.** Track training, inference, benchmark/result, fixed-output and physical/biological reproducibility separately.
9. **Credibility and artifact reproducibility are related but non-identical.** Missing assets can coexist with a credible bounded empirical claim when independent evidence supports that exact claim; this does not establish stronger causal claims about the missing training process.
10. **Expose denominators when they change the scientific estimand.** Keep exhaustive attempt logs in reproducibility assets unless they change the main scientific interpretation.
11. **Use negative results to locate the method boundary.** A useful negative result distinguishes what the method solves from what it does not solve.

### Revised evidence-minimality rule

Do not force every paper into a fixed number of decisive experiments.

- For a narrow claim, seek the minimal decisive contrast/evidence.
- For a complex multi-claim paper, seek the **minimal non-redundant evidence bundle**.

A bundle item belongs only if:
- it protects a central claim;
- it removes a distinct strong alternative explanation;
- no other bundle item can do the same job;
- its denominator and boundary are explicit;
- deleting it would force a real claim to narrow.

### Two evidence thresholds

Distinguish:
- **bounded empirical/method threshold** — enough to establish useful performance under named tasks/protocols;
- **strong causal/mechanistic threshold** — requires matched controls, isolated interventions, corpus exclusion, frozen representations, counterfactuals or orthogonal physical/biological evidence as appropriate.

Do not reject a bounded methods paper merely because it does not prove a stronger causal sentence it never needs to make.

Promotion levels:
- one episode -> PROVISIONAL;
- at least two independent episodes -> REPEATED;
- STABLE requires later rounds with additional independent papers and an explicit counterexample check.

A POTENTIALLY_CONTAMINATED episode may support recurrence, but must not independently justify STABLE status.

Store each rule with:
- trigger/context;
- bad pattern;
- improved pattern;
- why it helps;
- counterexample / when not to use it.

Do not generalize one author's stylistic preference into a universal writing rule.

## 9. Hard-reproduction credibility track

For papers where training, weights, data pipelines, scale, or wet-lab assets are not fully reproducible, run an additional blind/reveal exercise.

Before reference reveal:
1. inventory exactly what a third party can reproduce;
2. separate training, inference, benchmark, fixed-output, and wet-lab reproducibility;
3. predict the minimum evidence required for the intended claim;
4. identify potential fatal gaps.

After reveal, map each evidence layer to the gap it replaces.

Use the sentence discipline:
> This evidence supports X; it partially substitutes for missing Y; it does not establish Z.

Also record full candidate/search/filter funnels and information-isolation channels when relevant.

See `references/round1-repeated-rules.md` for currently repeated but not yet stable rules.

## 10. Practice progression

### Stage 0 — contaminated smoke test
Use a known paper/codebase to verify the workflow.

### Stage 1 — section reconstruction
Use a less-familiar source+paper pair.
Practice Method first, then Experiments.

### Stage 2 — story reconstruction
Draft title/abstract/introduction from source + results before seeing the original story.

### Stage 3 — own research
Apply the learned workflow to the user's own research, where no reference answer exists.

Own-research writing starts only after the skill has passed at least two external reconstruction episodes.

## 11. Relationship to other skills

Use:
- graft or source inspection to understand code;
- molecular-ai-grounding for molecular-state semantics;
- this skill for reconstruction/comparison learning;
- top-conference-paper-writing when the target is a short-form top-conference paper and the conference track has enough evidence;
- research-paper-writing only as a downstream generic clarity/reviewer-facing revision layer;
- nature-polishing only at the final English prose polish stage.

Do NOT route major-journal/subjournal writing through top-conference-paper-writing. Journal/subjournal writing remains a separate track that must be trained independently from its own blind/reveal corpus.

Do not substitute downstream polishing for missing scientific reconstruction.

## 12. Output contract

For each practice episode produce:

1. Source model — concise scientific reconstruction.
2. Frozen independent draft — before reference reveal.
3. Reference comparison matrix — differences by function.
4. Diagnosis — classified root causes.
5. Rewritten draft — independently re-authored.
6. Transferable lessons — promoted vs provisional rules.
7. Next practice target — one specific weakness to train next.

## Stop rule

If the comparison produces only superficial style differences, the episode did not teach enough.

Choose a new source/paper pair with a clearer scientific-method mapping rather than accumulating generic writing tips.
