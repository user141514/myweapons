---
name: journal-writing
description: Use for drafting, restructuring, or reviewing research papers aimed at Nature, Science, Cell, or major high-level journal families when long-form journal writing is the target. This skill is trained independently and must not inherit rules from top-conference-paper-writing.
---

# Journal Writing

Status: structural core v1 frozen; asset-to-prose execution v1 stable; end-to-end blind validation active.

This skill is an independent journal-writing track. It does **not** import structures, compression rules, scoring rubrics, or reviewer heuristics from `top-conference-paper-writing`.

## Current operating boundary

- Learn from real, published journal papers recorded in `training/CORPUS.md`.
- Treat a pattern as tentative until it survives transfer to papers with a different scientific and editorial shape.
- Do not force a universal section structure, figure count, paragraph template, or numeric score.
- Record failures and counterexamples; they are allowed to delete or narrow earlier observations.
- Preserve article-type differences instead of averaging them away.

## Stable structural core

### S1 — Dependency-first composition

Do not begin from a journal template. First reconstruct the paper's proof model:

1. central claim object;
2. decisive unresolved transitions;
3. evidence required to close each transition;
4. dependencies and branches among evidence states;
5. evidence regime (for example exploratory, randomized confirmatory, biochemical reconstitution, prospective experimental validation);
6. evidence distance of any extrapolative claim.

Generate the visible paper from this model. Section order, main-figure allocation and paragraph boundaries are projections of the proof model, not upstream rules.

### S2 — Premise trust before downstream consumption

Whenever a new artifact, representation, measurement, classification, model output or causal state will be used as a premise later, establish enough fit-for-purpose validity before downstream claims depend heavily on it.

Validation is evidence-regime dependent: accuracy evaluation, orthogonal assay, source fidelity, calibration, perturbation/rescue, provenance tracing, comparator design or another appropriate check. Headline evidence may appear early, but argumentative dependence must not outrun earned trust.

### S3 — Abstract as a minimum claim-authorization cutset

Treat the abstract as a lossy compression of the proof graph. Select the smallest set of nodes that jointly authorizes the central claim while preserving the unresolved problem, claim object plus evidence regime, decisive proof states, trust status and claim calibration.

Retain any node whose removal would materially change what claim the reader is licensed to accept. A null primary endpoint, comparator, allocation detail or validation gate may therefore be mandatory even under severe compression. Intermediate bridge/support nodes can be omitted when stronger downstream evidence dominates them and authorization is unchanged.

Do not force a fixed sentence count, word allocation or chronological background-method-results-significance template.

### S4 — Opening as bounded re-anchor plus missing prerequisite debt

At a Main/Introduction boundary, allow a short re-anchor of the global problem context. Then add only missing prerequisites needed to expose the decisive unresolved transition.

After re-anchoring, each background unit must perform causal work: explain why the current state fails, define a distinction needed to formulate the gap, establish why the proposed transition is plausible, or establish a constraint/evidence regime that changes what solution is acceptable. Historical material is useful when it explains the active bottleneck, not merely because it is background.

Use: `surface re-anchor -> missing prerequisite debt -> decisive unresolved transition -> this work`.

### S5 — Results paragraph as one decision-consumable state update

Use a Results paragraph to transform one licensed input state into one updated state that changes what later reasoning may assume or what action should follow: `input state -> discriminating evidence/action -> updated state`.

Do not require every paragraph to contain a complete question-method-result-conclusion mini-cycle. Give negative results paragraph-level visibility when they change the model or next action. Start a new paragraph when the next step consumes the just-established state, changes the active unknown, or changes the hypothesis/design under test.

### S6 — Main figures optimize scarce visible decision value

Treat main-figure space as a scarce visual-information budget, not as a ranking of scientific importance. Prioritize packets with high marginal visible decision value: distinct proof/reader-state gain, strong visual explanatory gain, or actionable causal/design/operational leverage.

Down-rank evidence that is redundant with already-visible proof, visually dense, or efficiently summarized in prose/Extended Data. A representative explanatory case can occupy main space while exhaustive aggregate evidence remains supporting, provided the aggregate remains auditable and the case does not inflate certainty.

### S7 — Closing claims maximize authorized semantic strength

Use the strongest semantic statement authorized by the evidence graph and evidence regime while exposing every material inferential jump and unresolved boundary. Calibration is semantic, not a count of hedging words.

Check causality/directness, study design, statistical authorization, population/context scope, power/multiplicity, operational definitions and distance to proposed applications/generalization. A categorical term can be valid when its operational contract is directly satisfied and scope is explicit; hedged wording can still overclaim if the underlying proposition exceeds the evidence.

Place limitations where they mark the boundary of an attractive but unauthorized extrapolation, not merely as a ritual limitations paragraph.

### S8 — Title as the nearest distinctive authorized claim handle

Choose the smallest title phrase that correctly identifies and distinguishes the paper while staying close to directly instantiated evidence. Prefer an identity-bearing object/operation, the nearest distinctive demonstrated capability/property, and any boundary required to avoid overclassification.

Do not optimize for maximum importance language. Quantitative extremes, downstream value propositions and broad field impact can remain in the abstract when they do not improve paper identity or would increase evidence distance.

### Routing

After S1, route by **central claim object first, evidence regime second**. Stable claim-type adapters A1–A6 live in `training/ADAPTERS.md`; they are proof-obligation sets, not mandatory outlines. Do not treat journal family (Nature / Science / Cell) as a substitute for claim-type routing.

## Training loop

Use the smallest useful loop:

`mimic -> test on a different paper type -> identify mismatch -> correct -> retest`

The structural core is frozen, but prose execution is **not** considered trained until it passes asset-blind writing tests:

`assets only -> locked draft -> reveal published prose -> compare information selection / ordering / paragraph transitions / claim calibration / sentence realization -> mutate the smallest responsible rule -> re-draft or test on a new unseen paper`

The loop itself is stable; its internal tasks, comparison dimensions, and acceptance criteria are intentionally allowed to change as evidence accumulates.

## Use on manuscripts

1. Identify the intended journal family, central claim object and evidence regime.
2. Build the dependency model from S1 before choosing visible structure.
3. Apply S2 to every object that downstream claims will treat as trusted input.
4. Route through the closest stable adapter in `training/ADAPTERS.md`; for hybrid papers, choose one dominant adapter and import only the secondary proof modules actually required.
5. Apply S3–S8 to title, abstract, opening, Results paragraphs, main figures and closing claims.
6. If the task falls outside the frozen v1 surfaces, treat it as untrained and prefer direct comparison with the closest real paper rather than inventing a universal convention.

## Training records

- `training/STATE.md`: authoritative current learning state.
- `training/ADAPTERS.md`: stable A1–A6 routing and proof obligations.
- `training/EXECUTION.md`: stable X0–X7 asset-to-prose execution model.
- `training/EXECUTION_OBSERVATIONS.md`: archived detailed failure-derived execution observations.
- `training/CORPUS.md`: selected real-paper corpus and why each paper is present.
- `training/V1_FREEZE.md`: v1 acceptance evidence, invariants and explicit untrained surfaces.
- `training/rounds/`: individual mimic/test/correct/retest episodes.
