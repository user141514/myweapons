---
name: research-factory
description: Use when the model is about to organize ongoing research into paper candidates, diagnose low research throughput, decide whether an idea should be screened/killed/promoted, convert historical results into publishable candidates, choose between CARD/GAP/PILOT/FULL stages, or when research is drifting into deep mechanism explanation without paper-level conversion. 适用于科研工厂、论文候选筛选、研究进度卡点诊断、历史结果挖矿、候选淘汰/晋级和从实验到论文的产出管理；不要仅因为项目是科研项目就固定触发。
---

# Research Factory

Trigger this skill from **behavior**, not repository identity.

Use it when the current reasoning is doing one of these things:
- turning a research direction into one or more paper candidates;
- deciding whether a candidate deserves compute;
- diagnosing why weeks of experiments have not converted into a paper;
- mining historical results for unfinished paper-shaped opportunities;
- choosing the next action after a GAP/PILOT/FULL result;
- noticing that mechanism explanation is growing faster than paper-level evidence;
- allocating parallel workers across novelty, baseline, implementation, review, and writing;
- deciding whether work belongs in PAPER_READY, KILLED, or THESIS_DEPTH.

Do **not** trigger merely because the repository is scientific or molecular.
Do not replace domain grounding or research-convergence; compose with them only when the behavior requires it.

## Core objective

Optimize trustworthy paper-level output per calendar time.

The first-class object is the **paper candidate**, not the mechanism branch.

A useful research week should preferentially create:
- screened candidate cards;
- reproduced gaps;
- completed pilots;
- figures/tables/manuscript sections;
- fast kills that release WIP.

Counts of hypotheses, mechanism explanations, tests, plans, closeouts, or agent turns are not primary progress.

## Candidate lifecycle

IDEA -> CARD_SCREENING -> GAP_REPRODUCTION -> METHOD_PILOT -> FULL_CONFIRMATION -> PAPER_READY

Terminal: KILLED / THESIS_DEPTH / SHORT_PAPER_READY

A bounded HARVEST lane may convert a robust non-flagship finding into a short paper without reopening the original method:
THESIS_DEPTH -> HARVEST_SCREENING -> SHORT_PAPER_READY or ARCHIVE.

### CARD_SCREENING
Before compute, require:
- plausible working title;
- generated object/task;
- named baseline;
- one reproducible or cheaply testable gap;
- one-sentence method delta;
- nearest direct prior;
- strongest cheap rival;
- three-figure story;
- minimum evidence package;
- budget;
- kill rule.

If title + three-figure story are not credible, do not promote.

### GAP_REPRODUCTION
Goal: prove the baseline gap exists locally.
Default budget: <=24 h.
No broad mechanism decomposition.
No gap -> KILL.

### METHOD_PILOT
Default budget: <=48 h.
At most: baseline; exact method delta; strongest cheap rival.
One primary endpoint.
One implementation/evaluator rescue for a concrete defect.
A valid scientific negative gets no parameter rescue.

### FULL_CONFIRMATION
Default total candidate cycle: <=7 days.
Allowed: independent confirmation; one quality/coverage/cost safeguard; one ablation family; closest-prior comparison; manuscript completion.
Must terminate as PAPER_READY / THESIS_DEPTH / KILLED.

## Anti-thesis-depth invariant

Within one card:
Observation -> one load-bearing model -> one discriminator -> result

One valid negative may authorize one upstream model update.
If the updated model also fails: close the card.
A third-generation explanation must re-enter the portfolio as a new candidate and compete for WIP.

## Historical-result mining

History is a mine, not a roadmap.
A historical result may become a new card only if:
1. its downstream lineage does not already kill the claim;
2. it is endpoint/task-level, not merely a precursor PASS;
3. a paper-shaped missing experiment still exists;
4. direct prior and strongest cheap rival remain unresolved;
5. it is not repair-only / baseline-integrity / thesis-depth work.

Never resurrect a precursor PASS whose downstream endpoint experiment failed.

## Parallel workcells

Fresh workers are disposable workcells.
Good scopes: direct-prior attack; baseline/gap reproduction; historical-result mining; implementation; independent review; figure/table/manuscript drafting.
Parent owns the candidate state and final decision.
Workers do not recursively create research trees.
Parallelism is useful only if it reduces CARD/GAP/PILOT cycle time.

## WIP defaults

- IDEA backlog <=12
- scientifically active candidates <=2
- GAP candidates <=2
- METHOD_PILOT <=1
- FULL_CONFIRMATION <=1
- GPU-heavy candidate <=1
- high-cost independent reviewer <=1

Fast KILL is successful throughput.
HARVEST WIP <=1 and must not consume the main METHOD_PILOT GPU slot.

## Paper-first behavior

At admission, draft: title; ~150-word abstract hypothesis; three figure captions; claim/limitation bullets.
After GAP PASS: problem paragraph; related-work table; method notation; empty main-results table.
After PILOT PASS: freeze Figure 1 and Methods; draft Results directly from artifacts.
During FULL: write Introduction/Related Work/Limitations in parallel.

For HARVEST_SCREENING, require the bounded claim to survive downstream evidence, direct-prior screening to pass, <=2 missing experiments, and <=3 days to a complete short-paper/workshop draft. Harvesting must not reinterpret repair, audit, or negative evidence as generator improvement.

## Integrity boundary

Industrialize literature triage, code templates, experiments, figures/tables, manuscript drafting, and reviewer simulation.
Never industrialize fabricated/manipulated data, hidden denominators, retry-until-success, repair/filtering presented as raw generation gain, target leakage, or salami slicing.

## Coordination with other skills

Use `research-convergence` when the behavior is primarily selecting a scientific hypothesis, choosing a discriminator, comparing method candidates, or recovering an interrupted research experiment.
Use `molecular-ai-grounding` when the behavior is primarily defining a molecular state/intervention or checking graph/geometry/charge/stereo/physical semantics.
Use this skill when the behavior is primarily paper-level portfolio and throughput, candidate lifecycle, historical asset conversion, or deciding whether to continue, kill, or write.
When multiple apply, read the smallest set needed for the actual behavior.