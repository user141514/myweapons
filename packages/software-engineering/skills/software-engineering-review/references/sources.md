# Sources, provenance, and limits

Prepared 2026-09-13. The skill text is an original practical synthesis, not a
copy or translation of any handbook, and not a certified implementation of a
standard. The following references justify selected concepts; the compact
workflow, examples, and acceptance rubric are local design choices.

## Primary engineering references

**S1 — IEEE Computer Society, SWEBOK Guide V4.0a.**
https://www.computer.org/education/bodies-of-knowledge/software-engineering/resources/
https://www.computer.org/education/bodies-of-knowledge/software-engineering/v4
Scope: software engineering is broader than testing. The official overview
describes its knowledge-area structure and explicitly includes architecture,
operations, and security. This work checked the overview and edition notice,
not the entire licensed guide. No guide PDF or substantial excerpt is bundled.

**S2 — D. L. Parnas (1972), On the criteria to be used in decomposing systems
into modules, Communications of the ACM 15(12), 1053–1058.**
https://doi.org/10.1145/361598.361623
Scope: decomposition criteria affect comprehensibility, flexibility, and
development work. The publisher abstract supports that framing. The skill's
change-boundary questions are an application, not a claim to reproduce the
paper's full method.

**S3 — NASA Software Engineering Handbook, SWE-055, Requirements Validation.**
https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695440/SWE-055%2B-%2BRequirements%2BValidation
Scope: validate requirements against intended use, operational constraints,
and stakeholder needs. Borrow that distinction, not NASA's project-scale
documentation and approval overhead for every local edit.

**S4 — Eiffel Software, Design by Contract introduction.**
https://www.eiffel.com/values/design-by-contract/introduction/
https://www.eiffel.org/doc/eiffelstudio/I2E-_Design_by_Contract_and_Assertions
Scope: preconditions, postconditions, and invariants as distinct obligations.
Do not confuse executable assertions or formal reasoning with a natural
language instruction claiming to enforce itself.

**S5 — Kubernetes, Liveness, Readiness, and Startup Probes.**
https://kubernetes.io/docs/concepts/workloads/pods/probes/
Scope: distinguish startup, liveness, and traffic-readiness decisions. Target
binding, business progress, and authorization are additional distinctions in
our model, not Kubernetes probe types.

**S6 — Malcolm Featonby, AWS Builders' Library,
Making retries safe with idempotent APIs.**
https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/
Scope: retries with side effects need an explicit idempotency contract and
request intent. Do not transfer AWS-specific default retry assumptions to
an arbitrary tool or browser transport.

**S7 — Dinah McNutt, Google SRE Book, Release Engineering.**
https://sre.google/sre-book/release-engineering/
Scope: reproducible building, controlled releases, version identification,
and deployment/rollback practices. A pushed commit is not runtime evidence.

**S8 — CMU SEI, Architecture Tradeoff Analysis Method collection.**
https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
Scope: evaluate architecture using concrete quality-attribute scenarios,
risks, and tradeoffs. This skill uses a small scenario-driven lens; it does
not require or claim a complete formal ATAM evaluation.

## GitHub and skill references considered

https://github.com/github/awesome-copilot/blob/main/agents/software-engineer-agent-v1.agent.md
Useful: separation of concerns, maintainability, and targeted engineering
checks. Rejected: blanket no-confirmation authority, generic automatic
retries, uninterrupted-execution promises, and documentation for every action.

https://github.com/github/awesome-copilot/blob/main/agents/se-system-architecture-reviewer.agent.md
Useful: considering system context and quality tradeoffs.
Rejected: selecting architectures using coarse scale thresholds, simplistic
technology decision trees, and automatic fallbacks not permitted by the task.

https://github.com/obra/superpowers
The already-installed writing-skills, brainstorming, systematic-debugging,
test-driven-development, and verification-before-completion skills provide
the surrounding workflow. Reuse them rather than creating a second planner,
review service, rule loader, or deployment controller.

## Deliberate limits

This is a judgment aid, not an authorization source, a sandbox, an SLA,
an exhaustive software-engineering curriculum, or a guarantee of future
agent behavior. A discovered file is not automatically an always-on policy.
Critical mechanical safety properties still require checks at their owners.
Evidence about one host, process, release, or task cannot be silently promoted
to all hosts or all future executions. Local observations belong in a dated
acceptance report, not in the evergreen core skill.
