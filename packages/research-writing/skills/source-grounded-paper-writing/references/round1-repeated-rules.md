# Round-1 Repeated Rules

status: REPEATED_NOT_STABLE
source episodes:
- MolDiff
- ResNet
- AlphaFold3
- AlphaMissense
- RFdiffusion

## Track A — Source to paper

### R-A1 Scientific objects, not source coverage
Method prose should be organized around scientific objects and causal design decisions, not source-file or execution-order coverage.

Repeated in:
- MolDiff
- ResNet
- AlphaMissense

### R-A2 Problem -> hypothesis -> operation -> falsifiable prediction -> experiment
A method becomes paper-shaped when the intervention is paired with the failure it targets and the evidence required to show that it owns the effect.

Repeated in:
- MolDiff
- ResNet
- AlphaMissense

### R-A3 Equations should define a scientific object
Prefer equations that define:
- state;
- reference mapping;
- residual;
- information quantity;
- objective;
- transition;
- decision rule.

Avoid equations that merely shorten a helper-function implementation.

Repeated in:
- MolDiff
- ResNet

### R-A4 Main-text granularity follows scientific explanation
Implementation detail belongs in the main paper only when changing it changes:
- the scientific object;
- the claim;
- the denominator;
- the information contract;
- the inference behavior.

Repeated in:
- MolDiff
- ResNet
- AlphaMissense

### R-A5 Source-first is not source-only story
Hold out the reference paper prose, but own-paper reconstruction may use:
- source;
- frozen experiment results;
- baseline evidence;
- problem observations.

Source alone often cannot reveal the empirical failure that motivated the design.

Repeated in:
- MolDiff
- ResNet
- AlphaMissense

## Track B — Credibility under reproduction debt

### R-B1 Split reproducibility into distinct axes
Never say “the paper is reproducible” as one binary.

Track separately:
- inference reproducibility;
- training reproducibility;
- benchmark/result reproducibility;
- fixed-output auditability;
- wet-lab reproducibility.

Repeated in:
- AlphaFold3
- AlphaMissense
- RFdiffusion

### R-B2 Replacement evidence supports bounded claims; it does not erase the debt
Examples of replacement evidence:
- independent external benchmarks;
- blinded/temporal evaluation;
- public fixed predictions;
- orthogonal assays;
- wet-lab validation;
- experimental structures;
- detailed ablations.

Each must be written as:
“supports X; partially replaces missing Y; does not establish Z.”

Repeated in:
- AlphaFold3
- AlphaMissense
- RFdiffusion

### R-B3 Evidence strength should climb with claim strength
Typical hierarchy:
model output
-> independent computational validation
-> biological/physical assay
-> structural/experimental confirmation.

Do not let one strong instance imply calibrated population performance.

Repeated in:
- AlphaMissense
- RFdiffusion
- AlphaFold3

### R-B4 Report the full search/filter funnel
For generative or selection-heavy systems track:
raw attempts
-> computationally valid
-> filtered/ranked
-> manually selected
-> experimentally tested
-> successful.

Expose:
- best-of-N;
- candidate budget;
- ranking budget;
- human selection;
- exclusions.

Repeated in:
- RFdiffusion
- AlphaFold3
- AlphaMissense (decision/calibration layer)

### R-B5 Information isolation is channel-specific
Distinguish:
- labels used for training;
- calibration/model selection;
- pretraining overlap;
- homology/family overlap;
- future database information;
- temporal holdout;
- blinding.

Repeated in:
- AlphaFold3
- AlphaMissense
- RFdiffusion

### R-B6 Visible failure boundaries improve a defensible narrow claim
Negative results should be promoted into the scope boundary rather than buried as local caveats.

Repeated in:
- AlphaFold3
- AlphaMissense
- RFdiffusion

## Practices not to copy from reference papers

Reference papers are not automatically the writing ground truth.

Reveal comparison must allow:
- COPY — clearly better abstraction/evidence communication;
- ADAPT — good abstraction but needs stronger source fidelity/boundary disclosure;
- REJECT — opaque funnel, inconsistent reporting, unfair comparison, or author-specific preference.

Round-1 REJECT/ADAPT examples:
- RFdiffusion's incomplete early-stage selection funnel;
- RFdiffusion reporting-summary mismatch with manual exclusions/selection;
- AlphaFold3's detailed methods not being equivalent to benchmark/training reproducibility;
- fixed-output release not being equivalent to a deployable/retrainable model;
- main-text omission of postprocessing details when they change molecular identity.
