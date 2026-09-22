# Stable Writing-Transfer Rules V1

date: 2026-09-20
source:
- first-cycle closures
- second-cycle adversarial closures
status: STABLE RULES ONLY

## S1 — Source correctness is not paper abstraction

Correct implementation reconstruction is necessary but insufficient.

A scientific Method must identify at least one higher-level object such as:
- state/representation;
- controlled quantity;
- interface/ownership boundary;
- supervision regime;
- process relation;
- reference state;
- objective trade-off.

Bad:
“module A calls B then C.”

Better:
“the method changes X relative to reference Y, which predicts behavior Z.”

Boundary:
for systems/software papers, execution topology itself may be the scientific object.

## S3 — Claim-evidence design is claim-strength calibrated

Evidence requirements depend on the exact verb in the claim.

Examples:
- works
- transfers
- causes
- generalizes
- is universal
- is calibrated
- is physically realized
- is clinically useful

Do not silently strengthen a claim and then judge the paper against evidence required for the stronger sentence.

For every claim:
1. write the weakest useful sentence;
2. write stronger versions;
3. identify the first evidence layer required for each upgrade.

## S4 — Experiments are claim–alternative–evidence graphs

For each important experiment:

claim
-> strongest plausible alternative explanation
-> discriminating evidence
-> result
-> sentence enabled
-> remaining boundary

Evidence roles:
- CLAIM_CHANGING
- FUNNEL
- AUDIT_SUPPORT

A strong experiment section is not a checklist.

The minimal evidence set can be:
- one clean discriminating experiment; or
- a multi-modal evidence bundle.

“Minimal” means every main-text evidence item has a claim-changing role, not that the paper has few experiments.

## S5 — Reproducibility is multidimensional

Track separately:
- training reproducibility;
- inference reproducibility;
- benchmark/result reproducibility;
- fixed-output auditability;
- biological/physical validation reproducibility.

Never collapse them into one binary “reproducible” variable.

Runnable inference does not prove training reproduction.
Missing training assets do not erase independently testable fixed-model results.

## S6 — Reproduction debt is offset by evidence, not rhetoric

When some research assets are unavailable or prohibitively expensive, credibility must come from falsifiable evidence appropriate to the claim layer.

Possible compensating evidence:
- time-shift/external benchmark;
- low-confound control;
- independent evidence domain;
- fixed public predictions;
- physical/biological validation;
- explicit failure boundary.

Prestige, venue, prose confidence and authority are not substitutes.

Boundary:
compensating evidence supports a bounded scientific claim; it does not make the missing artifact reproducible.

## S8 — Denominator discipline is evidence infrastructure

Surface denominators whenever changing the denominator changes scientific interpretation.

Examples:
- raw generated samples;
- filtered candidates;
- selected constructs;
- expressed constructs;
- assayed constructs;
- structurally resolved constructs.

Do not let exhaustive denominator accounting dominate a method-paper narrative unless denominator/evaluation methodology is itself the contribution.

Main text:
show the denominators needed to interpret the claim.

Supplement/repository:
store the complete attempt ledger and selection details.

## Cross-rule workflow

Before drafting a section:

1. ARTIFACT VISIBILITY
2. SCIENTIFIC OBJECT
3. COMPARATOR AXIS
4. CLAIM LADDER
5. ALTERNATIVE EXPLANATIONS
6. EVIDENCE ROLES
7. NARRATIVE COMPRESSION
8. BOUNDARY

The comparator-axis rule is still STABLE_CANDIDATE, not yet in this file as a stable rule.
