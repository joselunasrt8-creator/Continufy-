# Continufy SOP-to-Executable Governance Contract

- **Contract ID:** `continufy-sop-governance`
- **Contract version:** `1.0.0`
- **Status:** canonical contract for bounded reference execution
- **Owner:** Continufy, as custodian of this contract only
- **Scope:** the smallest domain-neutral representation needed to bind a versioned SOP to evidence, decision rules, independently sourced authority, execution eligibility, one exact action, proof, outcome, reconciliation, and a separately governed revision candidate.
**Non-scope:** this document is not a runtime, workflow engine, product, SaaS layer, autonomous agent, policy generator, trucking architecture, finance deployment, or claim of universality.

This document and the adjacent schemas are normative. Examples and the validator are conformance evidence, not an execution system.

## 1. Governing transformation and distinctions

```text
SOP
→ Required Inputs
→ Evidence Requirements
→ Decision Rules / Predicates
→ Authority Requirements
→ Stop / Escalation Conditions
→ Execution Eligibility
→ Exact Action
→ Proof
→ Outcome
→ Revision Candidate
```

No arrow grants the next state automatically. Every transition must satisfy the contract for the bound SOP version and execution instance.

```text
Instruction ≠ Authority
Evidence ≠ Decision
Decision ≠ Permission
Validation ≠ Execution
Capability ≠ Permission
Proposed Action ≠ Executed Action
Outcome ≠ Automatic SOP Revision
```

An **instruction** specifies required behavior. **Evidence** is a provenance-bound observation offered to satisfy an evidence requirement. A **predicate evaluation** applies a named rule version to cited evidence. A **decision candidate** is a proposed disposition. **Authority** is an independently issued, scoped, current binding from an authority owner. **Validation** determines whether the complete legitimacy conjunction holds for one exact action. **Execution eligibility** is the resulting permission state, not execution. **Execution** is an attempt to perform the exact eligible action. **Proof** is independently inspectable evidence of what execution did. An **outcome** is a later measured consequence. A **revision candidate** is a non-operative proposal for a future SOP version.

## 2. Canonical SOP definition object

The machine contract is [`sop-definition.schema.json`](sop-definition.schema.json). Its required top-level fields are:

| Field | Contract meaning |
| --- | --- |
| `contract_version`, `object_type` | Bind the object to this contract and to `SOP_DEFINITION`. |
| `sop_id`, `version`, `definition_digest` | Stable SOP identity, immutable semantic version, and canonical content identity. |
| `immutable` | Must be `true`; a changed definition requires a new version and digest. |
| `owner` | Accountable owner of the instruction; ownership alone does not supply runtime authority. |
| `purpose`, `scope`, `trigger` | Bounded intent, included/excluded domain, and initiation condition. |
| `input_object_types` | Named, typed inputs and their schema identities. |
| `required_evidence` | Evidence class, source class, freshness, provenance, contradiction behavior, and point of use. |
| `decision_rules` | Versioned predicates, referenced evidence, and true/false/unknown dispositions. |
| `authority_requirements` | Required authority type, issuer/owner, scope, action type, validity, and registry binding. |
| `stop_conditions` | Conditions producing fail-closed `NULL`; no action is eligible. |
| `escalation_conditions` | Conditions producing `ESCALATE`, with a named destination and required resolution evidence. |
| `allowed_actions`, `prohibited_actions` | Closed allowlist plus explicit denials. Silence is not permission. |
| `execution_preconditions` | Preconditions that must be evidenced immediately before eligibility validation. |
| `proof_requirements` | Required proof types, action binding, provenance, and retention. |
| `outcome_measurements` | Measurements that may be recorded after execution; missingness remains explicit. |
| `revision_policy` | Separate review, authority, evidence, version, and effective-date requirements. |
| `effective_from`, `supersedes` | Version effectiveness and optional direct predecessor identity/digest. |
| `provenance` | Authoring/review source artifacts and, for a superseding version, revision approval. |

Arrays that express requirements must be non-empty. Every requirement, rule, condition, and action has a stable local ID. References are by those IDs, not by display text. A definition is valid only when:

1. its `(sop_id, version, definition_digest)` is immutable and unique;
2. every rule and precondition refers to declared input/evidence IDs;
3. allowed and prohibited action types do not overlap;
4. required authority covers each allowed mutation-capable action;
5. `supersedes`, when present, names the same `sop_id`, an earlier version, its digest, and an approved revision record; and
6. no outcome or revision candidate is embedded as an operative change to this definition.

The digest is `sha256:<64 lowercase hexadecimal characters>` over the repository's declared canonical JSON serialization. The schemas constrain digest shape; the repository that freezes an object must declare and apply its serialization procedure. This contract does not pretend that an illustrative digest proves fixture bytes.

## 3. SOP execution-instance object

The machine contract is [`sop-execution-instance.schema.json`](sop-execution-instance.schema.json). An instance is bounded to one SOP definition and one proposed exact action:

```text
SOP Definition
→ Execution Context
→ Observed Inputs
→ Evidence Set
→ Predicate Evaluation
→ Decision Candidate
→ Authority Binding
→ Eligibility Validation
→ VALID | NULL | ESCALATE
→ Exact Execution, only when VALID
→ Proof
→ Outcome
→ Reconciliation
```

Required identities are preserved as follows:

| Required identity | Instance location |
| --- | --- |
| SOP version | `sop_binding.sop_id`, `version`, `definition_digest` |
| input/context | `execution_context.context_id/context_digest`; each `observed_inputs[].input_id/input_digest` |
| evidence and freshness | each `evidence_set[]` identity/digest, `as_of`, `captured_at`, `freshness_status`, source, and provenance |
| predicate/rule version | each `predicate_evaluations[].rule_id/rule_version` |
| decision candidate | `decision_candidate.decision_id/decision_digest` |
| authority object | `authority_binding.authority_id/authority_digest`, issuer, scope, validity, registry identity |
| validation result | `eligibility_validation.validation_id/validation_digest/result` and legitimacy facts |
| approved execution object | `approved_execution_object.action_id/action_digest` and bound SOP/action details |
| executed object | `execution.executed_object.action_id/action_digest`, when execution occurs |
| proof | `proof.proof_id/proof_digest/action_digest`, when required |
| outcome | `outcome.outcome_id/outcome_digest/status` |
| reconciliation | `reconciliation.status`, exact-object check, replay check, and exception state |

The approved execution object includes the action type, target digest, parameters digest, idempotency key, and SOP binding. If execution occurs:

```text
eligibility_validation.validated_action_digest
  = approved_execution_object.action_digest
  = execution.executed_object.action_digest
  = proof.action_digest
```

The executed action ID, type, target digest, parameters digest, idempotency key, SOP ID, and SOP version must also equal their approved values. Validation of a similar object, an earlier object, or a mutable pointer is not sufficient.

## 4. Lifecycle and state semantics

The lifecycle is append-only. A state may advance only through its named predecessor; a failure is recorded rather than rewritten.

```text
BOUND
→ INPUTS_OBSERVED
→ EVIDENCE_ASSEMBLED
→ PREDICATES_EVALUATED
→ DECISION_PROPOSED
→ AUTHORITY_BOUND
→ ELIGIBILITY_VALIDATED
   ├─ NULL ───────────────→ RECONCILED_WITHOUT_EXECUTION
   ├─ ESCALATE ───────────→ RECONCILED_WITHOUT_EXECUTION
   └─ VALID → EXECUTED → PROOF_RECORDED → OUTCOME_RECORDED → RECONCILED
```

- `VALID` means every required legitimacy fact is true for the exact approved object at validation time. It is neither execution nor proof.
- `NULL` means no execution eligibility exists. Missing, false, contradictory, unknown, expired, drifted, replayed, or mismatched required facts cannot be coerced to true.
- `ESCALATE` means eligibility is withheld and a named authority/reviewer must resolve the condition with new, identity-bound evidence. An unresolved escalation never executes. If resolution changes the proposed action, SOP version, or bound evidence, a new validation and normally a new instance are required.
- `EXECUTED` means an execution attempt was recorded for the exact approved object. A failed attempt is still not a successful action.
- `PROOF_RECORDED` does not imply the desired outcome.
- `OUTCOME_RECORDED` allows `AVAILABLE`, `PENDING`, or `UNAVAILABLE`; unavailable outcome is not invented.
- `RECONCILED` compares approved, executed, proved, and observed records and preserves mismatches or unresolved exceptions.

An instance contains append-only `lifecycle_history`. `execution.status = EXECUTED` is permitted only after `VALID`. For `NULL` or `ESCALATE`, `execution.status` must remain `NOT_ATTEMPTED`, `executed_object` and `proof` must be null, and reconciliation must close without execution or remain explicitly unresolved.

## 5. Authority and non-authority responsibilities

| Layer or role | May produce | Must not produce or infer |
| --- | --- | --- |
| LLM Layer | Reasoning, synthesis, candidate outputs, candidate decisions | Authority, authority bindings, legitimacy facts, execution eligibility, proof of execution |
| MindShift | Observations, context, candidate abstractions, candidate intent | Authority or permission |
| Methodology / research instruments | Evidence requirements, evaluation procedures, uncertainty treatment, calibration/revision evidence | Silent authorization, execution eligibility, policy mutation |
| SYNAPSE | Deterministic structural evidence with identity and provenance | Authority, permission, execution eligibility |
| SOP owner | Instruction, policy ownership, revision proposals | Runtime permission merely by authoring the instruction, unless separately named and bound as authority owner |
| Decision owner | Rule ownership and decision candidate | Permission unless a distinct valid authority binding covers the exact action |
| Authority owner/issuer | Scoped, expiring authority object under its own governance | Evidence fabrication, predicate truth, automatic execution |
| Executor | Attempt the exact eligible action | Change action/parameters/target after validation or self-authorize |
| Outcome observer | Record later measurements and missingness | Rewrite proof, adjudicate authority, mutate the SOP |
| Revision authority | Approve a new immutable SOP version after review | Rewrite a prior version or allow an outcome to mutate policy directly |

ContinuityOS owns the legitimacy boundary for mutation-capable action:

```text
Intent Candidate
→ Continuity
→ Authority
→ ATAO
→ AEO
→ Validation
→ Execution Eligibility
→ Execution Boundary
→ Proof
→ Registry
→ Reconciliation
```

This contract records identity-bound satisfaction references for Continuity, Authority, ATAO, and AEO but does not redefine those ContinuityOS concepts. `eligibility_validation.result` may be `VALID` only when ContinuityOS attests every required conjunction member for the same SOP binding and action digest:

```text
continuity_satisfied
∧ authority_satisfied
∧ atao_satisfied
∧ aeo_satisfied
∧ evidence_satisfied
∧ predicates_satisfied
∧ preconditions_satisfied
∧ exact_object_bound
∧ replay_absent
∧ sop_version_current
= true
```

Otherwise eligibility is `NULL`, except an SOP-declared escalation condition may produce `ESCALATE`. Neither an LLM, MindShift, an instrument, SYNAPSE, nor this contract may assert that conjunction on ContinuityOS's behalf.

## 6. Stop and escalation behavior

Stop and escalation are policy-declared, evidence-producing outcomes, not exceptions around the contract. Evaluation order is: bind version; detect replay/drift; assemble required evidence; assess freshness/contradiction; evaluate predicates; bind authority; evaluate declared stop conditions; evaluate declared escalation conditions; validate the exact object.

| Failure case | Required bounded behavior | Eligibility |
| --- | --- | --- |
| Missing evidence | Record missing requirement IDs; apply declared stop/escalation behavior; never synthesize the fact. | `NULL` or `ESCALATE` |
| Stale evidence | Mark `STALE`, record age and freshness rule, and reacquire or escalate. | `NULL` or `ESCALATE` |
| Contradictory evidence | Preserve all objects; do not silently prefer one; route per declared contradiction policy. | `NULL` or `ESCALATE` |
| Unknown rule | Record rule/version/observability as unknown; do not reverse-engineer it into asserted policy. | `NULL` or `ESCALATE` |
| Insufficient authority | Record unmet authority requirement. | `NULL` |
| Expired authority | Preserve the expired binding and require a new authority object. | `NULL` |
| Replay | Detect prior consumption of the idempotency key/action digest and record the prior reference. | `NULL` |
| Altered action after validation | Record exact-object mismatch; do not execute or represent the altered object as approved. | `NULL` |
| SOP version drift | Bind the observed current version and stop; a new validation/instance is required. | `NULL` |
| Unresolved exception | Preserve the exception and escalation route; do not apply a default success. | `ESCALATE` |
| Unsupported domain mapping | Record unsupported fields/concepts and transfer classification; do not weaken the core. | `NULL` or no instance |
| Unavailable outcome | Record `UNAVAILABLE`, reason, and observation attempt; do not infer success/failure. | Execution validity unchanged; revision evidence limited |
| Attempted self-modification | Preserve the attempt as a prohibited action/security event; require separate revision governance. | `NULL` |

No failure path transitions into successful execution without new admissible evidence, a current authority binding, and a fresh exact-object validation. When an escalation is resolved, the resolution object is evidence, not authority unless independently issued as a valid authority object.

## 7. Proof, outcome, and reconciliation

Proof is defined before execution by `proof_requirements`. Each required proof must name its proof type, producing source, required action binding, retention rule, and whether independent verification is required. A proof object must include identity/digest, the exact action digest, observation time, provenance, and cited receipt/evidence identities. Logs without target/action binding are not sufficient proof.

Proof establishes only what its procedure can support. It does not establish policy correctness, desired economic outcome, or SOP fitness. A successful execution lacking required proof reconciles as `PROOF_INCOMPLETE`, not as fully reconciled success.

Outcomes are append-only measurement records against declared `outcome_measurements`. They distinguish observed values, estimates, pending measurement, and unavailable measurement. An outcome must identify the execution/proof it follows, measurement definition/version, provenance, observation time, uncertainty, and limitations. Outcome absence cannot be converted into a favorable value.

Reconciliation records exactly one of `MATCHED`, `MISMATCH`, `PROOF_INCOMPLETE`, `OUTCOME_PENDING`, `CLOSED_WITHOUT_EXECUTION`, or `UNRESOLVED`. It compares identity equality, replay state, proof completeness, exception state, and outcome availability. Reconciliation never changes the historical objects it compares.

## 8. SOP versioning, supersession, and revision boundary

An SOP definition version is immutable. Corrections that change semantic fields, required evidence, rules, authority, stop/escalation behavior, actions, proof, outcome measures, or revision policy require a new semantic version and digest. Prior versions remain resolvable.

```text
Observed Outcome
→ Revision Candidate
→ Review / Authority
→ Approved New SOP Version
```

Never:

```text
Outcome
→ Automatic Governance Mutation
```

A revision candidate is non-operative. Approval requires the `revision_policy` of the current SOP, cited supporting and contrary evidence, a named reviewer, a valid revision-authority object, an approval time, the new version/digest, and an effective date. The approved new definition must preserve:

- the complete prior version and digest through `supersedes`;
- the reason for change;
- supporting evidence identities and limitations;
- revision authority identity/digest and scope;
- approval and effective dates; and
- an unbroken supersession lineage.

Executions already bound to an older version retain that binding. Version change never retroactively validates, invalidates, or rewrites them. A self-modification attempt or an `APPROVED` revision without authority is invalid.

## 9. Trucking reference mapping

The first empirical domain is `joselunasrt8-creator/trucking-software-research` at commit `546a797aa5784cc65a2395bb7249f7cfbf2ecc81`. This mapping reuses, and does not modify or replace, its `qualification-attempt-v1` research shape:

```text
authoritative_state
→ platform_state
→ policy + rule
→ decision
→ later_evidence
→ economic_outcome
→ reviewer_assessments
→ adjudication
```

That source instrument explicitly says it is a research measurement instrument, not a production decision contract. The SOP mapping treats its captured records as empirical evidence inputs to a later authorized reference execution; it does not turn the instrument into a trucking product or invent a new trucking architecture.

### Bounded carrier-qualification SOP

**Instruction:** before accepting a specifically identified carrier for a specifically identified load, validate required authoritative carrier state, represented broker/platform state, policy and rule versions, evidence freshness, load/equipment/insurance/compliance predicates, and a separate authority binding. If required evidence is missing, stale, contradictory, unknown, or policy-invalid, stop or escalate rather than infer eligibility.

| Domain-neutral field | Trucking binding |
| --- | --- |
| Inputs | Carrier identity digest, load/offer digest, broker/platform context, requested equipment/service, qualification time. |
| Authoritative evidence | Timestamped FMCSA/regulator evidence plus any separately required insurer or other named authoritative source; each retains source locator, retrieval/as-of times, and artifact hash. |
| Represented evidence | What the broker/platform displayed or used at T0, preserved separately even when it conflicts with authoritative state. |
| Freshness | Each evidence requirement declares maximum age and point of use; the reference execution records `FRESH`, `STALE`, or `UNKNOWN`. |
| Predicates | Versioned regulatory, broker-policy, platform-requirement, and risk-signal predicates remain distinct; load-specific equipment, insurance, compliance, and observed qualification rules are cited rather than guessed. |
| Decision owner | The named owner of the applicable broker/platform qualification rule; its candidate disposition is `ALLOW`, `DELAY`, `REVIEW`, or `REJECT`. |
| Authority owner | The separately named broker/shipper or other organization authorized to accept the carrier for the exact load under its governance. Decision ownership alone is not authority. |
| Stop conditions | Missing carrier/load identity; missing/stale required evidence; inapplicable/failed known hard predicate; expired/insufficient authority; replay; SOP drift; exact-action mismatch. |
| Escalation conditions | Contradictory authoritative/represented evidence, partially visible or proprietary rule, unresolved exception, or a policy-declared human review case. |
| Execution eligibility | `ALLOW` is only a decision candidate. Eligibility is `VALID` only after the complete legitimacy conjunction for the exact acceptance object; `DELAY`, `REVIEW`, and unresolved conditions are not executable acceptance. `REJECT` yields no acceptance action. |
| Exact permitted action | One `ACCEPT_CARRIER_FOR_LOAD` object binding carrier digest, load digest, terms/policy version, target system, parameters, idempotency key, SOP version, and action digest. It grants no broader carrier approval. |
| Proof | Immutable platform/broker acceptance receipt or state-transition record bound to the exact carrier/load action digest, actor, time, and resulting represented state. |
| Outcome | Observed/estimated/unavailable economic consequence, such as contribution margin or opportunity delay/loss, with basis, currency, time, provenance, uncertainty, and no causal overclaim. |
| Later revision evidence | Append-only resolution/adjudication, including `VALID_GATE`, `CANDIDATE_FALSE_GATE`, `CONFIRMED_FALSE_GATE`, or `INDETERMINATE`, reviewer evidence, missingness, and outcome evidence. It may propose but not enact a rule change. |

`FMCSA authoritative state` alone is not proof of carrier qualification. It may satisfy one authoritative evidence requirement, but it does not establish broker/load-specific policy, equipment fit, insurance, fraud/safety controls, current represented state, decision ownership, action authority, exact-object validation, or proof of acceptance.

Decision semantics are intentionally bounded:

- `ALLOW`: predicates support proposing acceptance; it is not permission.
- `DELAY`: do not accept until a declared temporal/evidence condition is satisfied and revalidated.
- `REVIEW`: escalate to the named review authority; no acceptance while unresolved.
- `REJECT`: propose no acceptance action and preserve the basis/evidence.

## 10. Finance transfer mapping

The transfer test is one bounded **payment authorization** SOP: authorize one payment instruction from one controlled account to one identified beneficiary. It is a mapping only, not a deployment, legal/compliance conclusion, or evidence of universality.

| Domain-neutral field | Finance binding |
| --- | --- |
| Inputs | Payment instruction digest, payer account digest, beneficiary digest, amount/currency, requested execution time, business-purpose reference. |
| Evidence | Account/control status, beneficiary verification, invoice/obligation evidence, available-funds observation, sanctions/fraud-control results, policy version, and provenance/freshness required by the owning institution. |
| Predicates | Versioned amount/limit, account status, beneficiary, duplicate-payment, separation-of-duties, sanctions/fraud, and policy predicates; unknown proprietary controls remain unknown rather than reconstructed. |
| Authority | A separately issued approval object naming approver, role, account/amount/action scope, validity window, and registry identity. A model score or analyst recommendation is not authority. |
| Stop conditions | Missing/contradictory/stale evidence, failed hard control, insufficient/expired approval, duplicate idempotency key, SOP drift, or altered payment object. |
| Escalation conditions | Policy-declared exception, contradictory beneficiary evidence, partially observable control, or amount requiring higher approval. |
| Execution eligibility | `VALID` only for the complete conjunction and exact payment action; otherwise `NULL` or policy-declared `ESCALATE`. |
| Exact action | One `SUBMIT_PAYMENT` object binding account, beneficiary, amount, currency, rail/date parameters, policy/SOP version, idempotency key, and digest. |
| Proof | Bank/payment-rail receipt or immutable ledger transition bound to the exact payment action digest and resulting status. |
| Outcome | Settled/returned/pending/unavailable status, timing, fees or other declared measures, provenance, and uncertainty. Outcome is not permission to change payment policy. |

The finance run may specialize evidence types, policies, predicates, authorities, actions, proof, and outcomes without changing the core definition/instance fields or lifecycle. If it cannot, the transfer result is negative or insufficient evidence; the core is not silently weakened during the run.

## 11. Cross-domain transfer matrix

Each candidate below has exactly one classification for this planned trucking/finance comparison.

| Candidate reusable concept | Classification | Boundary/rationale |
| --- | --- | --- |
| Immutable SOP definition separate from instance | `NATURAL_TRANSFER` | Both domains require a stable policy identity distinct from events. |
| Typed inputs and context digests | `NATURAL_TRANSFER` | Same structural role; domain object types differ. |
| Evidence identity, provenance, time, and freshness | `NATURAL_TRANSFER` | Same structural role; acceptable sources/freshness are policy-specific. |
| Predicate/rule version and explicit unknown result | `NATURAL_TRANSFER` | Both require versioned evaluation without guessing. |
| Decision candidate distinct from permission | `NATURAL_TRANSFER` | Preserves the same legitimacy boundary. |
| Independently issued scoped authority binding | `NATURAL_TRANSFER` | Same role; issuer, scope, and law/policy differ. |
| Fail-closed `VALID | NULL | ESCALATE` eligibility | `NATURAL_TRANSFER` | Same execution structure under domain policy. |
| Exact approved/executed object identity | `NATURAL_TRANSFER` | Same integrity property for carrier acceptance and payment. |
| Idempotency/replay control | `NATURAL_TRANSFER` | Same structural need; registry and replay window differ. |
| Action-bound proof and reconciliation | `NATURAL_TRANSFER` | Same role; receipts and resulting states differ. |
| Outcome-to-revision separation | `NATURAL_TRANSFER` | Same governance boundary. |
| Economic outcome measurement | `PARTIAL_TRANSFER` | Both can measure effects, but causality, amounts, latency, and missingness differ materially. |
| Evidence contradiction resolution | `PARTIAL_TRANSFER` | Preserve evidence and escalate in both; source priority and adjudication procedure are domain policy. |
| Human review/escalation destination | `PARTIAL_TRANSFER` | Same route concept, domain-specific reviewers and duties. |
| FMCSA/regulatory carrier evidence | `DOMAIN_SPECIFIC` | It has no finance meaning. |
| Broker/load/equipment qualification predicates | `DOMAIN_SPECIFIC` | Trucking policy and operational evidence. |
| Payment account, beneficiary, amount, rail, sanctions controls | `DOMAIN_SPECIFIC` | Finance policy/evidence. |
| Authority owner identities and approval limits | `DOMAIN_SPECIFIC` | Authority cannot transfer between organizations or domains. |
| Trucking `ALLOW | DELAY | REVIEW | REJECT` as finance outcomes | `FORCED_FIT` | Finance must map its own candidate decisions; copying labels would distort meaning. |
| `qualification-attempt-v1` reviewer adjudication as execution authority | `FORCED_FIT` | Research adjudication supplies later evidence, never runtime permission. |
| A single cross-domain evidence-source hierarchy | `INSUFFICIENT_EVIDENCE` | Two mappings cannot justify one hierarchy. |
| Automatic generalized SOP compiler | `INSUFFICIENT_EVIDENCE` | No reference executions yet support it. |
| FMCSA state in payment authorization | `NOT_APPLICABLE` | It is outside the bounded finance SOP. |

The `NATURAL_TRANSFER` rows are universal-execution-structure **candidates**, not universal truths. Domain policy, evidence, and authority remain local. `FORCED_FIT` rows are rejected abstractions and must not enter the core.

## 12. Valid and invalid examples

Fixtures live in [`examples`](examples). They are synthetic and grant no real authority.

| Fixture | Expected result | Demonstrated property |
| --- | --- | --- |
| `valid-sop-definition.json` | valid | Complete immutable carrier-qualification definition |
| `invalid-sop-definition.json` | `ACTION_POLICY_CONFLICT` | Same action cannot be both allowed and prohibited |
| `valid-execution-instance.json` | valid | Exact eligible carrier/load action, proof, outcome, reconciliation |
| `invalid-prohibited-authority-inference.json` | `PROHIBITED_AUTHORITY_INFERENCE` | LLM-produced candidate cannot become authority |
| `invalid-exact-object-mismatch.json` | `EXACT_OBJECT_MISMATCH` | Executed digest must equal validated/approved digest |
| `invalid-replay.json` | `REPLAY_DETECTED` | A replay cannot remain valid or execute |
| `invalid-sop-version-mismatch.json` | `SOP_VERSION_MISMATCH` | Validation/action must bind the instance SOP version |
| `invalid-revision-without-authority.json` | `REVISION_AUTHORITY_REQUIRED` | A superseding definition requires separate approval authority |

The deterministic checker [`validate_contract.py`](validate_contract.py) validates required structure and the cross-object invariants above. It deliberately does not execute any action.

Exact validation commands, results, and claim boundaries are preserved in the [`validation record`](validation-record.md).

## 13. Reference-execution rules and limitations

A trucking reference execution must freeze this contract/version, the exact SOP definition, source instrument identity, evidence collection procedure, authority source, validator version, instance identity, and expected proof/outcome. It must preserve negative, null, escalated, missing, and contradictory results. A later finance transfer must reuse this domain-neutral core unchanged; domain bindings may change only in the fields designed for specialization.

Known limitations:

- No real trucking execution, finance execution, or independent review has yet occurred under this contract.
- The trucking mapping uses a research measurement instrument as evidence context; it does not authorize production carrier acceptance.
- The finance mapping has not been validated against a particular institution's legal, compliance, security, accounting, or payment-rail controls.
- ContinuityOS remains the owner of its legitimacy concepts and implementation; this contract only requires their identity-bound satisfaction references.
- Canonical JSON serialization, registries, clock/trust model, retention mechanisms, privacy controls, and cryptographic verification are execution-environment responsibilities that a reference plan must freeze.
- Two bounded mappings cannot establish universality.

These limitations constrain claims but do not require changing the domain-neutral core before the two planned reference mappings. A reference run may still determine that revision is required.

## 14. Final determination

`SOP_CONTRACT_READY_FOR_REFERENCE_EXECUTION`

Rationale: the definition and instance objects, lifecycle, fail-closed behavior, independent authority boundary, exact-object invariant, proof/outcome/reconciliation model, immutable revision path, and two bounded mappings are explicit enough to freeze one real trucking SOP instance and later test one materially independent finance instance without changing the domain-neutral core during either run. Readiness authorizes neither run and is not evidence of universality or product readiness.

The named downstream consumers are a separately authorized trucking reference-execution issue and, only after its evidence is preserved and reviewed, a separately authorized finance transfer-execution issue. No runtime implementation is justified by this determination.
