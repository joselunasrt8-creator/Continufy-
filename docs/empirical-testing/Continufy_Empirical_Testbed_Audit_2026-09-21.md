# Continufy Ecosystem Empirical-Testbed Audit

**Audit date:** 2026-09-21  
**Primary coordination issue:** [`Continufy-` #16](https://github.com/joselunasrt8-creator/Continufy-/issues/16)  
**Mode:** repository-grounded, read-only with respect to GitHub; no experiment executed; no repository or issue mutated

## Final determination

`USE_EXISTING_REPOSITORY`

Use the repository that owns the tested mechanism for the first controlled experiment. The first experiment should be the already-frozen **MindShift Issue #81 v2 matched context-effect experiment** in [`MindShift-` PR #85](https://github.com/joselunasrt8-creator/MindShift-/pull/85), after its remaining provider-identity gate passes and execution is separately authorized under Issue #81.

Do **not** create a dedicated empirical-testbed repository now. Do **not** use `continuity-sandbox` as a general ecosystem testbed. Keep it bounded to its presently executable StateGate/ContinuityOS-style governance-consumer surface. If a later cross-component experiment becomes eligible, `architecturalboundary-research` already has the most legitimate existing responsibility and machinery for preregistered cross-repository investigations, machine-readable evidence, and bounded synthesis.

This determination does not establish ecosystem composition. It selects the smallest legitimate place to obtain the next comparative result.

## Audit boundary and frozen repository identities

The audit inspected current default branches, the primary issue and its comment, relevant open issues and PRs, documentation, tests, experiment artifacts, workflows, schemas, registries, and existing investigation surfaces.

| Repository | Frozen default-branch commit | Primary observed responsibility |
| --- | --- | --- |
| [`Continufy-`](https://github.com/joselunasrt8-creator/Continufy-/commit/5151c0f8d1aaf573790ae18c46003c3845036885) | `5151c0f8d1aaf573790ae18c46003c3845036885` | Umbrella identity and coordination contracts; explicitly not a runtime or cross-repository authority |
| [`continuity-sandbox`](https://github.com/joselunasrt8-creator/continuity-sandbox/commit/5ae864c37c1f1d256398680dc90880be9db96f40) | `5ae864c37c1f1d256398680dc90880be9db96f40` | Same-owner governance consumer and historical Merge Guard evidence surface |
| [`stategate`](https://github.com/joselunasrt8-creator/stategate/commit/a7556fede24d0d0aa6fccc29dccc645e2c466589) | `a7556fede24d0d0aa6fccc29dccc645e2c466589` | Deterministic exact-PR-state validation with `VALID | NULL` proof output |
| [`ContinuityOS-`](https://github.com/joselunasrt8-creator/ContinuityOS-/commit/44f1eff7f0f7032a1c1c4afe9820dc9e0b927d86) | `44f1eff7f0f7032a1c1c4afe9820dc9e0b927d86` | Legitimacy/governed-execution mechanisms, conformance suites, adapters, and demos |
| [`MindShift-`](https://github.com/joselunasrt8-creator/MindShift-/commit/53224ac47d058965280162aa01ef0e6f247104ef) | `53224ac47d058965280162aa01ef0e6f247104ef` | Non-operational cognition/context research; v1 experiment preserved as pre-outcome invalid |
| [`SYNAPSE`](https://github.com/joselunasrt8-creator/SYNAPSE/commit/975fbd743e4c310c5e41feac41698e2044f25b6d) | `975fbd743e4c310c5e41feac41698e2044f25b6d` | Deterministic structural compiler, analysis engine, CLI, schemas, fixtures, and evidence artifacts |
| [`architecturalboundary-research`](https://github.com/joselunasrt8-creator/architecturalboundary-research/commit/30b9730f04fe0e0902a93af43941a9fa6fa8b7bf) | `30b9730f04fe0e0902a93af43941a9fa6fa8b7bf` | Empirical investigation methodology, preregistration, evidence lifecycle, registries, and cross-repository synthesis |
| [`structural-analysis-foundations`](https://github.com/joselunasrt8-creator/structural-analysis-foundations/commit/7cc919bebe799b5c9086d4ef58968947c761d00a) | `7cc919bebe799b5c9086d4ef58968947c761d00a` | Formal structural-analysis research objects, canonical fixtures, promotion records, and conformance harness |
| [`structology`](https://github.com/joselunasrt8-creator/structology/commit/86ef8c05dda4cb5a377f138c57409173f79f6c84) | `86ef8c05dda4cb5a377f138c57409173f79f6c84` | Provisional documentation-only candidate model; explicitly not empirically validated |

Active work was inspected separately from default-branch state. Most importantly, [`MindShift-` PR #85](https://github.com/joselunasrt8-creator/MindShift-/pull/85) is open, draft, mergeable, and frozen at commit `d6905f1b3ba1adcafa8c8df41367550b5db00bef`, tree `459ae45587edc1bd479f465bfda912141a0ec623`.

## Governing boundaries

This audit applies the following as claim-separation rules, not slogans:

- Capability does not create permission.
- Evidence does not create authority.
- Internal reproducibility does not create independent validation.
- Documentation does not establish observed enforcement.
- Successful execution does not establish economic value.
- Correct components do not establish ecosystem composition.

Same-owner repositories can produce internal engineering and comparative evidence. They cannot, by themselves, establish independent adoption, external trust, retained use, willingness to pay, or an externally validated cross-domain architecture.

## 1. Ecosystem empirical-readiness matrix

| Component | Classification | Concrete evidence | Legitimately testable now | Not established |
| --- | --- | --- | --- | --- |
| Continufy umbrella | `NOT_APPLICABLE` | [`README.md`](https://github.com/joselunasrt8-creator/Continufy-/blob/5151c0f8d1aaf573790ae18c46003c3845036885/README.md) states `Umbrella ≠ Runtime`; the [Reference Execution coordination contract](https://github.com/joselunasrt8-creator/Continufy-/blob/5151c0f8d1aaf573790ae18c46003c3845036885/docs/reference-execution/v1.0/coordination-contract.md) coordinates separately authorized repository-owned work and does not execute it. | Coordination completeness, frozen-manifest discipline, and cross-repository comparison rules. | Runtime behavior, component efficacy, execution eligibility, or ecosystem composition. |
| `continuity-sandbox` | `READY_WITH_LIMITATIONS` | The repository contains one executable consumer workflow, `.github/workflows/merge-guard-consumer.yml`, and retained VALID/NULL/dependency documents. The workflow still invokes `joselunasrt8-creator/continuity-merge-guard@v1.0.0`, not current `stategate`. Issue #16 and its 2026-09-19 disposition restrict the surface to StateGate/ContinuityOS governance evidence. | Installation, VALID/NULL behavior, proof output, removal/substitution behavior, overhead, and same-owner governance consumption after the intervention is repinned. | MindShift, SYNAPSE, Structology, Structural Analysis Foundations, ABR, or integrated ecosystem behavior. It also cannot establish independent dependency. |
| StateGate | `READY_WITH_LIMITATIONS` | `guard.mjs`, `check.mjs`, fixtures, schemas, `test.mjs`, and `scripts/run-controlled-validation.mjs` are executable. Audit replay produced **90/90 passing deterministic tests**. The retained campaign ended `CONTROLLED_VALIDATION_INCONCLUSIVE`: 13/24 scenarios executed, 11 representational gaps, 0 false accepts, 0 false rejects, reproducible. [`stategate` #66](https://github.com/joselunasrt8-creator/stategate/issues/66) defines the real same-owner value study. | Exact-object validation semantics, proof determinism, bounded NULL causes, replay rejection, review-head binding, and controlled representable scenarios. | Unique workflow value, superiority to native GitHub controls or a small script, natural-workflow benefit, independent adoption, or economic value. |
| ContinuityOS | `READY_WITH_LIMITATIONS` | Current main contains runtime code, schemas, migrations, conformance packs, 500+ test/evidence paths, bounded adapters, and runnable demos. Audit execution of `actions/continuity-merge-guard/test.mjs` passed 16/16 and `conformance/runner.mjs` reported all declared Stage 1 and implemented Stage 2 cases observed. The filesystem governed-execution path is executable, but repository documents preserve bounded adapter and bypass limitations. | Specific declared legitimacy predicates, conformance behavior, replay/proof properties, and bounded gateway paths. | Non-bypassability across every mutation surface, universal governance, general ecosystem authority, external operational value, or composition with cognition/structural-analysis layers. |
| MindShift | `READY_WITH_LIMITATIONS` | Main preserves v1 as [`EXPERIMENT_INVALID`](https://github.com/joselunasrt8-creator/MindShift-/blob/53224ac47d058965280162aa01ef0e6f247104ef/docs/issue-81/experiment-record.md) before any outcomes. The default-branch validator passed during this audit. Active [`PR #85`](https://github.com/joselunasrt8-creator/MindShift-/pull/85) contains the v2 package; five deterministic tests and the non-provider preflight passed at its exact head. Provider identity remains `NOT_RUN_NO_CREDENTIAL`; no v2 outcome exists. | Whether one frozen context-organization treatment changes one frozen model’s outputs relative to an information-equivalent raw baseline. | General cognitive improvement, cross-model transfer, production necessity, authority, permission, legitimacy, or economic value. |
| SYNAPSE | `READY_FOR_CONTROLLED_TEST` | `pyproject.toml` exposes the `synapse` CLI; the repository contains deterministic compiler/analysis modules, 13 schema files, extensive positive/negative fixtures, and focused test modules. [`docs/issue-83-cross-repository-conformance.md`](https://github.com/joselunasrt8-creator/SYNAPSE/blob/975fbd743e4c310c5e41feac41698e2044f25b6d/docs/issue-83-cross-repository-conformance.md) and `conformance/foundation_adapter.py` implement an executable bridge to a pinned Structural Analysis Foundations fixture. [`SYNAPSE` #165](https://github.com/joselunasrt8-creator/SYNAPSE/issues/165) specifies an external-repository decision-recovery pilot. | Determinism, representation invariance, bounded structural predicates, artifact hashes, negative fixtures, and cross-repository conformance against frozen research fixtures. | Decision influence, prospective prediction, user trust, adoption, authority, or economic value. A same-owner conformance pass is not external validation. |
| Architectural Boundary Research | `READY_WITH_LIMITATIONS` | The repository contains a versioned investigation template, BOR/SRF/DER/MSR schemas, machine-readable registries, preregistration/result workspaces, deterministic builders, and `scripts/validate.py`. The full repository validator passed during this audit. However, its validation output still records the architectural-investigation instrument candidate as `INSTRUMENT_SPECIFICATION_REVISION_REQUIRED`. The prior StateGate consumer investigation is retained as `BLOCKED_BY_REPOSITORY_PERMISSIONS`. | Preregistered comparative studies, heterogeneous cohorts, missingness/blocker capture, reruns, bounded cross-repository synthesis, and negative/indeterminate retention. | Component authority, automatic promotion of findings, ecosystem composition before eligible cells execute, external adoption, or useful outcomes merely because the protocol ran. |
| Structural Analysis Foundations | `READY_WITH_LIMITATIONS` | The repository contains formal research objects, schemas, canonical fixtures, promotion packages/records, validation tools, and an executable conformance harness. Its external dependency-algebra adapter correctly emits `UNOBSERVED` when no implementation is available rather than `PASS`. The README also marks current JSON research-object records as seeds unless separately promoted. | Reference-harness mechanics, schema validity, bounded semantic conformance, promotion-record validity, and deterministic fixture realization. | Broad formal correctness of implementations, independent external conformance without an observed external implementation, or automatic authority from a conformance result. |
| Structology | `BLOCKED` | [`README.md`](https://github.com/joselunasrt8-creator/structology/blob/86ef8c05dda4cb5a377f138c57409173f79f6c84/README.md) labels Candidate Model v0.1 provisional and unvalidated; the repository has only three tracked content files and no schemas, validators, fixtures, or runtime. ABR’s `structology-transfer-audit-rehearsal-1` retained `BLOCKED` / `NOT_REACHED` because authoritative immutable references to the model, methodology contract, and transfer-audit instrument were unavailable. | Documentation consistency and candidate-definition review only. | Cross-domain transfer, natural fit, universality, executable enforcement, or empirical value. |

## 2. Existing-test-surface inventory

| Surface | Existing artifacts | Can test | Cannot establish | Responsibility fit |
| --- | --- | --- | --- | --- |
| MindShift Issue #81 v2 in PR #85 | Frozen protocol, task set, source manifest, model settings, historical-v1 manifest, deterministic runner, five tests | Matched context-only effect under one model/task/source cohort | General cognition, production value, authority, cross-model transfer | Excellent: it tests MindShift’s central surviving empirical claim inside the owning repository |
| SYNAPSE CLI and test/fixture suite | Compiler, registered analysis, canonical JSON, schemas, accepted/rejected fixtures, stable exit codes | Determinism, normalization, structural classifications, diagnostic behavior | Decision relevance or user value | Excellent for component behavior |
| SYNAPSE ↔ Structural Analysis Foundations adapter | Frozen research fixture translated through SYNAPSE and emitted as a machine-readable conformance result | Bounded semantic conformance and drift/failure behavior | Independent validation or generalized formal correctness | Legitimate cross-repository executable interface with bounded semantics |
| StateGate deterministic suite | `test.mjs`, fixtures, proof schema/metadata, controlled-validation script | `VALID | NULL`, hashes, review binding, replay resistance, representable scenarios | Natural workflow benefit or unique value | Excellent for semantics; limited for value |
| `continuity-sandbox` consumer workflow | One GitHub Action workflow plus retained mechanism/dependency artifacts | Same-owner installation/integration and governance behavior after repinning | Any non-governance component or ecosystem composition | Legitimate only if narrowed to StateGate/ContinuityOS |
| ContinuityOS conformance and bounded demos | Runtime/conformance suites, filesystem and GitHub-comment gateways, portability/LangChain demos | Specific legitimacy predicates and governed adapter behavior | Exhaustive non-bypass enforcement or external value | Legitimate for bounded ContinuityOS mechanisms, not as a neutral ecosystem testbed |
| ABR investigation system | Standard investigation topology, schemas, registries, validators, completed and blocked investigations | Preregistered cross-repository studies and bounded synthesis | Authority transfer, automatic promotion, usefulness from successful execution | Best existing host for later cross-component comparative experiments |
| Structural Analysis Foundations conformance harness | Research objects, canonical fixtures, adapters, deterministic replay/reporting | Bounded implementation conformance to specified semantics | Universality, authority, or external observation when adapter returns `UNOBSERVED` | Legitimate formal/semantic test surface |
| Continufy Reference Execution contract | Frozen cohort/record/comparison requirements | Coordination and reproducibility discipline | Component efficacy or authority | Coordination only; not an execution host |
| Structology repository | Candidate canon and boundary documentation | Review of definitions and internal consistency | Empirical transfer or runtime behavior | Not yet an empirical surface |

## 3. Executable cross-repository interfaces

### Observed executable interfaces

1. **Structural Analysis Foundations fixture → SYNAPSE adapter**  
   `SYNAPSE/conformance/foundation_adapter.py` reads the sibling `structural-analysis-foundations` repository, binds both Git commits, translates the Paper 1 fixture, executes SYNAPSE’s registered dependency analysis twice, and emits `synapse.cross-repository-conformance-result.v1`. This is executable, deterministic, and bounded.

2. **External dependency-algebra command → Structural Analysis Foundations harness**  
   `structural-analysis-foundations/conformance/adapters/dependency_algebra_external.py` resolves a CLI/executable/Python package, runs it twice, validates evidence, and distinguishes `UNOBSERVED`, `CONFORMANCE_PASS`, `CONFORMANCE_DRIFT`, and `CONFORMANCE_FAIL`. The interface is executable; current retained external observation is absent.

3. **Published governance action → consumer repository workflow**  
   `continuity-sandbox/.github/workflows/merge-guard-consumer.yml` invokes a published action and uploads `MERGE_GUARD_PROOF.json`. This is executable in GitHub Actions, but the pin targets the historical `continuity-merge-guard@v1.0.0` identity rather than current `stategate`; it must not be described as current StateGate evidence without repinning and rerunning.

4. **ABR promotion package → Structural Analysis Foundations review records**  
   ABR emits a versioned B2 promotion package with hashes; Structural Analysis Foundations preserves a snapshot and validates local admissibility/promotion records. This is an executable artifact-validation handoff, not a shared runtime and not automatic promotion.

### Documented or proposed interfaces only

- Continufy’s umbrella sequence and Reference Execution contract coordinate work but do not execute components.
- MindShift handoffs remain non-operational artifacts unless a downstream repository explicitly accepts and tests them.
- ABR #142 is a study specification, not an executed ecosystem topology.
- Structology’s candidate vocabulary has no executable cross-domain interface.
- ContinuityOS documentation that names broader agent/tool surfaces does not, by itself, prove every surface is routed through a non-bypassable gate.

## 4. Testbed decision

### Selected state

`USE_EXISTING_REPOSITORY`

### Exact interpretation

Use a **repository-owned experiment topology**, not a new universal harness:

1. Run isolated component experiments in the repository that owns the mechanism and claim.
2. Preserve machine-readable outputs and exact lineage locally.
3. Use `architecturalboundary-research` only when a concrete cross-component comparative question has eligible provider→target cells and at least two compatible frozen outputs.
4. Keep Issue #16 as the coordination/decision record, not an execution runtime.

For the immediate first experiment, the canonical surface is `MindShift-` PR #85. For a later cross-component cohort, the presumptive existing host is `architecturalboundary-research`, subject to its instrument-readiness limitation being resolved for the selected protocol.

### Why not `CREATE_DEDICATED_TESTBED`

A dedicated repository would presently duplicate capabilities that already exist:

- experiment-specific freezing and execution in MindShift;
- deterministic component evidence in SYNAPSE, StateGate, and ContinuityOS;
- formal conformance in Structural Analysis Foundations; and
- cross-repository investigation lifecycle, schemas, registries, and synthesis in ABR.

No concrete eligible experiment has demonstrated that these surfaces cannot preserve ownership, provenance, or experimental isolation. The burden required by Issue #16 for a new repository is therefore unmet.

### Why not `NO_TESTBED_JUSTIFIED_YET`

At least one controlled experiment is already prospectively specified and mechanically frozen: MindShift #81 v2. The absence of provider access is a remaining execution gate, not a reason to deny that a legitimate experimental surface exists.

### Responsibility conflict requiring correction

`continuity-sandbox/README.md` currently calls that repository “the controlled internal empirical testbed for the Continufy ecosystem.” Issue #16 and its September 19 disposition say the opposite for non-governance components. Because the repository’s only executable workflow is the historical Merge Guard consumer, the broad README sentence is not supported by observed capability and creates responsibility leakage. Narrow the README to StateGate/ContinuityOS governance experiments.

## 5. First experiment specification

### Identity

- **Experiment:** `MS81-V2`
- **Owning repository:** `joselunasrt8-creator/MindShift-`
- **Issue:** [`MindShift-` #81](https://github.com/joselunasrt8-creator/MindShift-/issues/81)
- **Frozen implementation:** [`MindShift-` PR #85](https://github.com/joselunasrt8-creator/MindShift-/pull/85)
- **Head commit:** `d6905f1b3ba1adcafa8c8df41367550b5db00bef`
- **Tree:** `459ae45587edc1bd479f465bfda912141a0ec623`
- **Base main:** `53224ac47d058965280162aa01ef0e6f247104ef`
- **Frozen source commit:** `d31d7630c5c2189dc350626215f2ba0c65b667a0`
- **Protocol:** `docs/issue-81/v2/protocol.md`, version `2.0.0`
- **Model:** `gpt-4.1-mini-2025-04-14`
- **Cohort:** four tasks, three paired replicates per task, 12 pairs, 24 generation outputs
- **Current state:** deterministic preflight passed; provider identity probe not run; no v2 outcomes exist

### Research question

Holding model, task, source bytes, system instruction, inference settings, and evaluation procedure constant, does `MINDSHIFT_STRUCTURED_V2` context organization improve model output relative to the competent `ORDINARY_RAW_V2` presentation?

### Baseline

`ORDINARY_RAW_V2`: concatenate each complete frozen source in manifest order with fixed source delimiters. No summarization, filtering, annotation, classification, reordering, or task guidance.

### Intervention

`MINDSHIFT_STRUCTURED_V2`: split the same source bytes at Markdown headings; categorize segments using frozen heading-only rules; emit them in a frozen category order while preserving source and segment order. Add only fixed structural syntax. No answer hints, task relevance, privileged facts, summaries, or task repetition.

### Counterfactual

The baseline is the direct counterfactual: same model, same source bytes, same task exactly once, same system instruction, same generation settings, and no structural categorization. A separate removal phase is unnecessary because the paired raw condition already represents absence of the intervention.

### Frozen artifact lineage

The preflight observed the following v2 SHA-256 identities at the exact PR head:

| Artifact | SHA-256 |
| --- | --- |
| `experiment.py` | `4582f96ab4caae46aa4331aa813e5ac99a6338245a85d2d9fcab5703e25d2204` |
| `historical-v1-manifest.json` | `d5c0ff78dcfee5167c75a27f12f520a2cfb891de4ccd8fff363b44f5ca21be26` |
| `model-settings.json` | `6a17732d98431befd1070f32e32a824c9c4fb9702238b594771cf65b4624f512` |
| `protocol.md` | `2972d45e253f19f4080fd6a741a44d7adc45023ecb64bfe5a8198ca0d8169c74` |
| `source-manifest.json` | `d527c5f4758d01dcf4ec85f08e98f4c0b147fcf2fcb8e9d76096db3e61c97d33` |
| `task-set.json` | `443e444ff2f6bdf02f75114f7b01631110243fa02272c7c18a5a6818e7745671` |

The v1 historical package is separately hash-protected and must remain unchanged.

### Machine-readable observations

The runner uses create-only writes under `docs/issue-81/v2/execution/` and preserves:

- `preflight-result.json`;
- `run-manifest.json`;
- raw provider bytes and per-call records;
- anonymous evaluation records;
- sealed condition key and digest;
- per-pass and final score JSON;
- pairwise preference JSON;
- `per-task-effects.json`;
- `aggregate-result.json`;
- `determination.json`;
- limitations and execution summary.

Provider-returned model identity, system fingerprint when available, token usage, timing, request/response hashes, repository commit/tree, protocol artifact hashes, and seed schedule are retained.

### Negative, null, and indeterminate outcomes

Exactly one outcome is allowed:

- `MINDSHIFT_CONTEXT_IMPROVEMENT_SUPPORTED`
- `NO_MEASURABLE_IMPROVEMENT`
- `MINDSHIFT_CONTEXT_DEGRADED_OUTPUT`
- `INDETERMINATE`
- `EXPERIMENT_INVALID`

All are first-class evidence. A provider-access failure before outcomes is an execution blocker, not a MindShift effect result.

### Stopping rule

Stop before or during execution on any failed preflight invariant, provider/model-identity failure, source/context mismatch, evaluator leakage, outcome-aware mutation, evidence overwrite attempt, or more than one incomplete pair. Do not expand tasks, replicates, models, rubric, or thresholds after any outcome is observed.

### Reproducibility requirements

- exact clean checkout of the frozen PR commit and tree;
- exact source commit and per-source hashes;
- exact protocol/task/model/runner artifact hashes;
- deterministic preflight and five tests pass;
- provider identity probe passes before generation;
- identical request bytes for allowed transient retries;
- create-only evidence directory;
- raw outputs and hashes retained;
- blinded identities and custody preserved;
- rerun is a separately preregistered replication, not an overwrite or retry disguised as the same run.

### Claim ceiling

A positive result supports only a bounded effect for this frozen model snapshot, four-task source cohort, two context constructors, generation settings, and model-as-judge evaluation procedure. It cannot support general LLM improvement, cross-model transfer, production necessity, ecosystem composition, authority, permission, legitimacy, execution eligibility, independent validation, adoption, or economic value.

## 6. Why this experiment has the highest information gain now

MindShift’s central value claim is still empirically unresolved. The existing v1 failure falsified a procedure, not the context-effect hypothesis. PR #85 removes the known information-equivalence defect without building a generalized harness. A valid result can therefore collapse a major branch of uncertainty:

- positive: justify a separately preregistered replication;
- null: stop assuming context structure adds value for this bounded cohort;
- degraded: treat the intervention as harmful under the tested conditions;
- indeterminate: expose evaluation/sample limitations without architecture expansion;
- invalid: identify a remaining experimental-design defect before broader ecosystem work.

By contrast, ABR #142 attempts to differentiate many provider→target edges before the simplest unresolved component-level effect is known. It is strategically valuable later, but not the minimum-information first move.

## 7. Blockers and prerequisites

### First experiment blockers

1. PR #85 is open and draft; its frozen head must remain exact.
2. The provider-identity probe has not run and currently reports `NOT_RUN_NO_CREDENTIAL`.
3. Issue #16 does not authorize model outcome generation; execution authority must come from Issue #81 or a clearly recorded owner decision.
4. The dated model snapshot must be accessible and must identify itself as the frozen model.
5. A clean checkout must pass the exact tests and both preflights before the first outcome call.

### Ecosystem-level blockers

1. Fewer than two components presently have compatible frozen empirical outcome packages suitable for an integration test.
2. `continuity-sandbox` has a responsibility contradiction and a historical action pin.
3. ABR’s cross-repository cohort issues #142/#143 are specifications, not frozen executed cohorts.
4. ABR’s architectural-investigation instrument still records `INSTRUMENT_SPECIFICATION_REVISION_REQUIRED` in current validation output.
5. StateGate’s internal consumer evidence has no natural-workflow outcome; the ABR #134 attempt is retained as permission-blocked.
6. Structology’s transfer test is blocked on authoritative immutable references and a frozen audit instrument.
7. No current evidence shows that a dedicated repository is required to preserve isolation or provenance.

## 8. Claims the first experiment could and could not support

### Could support

- whether the frozen MindShift context organization changes measured output quality versus an information-equivalent raw baseline;
- direction and magnitude of the paired effect within the frozen cohort;
- task-level heterogeneity;
- differences in omissions, unsupported claims, stale-context errors, contradictions, uncertainty calibration, decision usefulness, token use, latency, and preference;
- whether the frozen experimental machinery is valid, invalid, or indeterminate;
- whether a separate cross-model replication is justified.

### Could not support

- that MindShift increases underlying model capability;
- that the effect transfers to other models, tasks, domains, or users;
- that MindShift belongs in every Continufy workflow;
- that MindShift artifacts create authority, permission, legitimacy, or execution eligibility;
- that SYNAPSE, StateGate, ContinuityOS, ABR, SAF, or Structology compose with MindShift;
- that Continufy is a validated cross-domain architecture;
- external adoption, retention, trust, willingness to pay, market value, or economic dependency.

## 9. Recommended GitHub issue changes

Do not execute or create infrastructure from Issue #16. Update it as a coordination decision record:

1. **Retitle** to: `Coordinate bounded Continufy empirical testing and testbed decision`.
2. **Record the canonical determination:** `USE_EXISTING_REPOSITORY`.
3. **Name the first surface:** `MindShift-` Issue #81 / PR #85, with exact commit/tree and the provider gate.
4. **State that Issue #16 does not authorize experiment execution.** Execution remains repository-local.
5. **Replace “at least one experiment for each participating component”** with “exactly one first experiment selected; later experiments require independent eligibility and ownership.” The current wording encourages unnecessary breadth.
6. **Define the later cross-component host:** presumptively `architecturalboundary-research`, only after an eligible concrete experiment exists and its instrument is frozen.
7. **Preserve the new-repository gate:** create a dedicated testbed only if a specified cross-component experiment cannot run in owning repositories or ABR without ownership, provenance, or isolation leakage.
8. **Link a corrective documentation issue/PR for `continuity-sandbox`:** narrow its README from ecosystem-wide testbed to StateGate/ContinuityOS governance sandbox and repin any future experiment to the exact current intervention identity.
9. **Link existing experiment issues without collapsing evidence classes:** MindShift #81, SYNAPSE #165, StateGate #66, ABR #142, and ABR #143.
10. **Record this audit as evidence, not authority:** it supports the coordination decision but does not execute, validate, or close the linked experiments.

## 10. Closure criteria for Continufy Issue #16

Issue #16 can close when all of the following are true:

- [ ] The issue records exactly `USE_EXISTING_REPOSITORY`.
- [ ] The issue states that repository-owned component experiments remain in their owning repositories.
- [ ] The first experiment is identified as MindShift #81 v2 at PR #85’s exact frozen identity.
- [ ] The issue explicitly states that no outcome generation is authorized by Issue #16.
- [ ] The `continuity-sandbox` scope contradiction is corrected or linked as a blocking documentation correction.
- [ ] `architecturalboundary-research` is named only as the presumptive later cross-component investigation host, not as proof that an integrated architecture exists.
- [ ] The dedicated-repository creation gate requires a concrete failed-fit demonstration against existing surfaces.
- [ ] Negative, degraded, invalid, blocked, and indeterminate outcomes remain admissible.
- [ ] Internal evidence and external validation remain explicitly separated.
- [ ] Follow-on experiment execution remains tracked in component-owned issues rather than keeping #16 open as an indefinite umbrella.

Issue #16 does **not** need to remain open until every component has run an experiment. Its proper closure product is the bounded testbed decision and routing rule. Keeping it open for all component outcomes would turn a coordination issue into an unbounded architecture program.

## Concise determination

Use the existing `MindShift-` experiment surface for the first controlled test; reserve `architecturalboundary-research` for a later eligible cross-component comparison; keep `continuity-sandbox` governance-only; create no new repository. The next evidence should be one valid, bounded MindShift #81 v2 outcome—not another ecosystem integration layer.
