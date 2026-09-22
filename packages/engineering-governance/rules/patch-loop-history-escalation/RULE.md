## Patch-loop / history escalation gate

Do not equate continued patching with progress. Before adding another fix at a boundary that has already received recent fixes, inspect whether the current failure is being created or exposed by earlier changes.

Trigger this gate when any of these signals appears:

- the same interface/module/boundary needs multiple sequential fixes in one task;
- a new patch compensates for behavior introduced by an earlier patch;
- each fix reveals a new shared-infrastructure problem and the mutation surface keeps widening;
- new fallback/reconcile/special-case logic is being added mainly to preserve earlier changes;
- tests are green locally but another adjacent contract repeatedly breaks;
- the next proposed fix cannot be explained directly from the original Claim and Owned Surface.

When triggered, **pause new mutation** and review the history from the assignment start or nearest known-good baseline:

`original assignment -> authorized diff -> later patches -> current failure`.

Classify earlier hunks as `EXPLICIT | NECESSARY | OBSERVED-UNOWNED | WRONG-ASSUMPTION`. Ask whether removing/reverting an earlier unauthorized or wrong-assumption change would eliminate the need for the new patch. Prefer the smallest rollback/revert of the causal overreach over another forward compensation patch.

A deadline, desire to keep momentum, existing sunk cost, or "tests pass after this patch" is not authorization to continue a patch chain. If ownership/root cause cannot be established without a new owner, unavailable evidence, or architectural decision, stop at that blocker and hand it off. Pausing is a valid engineering outcome.

Do not over-trigger this gate for one isolated defect with a clear owner and causal fix. Its purpose is to detect **patch chains as evidence of a bad historical decision**, not to forbid bounded bug fixes.

