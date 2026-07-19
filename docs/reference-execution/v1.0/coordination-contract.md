# Reference Execution v1.0 Coordination Contract

Status: proposed program-level contract for [Issue #9](https://github.com/joselunasrt8-creator/Continufy-/issues/9)

Reference Execution v1.0 tests whether the current, version-bound audit and evidence instruments can repeatedly produce complete, valid, traceable, and intelligible artifacts across materially different repositories. It establishes internal reproducibility only. It is not independent replication, external validation, scientific acceptance, repository authority, or permission to execute.

This contract coordinates separately authorized, repository-owned work. Continufy does not execute against, freeze, mutate, or make determinations for a participating repository.

## Governing dependencies

- [Issue #1](https://github.com/joselunasrt8-creator/Continufy-/issues/1) owns the [canonical instrument specification](canonical-instrument-specification.md) and its versioned output semantics.
- [Issue #8](https://github.com/joselunasrt8-creator/Continufy-/issues/8) owns program readiness and the repository-local freeze boundary.
- [Issue #3](https://github.com/joselunasrt8-creator/Continufy-/issues/3) owns the broader portfolio and artifact map; this execution must not substitute for it.
- This contract owns only the Reference Execution v1.0 cohort protocol, record requirements, comparison rules, and sealing criteria.

If a dependency is incomplete or contradictory, record the condition as `BLOCKED` or `INDETERMINATE` as defined below. Do not repair the dependency by inventing program-level authority or silently changing its meaning.

## Execution scope

The execution subject is each participating repository at one exact, repository-approved commit. The governing methodology and instruments are the exact immutable versions recorded before execution. Evidence consists of the bound inputs, generated artifacts, validation results, hashes, provenance, interventions, observations, and rerun results required by this contract.

The coordinated sequence is:

```text
Freeze -> Execute -> Observe -> Compare -> Calibrate -> Rerun -> Seal
```

`Calibrate` means recording friction, ambiguity, and improvement candidates. It does not permit an instrument, methodology, canonical definition, input commit, or completed record to be changed within v1.0. A required change creates follow-up work for a later version.

Issue #9 establishes this protocol and its handoff template only. It does not authorize or perform the downstream executions.

## Participating repository inventory

The v1.0 candidate cohort is fixed to these verified repository identities:

| Repository | Canonical repository | Required pre-execution binding |
| --- | --- | --- |
| MindShift | [`joselunasrt8-creator/MindShift-`](https://github.com/joselunasrt8-creator/MindShift-) | Exact commit and repository-local freeze record |
| Research Methodology | [`joselunasrt8-creator/research-methodology-`](https://github.com/joselunasrt8-creator/research-methodology-) | Exact commit and repository-local freeze record |
| Structology | [`joselunasrt8-creator/structology`](https://github.com/joselunasrt8-creator/structology) | Exact commit and repository-local freeze record |
| Architectural Boundary Research | [`joselunasrt8-creator/architecturalboundary-research`](https://github.com/joselunasrt8-creator/architecturalboundary-research) | Exact commit and repository-local freeze record |
| Structural Analysis Foundations | [`joselunasrt8-creator/structural-analysis-foundations`](https://github.com/joselunasrt8-creator/structural-analysis-foundations) | Exact commit and repository-local freeze record |
| SYNAPSE | [`joselunasrt8-creator/SYNAPSE`](https://github.com/joselunasrt8-creator/SYNAPSE) | Exact commit and repository-local freeze record |
| ContinuityOS | [`joselunasrt8-creator/ContinuityOS-`](https://github.com/joselunasrt8-creator/ContinuityOS-) | Exact commit and repository-local freeze record |

Listing a repository does not assert readiness, compatibility, or successful execution.

### Exclusion rules

A repository may be excluded only before the cohort manifest is frozen, and only when its repository owner records an immutable rationale and evidence reference. Valid rationales are:

- the repository owner declines or has not authorized participation;
- the repository cannot produce a repository-local freeze record;
- no admissible, versioned instrument applies without changing its semantics;
- the repository or required evidence is unavailable at a stable immutable reference;
- participation would violate a documented repository-local boundary.

An exclusion record must name the repository, responsible owner, rationale, evidence, decision date, effect on comparison coverage, and conditions for inclusion in a later version. Convenience, an unexpected result, or a desire to improve cohort results is not a valid rationale. Exclusion is not `BLOCKED`: exclusion removes the repository from the frozen cohort with rationale; `BLOCKED` is an execution determination for a repository that remains in it. No repository may be added to v1.0 after the cohort manifest is frozen.

## Entry and execution-plan requirements

Before program execution begins, Issue #8 must record the cohort readiness decision and every included repository must provide a repository-owned plan based on the [downstream execution-plan template](downstream-execution-plan-template.md). Each plan must bind:

- repository identity, exact commit SHA, and repository-local freeze reference;
- instrument identity and immutable version or commit;
- methodology identity and immutable version or commit;
- execution inputs and expected output classes;
- environment and dependency identities sufficient to reconstruct the run;
- validation procedure, clean-rerun procedure, and local stopping conditions;
- planned artifact and execution-record locations;
- accountable repository owner and authorized executor.

A branch name such as `main` is context, not an immutable binding. Missing entry evidence prevents execution and must be recorded rather than inferred.

## Immutable execution record

Each included repository must own and preserve one immutable execution record. The program manifest references that record; it does not replace or reinterpret it. At minimum the record must contain:

1. stable execution ID and record-schema version;
2. repository identity, exact commit SHA, and freeze reference;
3. instrument and methodology identities and exact versions;
4. executor, start/end timestamps, and environment/dependency identities;
5. all inputs, including identities, hashes, and provenance;
6. invoked stages, parameters, and commands or procedures;
7. generated and expected-but-missing artifacts;
8. validation procedures and results;
9. artifact hashes and the named hash algorithm;
10. provenance and lineage from inputs through instruments to outputs;
11. every manual intervention, with actor, time, reason, and effect;
12. ambiguities, missing fields, deviations, warnings, and failures;
13. clean-rerun method, result, comparison, and differences;
14. classified defects and improvement candidates with evidence links;
15. final determination, rationale, approver, and decision time;
16. amendments, if any, as append-only superseding records.

Unknown values remain explicitly `UNKNOWN`; inapplicable values use `NOT_APPLICABLE` with a reason. Required fields must never be silently omitted. Human-readable and machine-readable forms, when both exist, must reference the same execution ID and declare which form is authoritative for field-level comparison.

## Valid execution determinations

Exactly one final determination is required for every included repository:

| Determination | Meaning |
| --- | --- |
| `COMPLETE` | All required stages, artifacts, validation, provenance, and applicable clean rerun completed with no material limitation. |
| `COMPLETE_WITH_LIMITATIONS` | The run is valid and reviewable, but explicit limitations reduce coverage or comparability without invalidating the recorded result. |
| `BLOCKED` | A precondition or execution dependency prevented a valid completion. This is an operational state, not a negative research result. |
| `INVALID` | Execution occurred, but a violated binding, corrupted lineage, invalid procedure, or failed validity rule makes its results unusable as a reference execution. |
| `INDETERMINATE` | The evidence is insufficient or ambiguous to decide whether the run is complete, blocked, or invalid without changing the frozen interpretation. |

A research finding, including the absence of an expected phenomenon, is recorded separately from the execution determination. `COMPLETE_WITH_LIMITATIONS` may not be used to conceal a validity failure, and `BLOCKED` may not be presented as evidence against a research claim.

## Artifact, identity, and provenance rules

- Every input, generated artifact, execution record, comparison report, and sealed manifest must have a stable identity, media/format declaration, producing execution ID, and cryptographic hash with algorithm.
- Hash the preserved bytes. If normalization is necessary, retain and hash the source, document the normalization procedure and version, and separately hash the normalized artifact.
- Provenance must trace repository commit and source inputs through the exact instrument/methodology versions and interventions to each output. References must be resolvable without relying on mutable branch state.
- Generated artifacts remain owned by the repository or authority that produced them. A program manifest records references and hashes; it does not promote, copy authority from, or declare artifacts canonical.
- Corrections are append-only: preserve the original, record the reason, create a new identity and hash, and link the superseding record. Never rewrite a sealed record in place.
- Sensitive or non-public evidence may be referenced by access-controlled identity and hash. Access limits and their effect on reviewability must be explicit.

## Clean-rerun expectations

Every applicable execution must be attempted again from a clean checkout or equivalent isolated state at the same repository commit, using the same bound instrument, methodology, inputs, parameters, and declared environment. The rerun must not reuse generated outputs or undeclared mutable caches from the first run.

Record whether artifacts are byte-identical. When byte identity is not an explicit instrument guarantee, compare the documented semantic fields and explain every difference, including timestamps, ordering, generated identifiers, environment drift, or manual intervention. An omitted clean rerun requires an explicit reason and normally limits the result to `COMPLETE_WITH_LIMITATIONS`; if repeatability is necessary to validity, use `BLOCKED`, `INVALID`, or `INDETERMINATE` as supported by evidence.

## Cross-repository comparison

Comparison begins only after every included repository has an immutable record and determination. The report must compare the same declared dimensions without flattening repository-local semantics:

- binding completeness and traceability;
- required, generated, and missing artifact classes;
- validation coverage and result;
- first-run versus clean-rerun equivalence;
- manual intervention count, type, and effect;
- ambiguities, missing fields, warnings, and failure stages;
- determination and limitations;
- repository, instrument, methodology, environment, and coordination classifications;
- recurrent friction and improvement candidates.

For each comparison, cite the execution IDs and artifact hashes, distinguish `NOT_APPLICABLE` from `UNKNOWN` and absent, and state whether values are directly comparable. A recurring observation is evidence for investigation, not a universal invariant, canonical object type, or automatic methodology change.

## Defect and ambiguity classification

Every observed problem must have one primary class and evidence. Do not use classification to assign authority beyond the evidence.

| Class | Test |
| --- | --- |
| `REPOSITORY_DEFECT` | The bound repository violates its own documented contract or cannot supply repository-owned required evidence. |
| `INSTRUMENT_DEFECT` | The frozen instrument implementation or contract fails on admissible input or cannot produce its promised record. |
| `METHODOLOGY_AMBIGUITY` | The frozen methodology permits materially different interpretations or lacks a required decision rule. |
| `EXECUTION_ENVIRONMENT_DEFECT` | The declared environment or dependency realization prevents or changes an otherwise valid run. |
| `COORDINATION_AMBIGUITY` | This program contract, cohort binding, or cross-repository comparison rule is insufficient or contradictory. |

When evidence supports more than one class, create linked records for each asserted class and state the causal relationship; never relabel a repository defect as an instrument defect, or the reverse, to obtain a preferred determination. Unresolved ownership remains an ambiguity with alternatives and evidence needed to resolve it.

Instrument improvements and proposed methodology clarifications are candidates only. They require separate repository-owned review and versioning. No observation automatically enters canon, creates an ontology term or canonical object type, or authorizes a downstream issue or change.

## Freeze, versioning, and required outputs

Before the first run, freeze a Reference Execution manifest as `v1.0.0` containing the included and excluded inventories, exact repository/instrument/methodology bindings, record-schema version, comparison dimensions, expected outputs, accepted limitations, and Issue #8 readiness evidence. The manifest's own identity and hash are part of the sealed artifact set.

During execution, governing changes are prohibited. Evidence-only, append-only corrections that do not change meaning use a patch version and preserve lineage. Any change to the cohort, bindings, required fields, determination semantics, validity rules, or comparison method requires a new minor or major reference-execution version and cannot be folded back into v1.0.0 results. A sealed artifact is never overwritten.

The complete v1.0 output set is:

1. reference execution manifest;
2. immutable execution record for each included repository;
3. cross-repository comparison report;
4. instrument friction register;
5. methodology ambiguity register;
6. instrument improvement register;
7. reference execution conclusion;
8. frozen Reference Execution v1.0 artifact set with manifest and hashes.

The conclusion must state cohort coverage, exclusions, determinations, limitations, and whether internal reproducibility was demonstrated. It must explicitly disclaim external validation and automatic promotion.

## Stopping rule

Stop Reference Execution v1.0 when all included repositories have one sealed determination; every required output is present, identity-bound, hashed, and linked from the frozen manifest; and every discovered ambiguity, defect, limitation, and improvement opportunity has an evidence-linked follow-up record.

Do not continue under v1.0 to fix repositories or instruments, resolve scientific disagreements, add ontology or canonical object types, expand the cohort, promote findings into canon, claim external validation, or perform unrelated cleanup. Those actions require separately authorized downstream work or a later version.
