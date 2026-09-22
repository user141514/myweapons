# Comparison Rubric

Use after the independent draft is frozen and the reference paper is revealed.

## 1. Scientific reconstruction score

Rate 0–2 for each:
- task is reconstructed correctly;
- input/output object is correct;
- state variables are correct;
- major components and dependencies are correct;
- training objective is correct;
- inference procedure is correct;
- evaluator/denominator is correct;
- major claim boundaries are correct.

A writing comparison is invalid if source reconstruction is substantially wrong.

## 2. Abstraction score

For each subsection ask:
- Did the draft name the scientific object, or narrate implementation details?
- Did it identify invariants/interfaces?
- Did it compress repeated code into one concept/equation?
- Did it separate implementation choices from contribution-level design?

Typical failure:
“layer-by-layer source translation”.

Desired behavior:
“scientific object reconstructed from implementation”.

## 3. Information-order score

Compare dependency order:
- prerequisite concept before dependent concept;
- motivation before unexplained design;
- notation before equation use;
- method before implementation detail;
- comparison protocol before result claim.

Tag each important ordering difference:
- BETTER_REFERENCE_ORDER;
- BETTER_DRAFT_ORDER;
- EQUIVALENT_CHOICE.

Do not assume the published paper is automatically optimal.

## 4. Compression score

For every paragraph, label:
- necessary technical detail;
- implementation-only detail;
- repeated detail;
- missing abstraction;
- missing notation;
- missing figure/table support.

Measure improvement by fewer conceptual steps needed by the reader, not by sentence count alone.

## 5. Claim-evidence score

For each major sentence:
- claim;
- source/evidence anchor;
- reference-paper wording scope;
- draft wording scope;
- supported / unsupported / narrower-than-needed.

Prefer correct narrow claims over impressive unsupported claims.

## 6. Reader-model score

Check:
- what prior knowledge is assumed;
- what terminology is introduced;
- what background is explained;
- where the draft is too code-internal;
- where the reference paper is too terse.

## 7. Difference diagnosis table

Use columns:

| Difference | Draft | Reference | Diagnosis class | Which is better? | Why? | Rewrite action |
|---|---|---|---|---|---|---|

Allowed diagnosis classes are defined in SKILL.md.

## 8. Rule promotion

A writing lesson is:
- PROVISIONAL after one episode;
- REPEATED after two independent episodes;
- STABLE after at least three episodes with no strong counterexample.

Stable rules may be folded into research-paper-writing later.

Do not promote:
- author-specific voice;
- venue formatting convention;
- one-off notation;
- phrase-level imitation.
