# Repository-Local Reference Execution v1.0 Plan and Record

Use one copy of this template in each participating repository only after that repository authorizes the work. The repository owns the completed plan, execution, artifacts, and determination. Completing this template does not transfer authority to Continufy or authorize execution by itself.

Governing program contract: [Reference Execution v1.0 Coordination Contract](coordination-contract.md)

## 1. Plan identity and authority

| Field | Value |
| --- | --- |
| Plan ID | `PENDING` |
| Plan version | `1.0.0` |
| Repository name and URL | `PENDING` |
| Repository owner | `PENDING` |
| Authorized executor | `PENDING` |
| Repository-local authorization issue/record | `PENDING` |
| Repository-local freeze issue/record | `PENDING` |
| Issue #8 readiness-manifest reference | `PENDING` |
| Planned execution window | `PENDING` |

Authority statement:

> This execution is authorized and determined by the repository named above. Program coordination, an instrument result, or a completed artifact does not grant authority, canonical status, promotion, or permission to execute any other action.

## 2. Frozen bindings

| Binding | Immutable identity | Evidence or hash |
| --- | --- | --- |
| Repository commit SHA | `PENDING` | `PENDING` |
| Reference branch/tag (context only) | `PENDING` | `PENDING` |
| Instrument name and version/commit | `PENDING` | `PENDING` |
| Methodology name and version/commit | `PENDING` | `PENDING` |
| Record-schema version | `PENDING` | `PENDING` |
| Environment image/platform | `PENDING` | `PENDING` |
| Dependency lock(s) | `PENDING` | `PENDING` |

Explain how each immutable reference can be resolved. Do not use a mutable branch alone as a binding.

## 3. Scope and admissibility

- Repository-local execution subject: `PENDING`
- Governing questions: `PENDING`
- Included paths/evidence classes: `PENDING`
- Excluded paths/evidence classes and rationale: `PENDING`
- Expected output classes: `PENDING`
- Repository-local non-goals and boundaries: `PENDING`
- Why the frozen instrument accepts this input without semantic change: `PENDING`
- Local stopping conditions: `PENDING`

## 4. Input inventory

| Input ID | Description | Source/provenance | Format | Hash algorithm and value | Access limits |
| --- | --- | --- | --- | --- | --- |
| `PENDING` | `PENDING` | `PENDING` | `PENDING` | `PENDING` | `PENDING` |

Use `UNKNOWN` for an unknown value and `NOT_APPLICABLE` with a reason when a field does not apply.

## 5. Procedure and validation plan

1. Clean checkout/isolation procedure: `PENDING`
2. Environment realization procedure: `PENDING`
3. Exact stages, commands, parameters, or human procedures: `PENDING`
4. Expected artifacts and planned locations: `PENDING`
5. Validation rules and expected results: `PENDING`
6. Failure capture procedure: `PENDING`
7. Manual intervention policy: `PENDING`
8. Clean-rerun procedure: `PENDING`
9. First-run/rerun comparison rules, including allowed nondeterminism: `PENDING`

No planned step may mutate the frozen repository commit, instrument, methodology, or prior output. Calibrations discovered during the run become observations or later-version candidates.

## 6. Execution event log

| Time | Stage | Actor/tool and version | Inputs | Action | Output/event ID | Result |
| --- | --- | --- | --- | --- | --- | --- |
| `PENDING` | `PENDING` | `PENDING` | `PENDING` | `PENDING` | `PENDING` | `PENDING` |

### Manual interventions

| Time | Actor | Trigger | Intervention | Reason | Effect on validity/reproducibility |
| --- | --- | --- | --- | --- | --- |
| `NOT_APPLICABLE` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | No intervention | None |

## 7. Artifact and validation record

| Artifact ID | Expected/generated/missing | Path or resolvable reference | Format | Producing stage | Hash algorithm and value | Provenance parent(s) | Validation result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PENDING` | `PENDING` | `PENDING` | `PENDING` | `PENDING` | `PENDING` | `PENDING` | `PENDING` |

- Validation evidence: `PENDING`
- Missing fields/artifacts: `PENDING`
- Warnings and execution failures: `PENDING`
- Provenance/lineage summary: `PENDING`

## 8. Clean rerun

| Field | Value |
| --- | --- |
| Rerun execution ID | `PENDING` |
| Isolation evidence | `PENDING` |
| Reused frozen bindings | `PENDING` |
| Start/end timestamps | `PENDING` |
| Byte-identical artifacts | `PENDING` |
| Semantic comparison result | `PENDING` |
| Explained differences | `PENDING` |
| Undeclared cache/output reuse check | `PENDING` |
| Rerun limitation or reason not attempted | `PENDING` |

## 9. Observations, defects, and ambiguities

Keep repository results distinct from execution validity. Internal reproducibility is not external validation, and a blocked execution is not a negative research result.

| Observation ID | Evidence | Primary class | Description | Alternatives/uncertainty | Execution effect | Follow-up reference |
| --- | --- | --- | --- | --- | --- | --- |
| `PENDING` | `PENDING` | `REPOSITORY_DEFECT` / `INSTRUMENT_DEFECT` / `METHODOLOGY_AMBIGUITY` / `EXECUTION_ENVIRONMENT_DEFECT` / `COORDINATION_AMBIGUITY` | `PENDING` | `PENDING` | `PENDING` | `PENDING` |

Create linked records rather than collapsing multiple supported classes. Candidate improvements and concepts are not accepted methodology, ontology, canonical object types, or canon.

## 10. Final determination

Select exactly one:

- [ ] `COMPLETE`
- [ ] `COMPLETE_WITH_LIMITATIONS`
- [ ] `BLOCKED`
- [ ] `INVALID`
- [ ] `INDETERMINATE`

| Field | Value |
| --- | --- |
| Determination rationale | `PENDING` |
| Supporting execution/artifact IDs | `PENDING` |
| Limitations | `PENDING` |
| Evidence that would change the determination | `PENDING` |
| Repository approver | `PENDING` |
| Decision timestamp | `PENDING` |

Research findings, including negative or null findings: `PENDING`

The determination describes execution validity and completeness only. `BLOCKED` is not a negative research result, and no determination automatically promotes an output or authorizes a repository change.

## 11. Seal and program handoff

| Field | Value |
| --- | --- |
| Immutable execution-record identity | `PENDING` |
| Record hash and algorithm | `PENDING` |
| Artifact-manifest identity and hash | `PENDING` |
| Supersedes/superseded by | `NOT_APPLICABLE` |
| Program-manifest reference | `PENDING` |
| Comparison-report handoff fields | `PENDING` |
| Open evidence-linked follow-ups | `PENDING` |

Seal only after all required fields are present or explicitly marked `UNKNOWN`/`NOT_APPLICABLE`, all artifacts are identity-bound and hashed, the final determination is approved locally, and corrections use append-only supersession. The handoff supplies evidence to program comparison; it does not surrender repository ownership or claim external validation.
