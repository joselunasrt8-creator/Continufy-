# Canonical Continufy Research & Development Instrument Specification

**Instrument name:** Continufy Research & Development Instrument  
**Instrument version:** `1.0.0`  
**Status:** immutable reference specification for Reference Execution v1.0  
**Canonical owner:** Continufy, as the custodian of this specification only  
**Repository ownership:** each participating repository owns its authorization, local methodology, execution, evidence, outputs, determinations, and any accepted changes.  
**Scope:** one reusable, non-executing instrument contract for obtaining and validating traceable repository findings and candidates from a frozen repository reference.  

This is the authoritative instrument reference for Reference Execution v1.0. It specifies an identical contract that a repository may execute only under that repository's own authority. It neither executes work nor grants authority, legitimacy, permission, canonical status, or acceptance of any output.

## 1. Immutable identity and boundaries

The identity above, including name, version, scope, required stages, required evidence, output semantics, validation rules, and stopping rules, is immutable for every execution bound to `1.0.0`. A binding must use this document's immutable repository commit and content hash; a branch or URL alone is not an immutable identity.

### 1.1 Purpose

The instrument makes repository examination repeatable and reviewable by requiring a fixed path from admissible repository inputs to bounded observations, evidence, findings, candidates, validation, and a preserved freeze record. Its governing purpose is internal reproducibility of the procedure and its artifacts across repositories, without flattening repository-local meaning.

### 1.2 Governing questions

Every execution shall address only these questions, plus repository-local questions that do not alter their meaning:

1. What does the frozen repository reference and its admissible evidence directly support as observations?
2. What evidence can be constructed, traced, and bounded from those observations?
3. What repository findings are supported by that evidence, with what uncertainty and limitations?
4. What reusable Research Methodology or Structology candidates are suggested, while remaining unaccepted candidates?
5. Did the bound instrument produce required, traceable outputs under its declared validation and rerun conditions?
6. What evidence-supported observations could improve a future instrument version?

### 1.3 Explicit non-responsibilities

This instrument does **not**:

- execute against any repository or authorize an execution;
- redefine repository-local methodology, Structology, ownership, scope, or approval;
- accept a Methodology Candidate or Structology Candidate;
- declare scientific truth, authority, legitimacy, permission, compatibility, readiness, or universal validity;
- create runtime systems, orchestration, schemas, validators, automation, synchronization, or authority mechanisms;
- mutate a repository, its evidence, a prior execution, or this version of the instrument; or
- substitute for the Reference Execution v1.0 coordination contract or a repository-local plan.

### 1.4 Compatibility and versioning policy

An execution is compatible with `1.0.0` only when it uses the frozen instrument identity, all mandatory inputs, all applicable stages, all required output classes, and this validation and stopping contract without semantic alteration. Repository-local procedures may add evidence or controls, but may not remove, reinterpret, or weaken required elements.

Version numbers use `MAJOR.MINOR.PATCH`:

- `PATCH` corrects presentation or clarifies wording without changing required meaning, stage behavior, inputs, outputs, validation, or stopping semantics;
- `MINOR` adds backward-compatible optional guidance or output detail without changing prior required semantics; and
- `MAJOR` changes required meaning, admissibility, stages, outputs, validation, rerun, stopping, or compatibility.

No version is retroactive. An execution remains bound to the exact version and immutable source reference recorded at its start.

## 2. Required distinctions

The following distinctions are mandatory and must not be collapsed in an execution record:

```text
Observation                    != Evidence
Evidence                       != Claim
Repository Finding             != Methodology Candidate
Methodology Candidate          != Accepted Methodology
Structology Candidate          != Accepted Structology
Execution                      != Validation
Validation                     != Scientific Truth
Validation                     != Authority
Validation                     != Permission
Instrument Improvement         != Instrument Mutation
Reference Execution            != Universal Validation
```

An **Observation** is a recorded, bounded encounter with an admissible input. **Evidence** is an identity-bound, provenance-traceable artifact or record supporting or limiting a claim. A **Claim** is an interpretation that must name its supporting and contrary evidence. A **Repository Finding** is a claim about the bound repository reference; it is not a general rule. Candidates are proposed transferable material only and have no acceptance effect. Validation concerns conformance, traceability, and reproducibility of this execution; it does not certify truth, authority, or permission.

## 3. Admissible inputs

All inputs must be bound to the execution by stable identity, source/provenance, format, access limitation, hash and named hash algorithm where bytes can be preserved. `UNKNOWN` is allowed only with an explanation; `NOT_APPLICABLE` requires a reason. Required fields may never be silently absent.

### 3.1 Mandatory inputs

| Input | Admissibility requirement |
| --- | --- |
| Repository commit SHA | Exact immutable commit of the examined repository; mutable branch names are contextual only. |
| Repository identity | Canonical repository name and resolvable location, plus repository owner. |
| Canonical entry documents | Repository-designated entry documents that establish scope, structure, and local boundaries at the bound commit. |
| Repository-local methodology | Exact local methodology identity/version or an explicit documented absence and limitation. |
| Frozen contracts | Applicable repository-local contracts and the bound instrument and coordination-contract references. |
| Evidence artifacts | Identified artifacts admissible under repository-local boundaries, including source documents, records, tests, logs, or analysis artifacts used as evidence. |
| Issue inventory | Immutable or time-bounded inventory reference, with collection procedure and access limits. |
| Pull-request inventory | Immutable or time-bounded inventory reference, with collection procedure and access limits. |
| Known limitations | Repository-declared and execution-discovered limitations known at start. |
| Declared exclusions | Explicit excluded paths, artifacts, questions, and rationale. |

### 3.2 Optional inputs

Optional inputs include release/tag context, environment manifests, dependency locks, prior execution records, external review references, supplementary datasets, and repository-owner annotations. They are admissible only when identity-bound and must not silently replace a mandatory input. Their absence is not itself failure unless a repository-local contract makes them required.

An inaccessible mandatory input produces `BLOCKED`, `INCOMPLETE`, or `INDETERMINATE` as supported by the record; it must not be reconstructed by assumption. Sensitive evidence may be referenced through access-controlled identity and hash, with the review limitation stated.

## 4. Canonical execution pipeline

An execution uses this sequence and preserves an event record for each invoked stage:

```text
Repository
  -> Repository Boundary Review
  -> Observation Collection
  -> Classification
  -> Evidence Construction
  -> Repository Findings
  -> Methodology Candidates
  -> Structology Candidates
  -> Instrument Findings
  -> Validation
  -> Freeze Record
  -> Calibration Observations
```

In the table below, “prior outputs” means the preserved outputs from preceding applicable stages. A stage may be `NOT_APPLICABLE` only where its row permits no result; it still requires a recorded rationale. A failed, blocked, or stopped stage cannot transition as if it succeeded.

| Stage | Purpose; inputs | Outputs and required evidence | Transition condition | Failure, blocked, and stopping conditions |
| --- | --- | --- | --- | --- |
| Repository | Bind the subject using repository identity, commit SHA, and owner. | Repository binding record; commit-resolution evidence and hash/reference. | Exact identity and commit resolve. | Failure: binding mismatch. Blocked: commit/identity unavailable. Stop if no immutable subject can be bound. |
| Repository Boundary Review | Establish admissibility from entry documents, local methodology, frozen contracts, known limitations, and exclusions. | Boundary record; cited entry documents, inclusion/exclusion rationale, access limits. | Mandatory scope and exclusions are explicit. | Failure: work uses inadmissible input. Blocked: local boundary cannot be determined. Stop if admissibility cannot be established. |
| Observation Collection | Record bounded observations from admissible evidence artifacts, issue inventory, and PR inventory. | Observation records; source identities, collection method/time, and direct references. | Each observation is source-bound and non-interpretive. | Failure: observation lacks source or exceeds boundary. Blocked: mandatory source inaccessible. Stop when collection cannot proceed without guessing. |
| Classification | Classify observations, evidence status, uncertainty, limitations, and possible defect/ambiguity class without assigning authority. | Classification record; rules used, alternatives, and uncertainty. | Every classification points to observation(s). | Failure: unsupported or collapsed classification. Blocked: applicable rule is contradictory. Stop if ambiguity prevents bounded classification. |
| Evidence Construction | Produce traceable evidence from observations and permitted transformations. | Evidence set; parent observations, transformation/procedure, hashes, provenance, and limitations. | Each evidence item is identity- and lineage-bound. | Failure: broken lineage or altered source without disclosure. Blocked: required transformation cannot be reproduced. Stop if evidence cannot be constructed validly. |
| Repository Findings | State repository-specific claims supported and limited by the evidence set. | Repository Findings output; claim-to-evidence map, uncertainty, contrary/missing evidence, limitations. | Findings do not generalize beyond bound repository reference. | Failure: claim lacks evidence or overstates scope. Blocked: evidence is insufficient for the required finding. Stop with no finding rather than an inferred one. |
| Methodology Candidates | Extract possible reusable methodology implications from findings, without accepting them. | Research Methodology Candidates output; source findings, candidate statement, uncertainty, non-acceptance label. | Candidate remains distinct from finding and accepted methodology. | Failure: candidate represented as accepted. Blocked: transfer implication cannot be bounded. Stop this stage with `NOT_APPLICABLE` if none is supported. |
| Structology Candidates | Extract possible Structology implications from findings, without accepting them. | Structology Candidates output with the same traceability and non-acceptance label. | Candidate remains distinct from finding and accepted Structology. | Failure: candidate represented as accepted. Blocked: relation to Structology cannot be bounded. Stop this stage with `NOT_APPLICABLE` if none is supported. |
| Instrument Findings | Record observations about the instrument’s operation, friction, ambiguity, or defect. | Instrument Improvement Observations; affected stage, evidence, impact, uncertainty, and future-version-only status. | Observation is separated from any instrument change. | Failure: a finding silently changes this instrument. Blocked: insufficient evidence to locate the issue. Stop with `NOT_APPLICABLE` if none is supported. |
| Validation | Test required bindings, evidence, outputs, provenance, and applicable rerun results. | Validation Record; criteria, evidence, procedures, outcomes, failures, and limitations. | Every applicable criterion has a result or explicit limitation. | Failure: validation criterion fails. Blocked: required validation evidence unavailable. Stop if validity cannot be decided without changing frozen meaning. |
| Freeze Record | Preserve the execution result append-only after validation. | Freeze Record and Execution Metadata; final outcome, hashes, lineage, timestamps, and supersession links. | Required artifacts are present or explicitly accounted for and stopping outcome is recorded. | Failure: record is mutable, incomplete without marking, or unlinked. Blocked: preservation facility unavailable. Stop without claiming a sealed execution. |
| Calibration Observations | Preserve friction and improvement observations after freeze without modifying the execution or instrument. | Calibration Observations; evidence-linked candidates and follow-up references. | Observations are append-only and non-mutating. | Failure: calibration rewrites frozen content. Blocked: evidence cannot be preserved. Stop after recording the limitation. |

## 5. Canonical outputs

Every output has a stable output ID, producing execution ID, instrument version/reference, repository identity/commit, creation time, provenance parents, format/location, hash and algorithm, uncertainty, limitations, and `supersedes`/`superseded_by` field. An output may be absent only when explicitly `NOT_APPLICABLE` or when the stop record explains its absence. Corrections create a new identity and append-only supersession link; they never overwrite output bytes.

| Output | Required fields beyond common fields | Supersession behavior |
| --- | --- | --- |
| Repository Findings | Finding ID; bounded claim; supporting and contrary/missing evidence IDs; observation IDs; classification; scope; uncertainty; limitations. | A correction creates a new finding linked to the prior finding; the prior finding remains available. |
| Research Methodology Candidates | Candidate ID; candidate statement; source finding IDs; transfer assumptions; uncertainty; limitations; explicit `NOT_ACCEPTED` status. | New candidate or revised wording supersedes only its own candidate record, never methodology. |
| Structology Candidates | Candidate ID; candidate statement; source finding IDs; stated structural relation; uncertainty; limitations; explicit `NOT_ACCEPTED` status. | New candidate or revision supersedes only its own candidate record, never Structology. |
| Instrument Improvement Observations | Observation ID; affected instrument clause/stage; evidence IDs; observed effect; proposed future consideration; uncertainty; limitations; explicit `NO_MUTATION_TO_BOUND_VERSION`. | Later observations may supersede a prior observation’s interpretation, not the frozen instrument. |
| Freeze Record | Freeze ID; final stopping outcome; complete output inventory; hashes; validation ID; approvals if locally required; preservation location; supersession chain. | A sealed record is immutable; a correction is a new linked freeze record. |
| Execution Metadata | Execution ID; executor; start/end time; environment/dependency identities; procedures/parameters; intervention log; input inventory; repository and instrument bindings. | An amended metadata record is append-only and preserves the original metadata. |
| Validation Record | Validation ID; criteria; required evidence; procedure; outcome per criterion; failures; limitations; validator identity/process; rerun comparison. | Later validation does not erase earlier results; it creates a linked validation record. |
| Calibration Observations | Calibration ID; source execution/freeze ID; friction or ambiguity; evidence; impact; uncertainty; limitation; later-version follow-up reference. | A later assessment may supersede the observation’s assessment but cannot alter the frozen execution. |

## 6. Validation contract

Validation requires evidence that: (1) repository and instrument bindings resolve to their frozen identities; (2) mandatory inputs and boundary decisions are recorded; (3) each applicable stage has its required evidence and a valid transition; (4) output IDs, hashes, provenance, uncertainty, and limitations are present; (5) claims do not exceed their evidence; (6) candidate and authority distinctions are preserved; (7) stopping outcome is evidence-supported; and (8) a clean rerun is attempted where applicable or its omission is explicitly limited.

Validation criteria are **binding integrity**, **input completeness**, **boundary adherence**, **stage conformance**, **evidence lineage**, **output completeness**, **distinction preservation**, **rerun conformance**, and **freeze preservation**. Each criterion has one outcome: `PASS`, `FAIL`, `LIMITED`, `BLOCKED`, `NOT_APPLICABLE`, or `INDETERMINATE`, with evidence and rationale.

A validation failure is a `FAIL` criterion, broken binding/lineage, unrecorded mandatory omission, unsupported claim, invalid stage transition, or overwritten history. Validation limitations—such as access restrictions, nondeterministic artifacts, unavailable clean isolation, or incomplete inventories—must state affected criteria and impact. A validation result is not execution itself, not scientific truth, not authority, and not permission.

## 7. Clean rerun contract

A legitimate rerun is a new execution with a new rerun ID, created from a clean checkout or equivalent isolated state at the same repository commit and using the same frozen instrument version/reference, mandatory inputs, declared procedures, parameters, and applicable environment/dependency identities. It must not reuse generated outputs or undeclared mutable caches from the earlier execution.

The rerun record must preserve isolation evidence, binding replay evidence, commands/procedures, environment differences, generated artifact hashes, validation results, and comparison with the original. Compare byte identity when the instrument explicitly guarantees it; otherwise compare declared semantic fields and explain every difference, including time, ordering, generated IDs, environment drift, or intervention. A legitimate rerun never overwrites the original: both execution IDs, artifacts, comparison, and historical record remain preserved. A rerun that changes a frozen binding is a new execution, not a rerun.

## 8. Amendment and supersession rules

An instrument amendment follows this append-only sequence: **proposal** with evidence and affected clauses; **review** against scope, compatibility, and prior executions; **acceptance** by the canonical owner through a separately recorded decision; **version creation** with immutable identity and changelog; and **historical preservation** of all proposals, reviews, decisions, and prior versions.

No execution may silently mutate an instrument. Calibration and Instrument Improvement Observations are inputs to a possible proposal only. A new version supersedes a prior version only when its published immutable specification declares that relationship and its compatibility impact. It must preserve prior versions, explain changes, state compatibility and migration expectations, and never reinterpret prior output. Older executions remain bound to their original instrument version. Migration creates a new execution or an explicit comparison record; it does not convert historical execution records in place.

## 9. Stopping rules and outcomes

Every stopped execution preserves a stopping record with execution ID, stage reached, time, responsible actor/process, evidence IDs, unmet condition, affected outputs, uncertainty, limitations, and next evidence needed. Exactly one outcome applies:

| Outcome | Meaning and required preservation |
| --- | --- |
| `NORMAL_COMPLETION` | All applicable stages complete; required outputs are frozen; validation is recorded; applicable rerun comparison is complete or explicitly limited. Preserve final inventory and evidence. |
| `BLOCKED_EXECUTION` | An external prerequisite, required input, access boundary, or preservation dependency prevents valid continuation. Preserve blocker, owner/boundary, attempted work, and evidence needed to unblock. |
| `INCOMPLETE_EXECUTION` | Work stopped before required stages/outputs completed for a non-blocker reason. Preserve missing work, stage state, and reason; do not present results as complete. |
| `INDETERMINATE_EXECUTION` | Evidence is insufficient or contradictory to decide a required interpretation or validation result without changing frozen meaning. Preserve alternatives and evidence needed to decide. |
| `FAILURE` | A procedure, binding, validation criterion, lineage, or preservation rule failed. Preserve failure evidence, impact, and whether earlier outputs are usable only as unvalidated artifacts. |
| `CANCELLATION` | An authorized repository-local actor ended the execution. Preserve cancellation source, time, completed stages, and artifact status. |
| `DEFERRED_EXECUTION` | Execution is intentionally postponed before or during work. Preserve deferment reason, frozen state, conditions for resumption, and absence of completion claim. |

These instrument outcomes may be mapped into a program-level determination only by the governing coordination contract; they do not themselves create authority or a research conclusion.

## 10. Reference Execution v1.0 use

For Reference Execution v1.0, a repository-local plan binds this exact instrument version before work begins and records all local authorization separately. The coordination contract may add cohort-level records and comparison requirements, but cannot mutate this bound instrument during an execution. Identical instrument stages and requirements enable comparison; repository findings, methodology, Structology, authority, and acceptance remain local and are not made universal by repeated execution.
