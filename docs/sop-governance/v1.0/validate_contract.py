#!/usr/bin/env python3
"""Deterministic conformance checks for the Continufy SOP contract fixtures.

This is a documentation validator, not a workflow runtime or execution engine.
It uses only the Python standard library and checks cross-object invariants that
JSON Schema cannot express, including exact-object identity and version binding.
"""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
EXAMPLES = ROOT / "examples"
DIGEST_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
SEMVER_RE = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")
NON_AUTHORITY_LAYERS = {"LLM_LAYER", "MINDSHIFT", "METHODOLOGY", "SYNAPSE"}
ACTION_IDENTITY_FIELDS = (
    "action_id",
    "action_digest",
    "action_type",
    "target_digest",
    "parameters_digest",
    "idempotency_key",
    "sop_id",
    "sop_version",
)


class ContractError(Exception):
    def __init__(self, code: str, detail: str) -> None:
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.detail = detail


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def fail(code: str, detail: str) -> None:
    raise ContractError(code, detail)


def require(condition: bool, code: str, detail: str) -> None:
    if not condition:
        fail(code, detail)


def validate_schema_document(schema: dict[str, Any], filename: str) -> None:
    require(
        schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema",
        "SCHEMA_DECLARATION_INVALID",
        f"{filename} must declare JSON Schema draft 2020-12",
    )
    require(schema.get("type") == "object", "SCHEMA_ROOT_INVALID", f"{filename} root must be an object")
    require(schema.get("additionalProperties") is False, "SCHEMA_ROOT_OPEN", f"{filename} root must be closed")
    properties = schema.get("properties", {})
    for field in schema.get("required", []):
        require(field in properties, "SCHEMA_REQUIRED_PROPERTY_UNDECLARED", f"{filename}: {field}")

    definitions = schema.get("$defs", {})

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            ref = value.get("$ref")
            if isinstance(ref, str) and ref.startswith("#/$defs/"):
                name = ref.removeprefix("#/$defs/")
                require(name in definitions, "SCHEMA_REF_UNRESOLVED", f"{filename}: {ref}")
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(schema)


def validate_top_level(data: dict[str, Any], schema: dict[str, Any]) -> None:
    require(isinstance(data, dict), "OBJECT_REQUIRED", "contract fixture root must be an object")
    required = schema["required"]
    missing = [field for field in required if field not in data]
    require(not missing, "MISSING_REQUIRED_FIELD", ", ".join(missing))
    unknown = sorted(set(data) - set(schema["properties"]))
    require(not unknown, "UNKNOWN_TOP_LEVEL_FIELD", ", ".join(unknown))


def validate_digest_fields(value: Any, path: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if (key == "digest" or key.endswith("_digest")) and child is not None:
                require(
                    isinstance(child, str) and DIGEST_RE.fullmatch(child) is not None,
                    "DIGEST_INVALID",
                    child_path,
                )
            validate_digest_fields(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            validate_digest_fields(child, f"{path}[{index}]")


def validate_semver(value: Any, path: str) -> None:
    require(isinstance(value, str) and SEMVER_RE.fullmatch(value) is not None, "SEMVER_INVALID", path)


def unique_ids(items: Any, field: str, path: str) -> set[str]:
    require(isinstance(items, list) and items, "NONEMPTY_ARRAY_REQUIRED", path)
    values: list[str] = []
    for index, item in enumerate(items):
        require(isinstance(item, dict), "OBJECT_REQUIRED", f"{path}[{index}]")
        require(isinstance(item.get(field), str) and item[field], "ID_REQUIRED", f"{path}[{index}].{field}")
        values.append(item[field])
    require(len(values) == len(set(values)), "DUPLICATE_ID", path)
    return set(values)


def validate_definition(data: dict[str, Any], schema: dict[str, Any]) -> None:
    validate_top_level(data, schema)
    require(data["contract_version"] == "continufy-sop-governance-v1.0.0", "CONTRACT_VERSION_INVALID", "contract_version")
    require(data["object_type"] == "SOP_DEFINITION", "OBJECT_TYPE_INVALID", "object_type")
    require(data["immutable"] is True, "DEFINITION_NOT_IMMUTABLE", "immutable must be true")
    validate_semver(data["version"], "version")
    validate_digest_fields(data)

    for field in (
        "input_object_types",
        "required_evidence",
        "decision_rules",
        "authority_requirements",
        "stop_conditions",
        "escalation_conditions",
        "allowed_actions",
        "prohibited_actions",
        "execution_preconditions",
        "proof_requirements",
        "outcome_measurements",
    ):
        require(isinstance(data[field], list) and data[field], "NONEMPTY_ARRAY_REQUIRED", field)

    evidence_ids = unique_ids(data["required_evidence"], "requirement_id", "required_evidence")
    unique_ids(data["decision_rules"], "rule_id", "decision_rules")
    unique_ids(data["authority_requirements"], "authority_requirement_id", "authority_requirements")
    unique_ids(data["stop_conditions"], "condition_id", "stop_conditions")
    unique_ids(data["escalation_conditions"], "condition_id", "escalation_conditions")
    unique_ids(data["execution_preconditions"], "precondition_id", "execution_preconditions")
    unique_ids(data["proof_requirements"], "proof_requirement_id", "proof_requirements")
    unique_ids(data["outcome_measurements"], "measurement_id", "outcome_measurements")

    allowed = {item.get("action_type") for item in data["allowed_actions"]}
    prohibited = {item.get("action_type") for item in data["prohibited_actions"]}
    overlap = sorted(allowed & prohibited)
    require(not overlap, "ACTION_POLICY_CONFLICT", ", ".join(overlap))

    covered_actions = {
        action
        for requirement in data["authority_requirements"]
        for action in requirement.get("action_types", [])
    }
    uncovered = sorted(allowed - covered_actions)
    require(not uncovered, "ACTION_AUTHORITY_UNCOVERED", ", ".join(uncovered))

    for rule in data["decision_rules"]:
        refs = set(rule.get("evidence_requirement_refs", []))
        require(refs <= evidence_ids, "UNKNOWN_EVIDENCE_REQUIREMENT_REF", rule["rule_id"])
        validate_semver(rule.get("rule_version"), f"decision_rules.{rule['rule_id']}.rule_version")
    for precondition in data["execution_preconditions"]:
        refs = set(precondition.get("evidence_requirement_refs", []))
        require(refs <= evidence_ids, "UNKNOWN_EVIDENCE_REQUIREMENT_REF", precondition["precondition_id"])

    revision_policy = data["revision_policy"]
    for flag in (
        "automatic_revision_prohibited",
        "review_required",
        "supporting_evidence_required",
        "contrary_evidence_required",
        "new_version_required",
        "effective_date_required",
    ):
        require(revision_policy.get(flag) is True, "REVISION_POLICY_WEAKENED", flag)

    supersedes = data["supersedes"]
    approval = data["provenance"].get("revision_approval")
    if supersedes is not None:
        require(approval is not None, "REVISION_AUTHORITY_REQUIRED", "superseding version lacks revision approval")
        require(supersedes.get("sop_id") == data["sop_id"], "SUPERSESSION_LINEAGE_INVALID", "sop_id differs")
        validate_semver(supersedes.get("version"), "supersedes.version")
        require(supersedes["version"] != data["version"], "SUPERSESSION_LINEAGE_INVALID", "version did not change")
        require(approval.get("authority_id") and approval.get("authority_digest"), "REVISION_AUTHORITY_REQUIRED", "approval authority identity incomplete")
        require(approval.get("effective_from") == data["effective_from"], "REVISION_EFFECTIVE_DATE_MISMATCH", "approval and definition differ")
    else:
        require(approval is None, "UNBOUND_REVISION_APPROVAL", "initial version cannot carry a supersession approval")


def same_sop_binding(left: dict[str, Any], right: dict[str, Any]) -> bool:
    return all(left.get(key) == right.get(key) for key in ("sop_id", "version", "definition_digest"))


def validate_execution(data: dict[str, Any], schema: dict[str, Any]) -> None:
    validate_top_level(data, schema)
    require(data["contract_version"] == "continufy-sop-governance-v1.0.0", "CONTRACT_VERSION_INVALID", "contract_version")
    require(data["object_type"] == "SOP_EXECUTION_INSTANCE", "OBJECT_TYPE_INVALID", "object_type")
    validate_digest_fields(data)

    binding = data["sop_binding"]
    validate_semver(binding.get("version"), "sop_binding.version")
    validation = data["eligibility_validation"]
    approved = data["approved_execution_object"]
    execution = data["execution"]
    authority = data["authority_binding"]
    reconciliation = data["reconciliation"]

    if authority is not None:
        require(
            authority.get("produced_by_layer") not in NON_AUTHORITY_LAYERS,
            "PROHIBITED_AUTHORITY_INFERENCE",
            f"{authority.get('produced_by_layer')} cannot produce authority",
        )

    require(
        same_sop_binding(binding, validation["validated_sop_binding"]),
        "SOP_VERSION_MISMATCH",
        "instance and validation bindings differ",
    )
    require(
        approved.get("sop_id") == binding["sop_id"] and approved.get("sop_version") == binding["version"],
        "SOP_VERSION_MISMATCH",
        "approved action does not bind the instance SOP version",
    )

    require(
        reconciliation.get("replay_status") != "REPLAY_DETECTED"
        and validation["legitimacy_conjunction"].get("replay_absent") is True,
        "REPLAY_DETECTED",
        "replayed actions cannot be eligible or executed",
    )

    require(
        validation.get("validated_action_digest") == approved.get("action_digest"),
        "EXACT_OBJECT_MISMATCH",
        "validated and approved action digests differ",
    )
    executed = execution.get("executed_object")
    if execution.get("status") in {"EXECUTED", "FAILED"}:
        require(executed is not None, "EXECUTED_OBJECT_REQUIRED", "execution attempt lacks exact object")
        mismatches = [field for field in ACTION_IDENTITY_FIELDS if approved.get(field) != executed.get(field)]
        require(not mismatches, "EXACT_OBJECT_MISMATCH", ", ".join(mismatches))

    result = validation.get("result")
    legitimacy = validation["legitimacy_conjunction"]
    legitimacy_flags = (
        "continuity_satisfied",
        "authority_satisfied",
        "atao_satisfied",
        "aeo_satisfied",
        "evidence_satisfied",
        "predicates_satisfied",
        "preconditions_satisfied",
        "exact_object_bound",
        "replay_absent",
        "sop_version_current",
    )
    if result == "VALID":
        false_flags = [flag for flag in legitimacy_flags if legitimacy.get(flag) is not True]
        require(not false_flags, "LEGITIMACY_CONJUNCTION_FALSE", ", ".join(false_flags))
        require(authority is not None, "AUTHORITY_REQUIRED", "VALID result lacks authority")
        require(authority.get("status") == "ACTIVE", "AUTHORITY_NOT_ACTIVE", authority.get("status", "missing"))
        require(
            legitimacy.get("authority_digest") == authority.get("authority_digest"),
            "AUTHORITY_BINDING_MISMATCH",
            "validation cites a different authority object",
        )
        require(all(item.get("freshness_status") == "FRESH" for item in data["evidence_set"]), "EVIDENCE_NOT_FRESH", "VALID result contains stale or unknown evidence")
        require(all(not item.get("contradiction_refs") for item in data["evidence_set"]), "EVIDENCE_CONTRADICTORY", "VALID result contains unresolved contradiction")
        require(all(item.get("result") == "TRUE" for item in data["predicate_evaluations"]), "PREDICATE_NOT_SATISFIED", "VALID result contains false or unknown predicate")
    else:
        require(execution.get("status") == "NOT_ATTEMPTED", "INELIGIBLE_EXECUTION_ATTEMPT", result)
        require(executed is None and data["proof"] is None, "INELIGIBLE_EXECUTION_ARTIFACT", result)

    require(
        data["decision_candidate"].get("proposed_action_id") == approved.get("action_id"),
        "PROPOSED_ACTION_MISMATCH",
        "decision and approved action IDs differ",
    )
    proof = data["proof"]
    if proof is not None:
        require(proof.get("action_digest") == approved.get("action_digest"), "EXACT_OBJECT_MISMATCH", "proof action digest differs")
        require(proof.get("receipt_digest") == execution.get("receipt_digest"), "PROOF_RECEIPT_MISMATCH", "proof and execution receipt differ")
    outcome = data["outcome"]
    if outcome is not None:
        require(outcome.get("action_digest") == approved.get("action_digest"), "OUTCOME_ACTION_MISMATCH", "outcome action digest differs")
        if outcome.get("status") == "AVAILABLE":
            require(outcome.get("measurements"), "OUTCOME_MEASUREMENT_REQUIRED", "AVAILABLE outcome is empty")
            require(outcome.get("unavailable_reason") is None, "OUTCOME_STATUS_CONFLICT", "AVAILABLE outcome has unavailable reason")
        if outcome.get("status") == "UNAVAILABLE":
            require(outcome.get("unavailable_reason"), "OUTCOME_UNAVAILABLE_REASON_REQUIRED", "reason missing")

    revision = data["revision_candidate"]
    if revision is not None:
        require(revision.get("status") == "CANDIDATE_ONLY", "ATTEMPTED_SELF_MODIFICATION", "execution instance cannot approve revision")
        require(outcome is not None and revision.get("source_outcome_id") == outcome.get("outcome_id"), "REVISION_OUTCOME_MISMATCH", "candidate source outcome differs")

    lifecycle = data["lifecycle_history"]
    require(isinstance(lifecycle, list) and lifecycle, "LIFECYCLE_REQUIRED", "lifecycle_history")
    sequences = [event.get("sequence") for event in lifecycle]
    require(sequences == list(range(1, len(lifecycle) + 1)), "LIFECYCLE_SEQUENCE_INVALID", str(sequences))
    states = [event.get("state") for event in lifecycle]
    required_order = ["BOUND", "INPUTS_OBSERVED", "EVIDENCE_ASSEMBLED", "PREDICATES_EVALUATED", "DECISION_PROPOSED"]
    require(states[: len(required_order)] == required_order, "LIFECYCLE_ORDER_INVALID", str(states))
    if result == "VALID" and execution.get("status") == "EXECUTED":
        require("ELIGIBILITY_VALIDATED" in states and states.index("ELIGIBILITY_VALIDATED") < states.index("EXECUTED"), "EXECUTION_BEFORE_VALIDATION", str(states))

    if reconciliation.get("status") == "MATCHED":
        require(reconciliation.get("exact_object_match") is True, "RECONCILIATION_CONFLICT", "MATCHED without exact identity")
        require(reconciliation.get("proof_complete") is True, "RECONCILIATION_CONFLICT", "MATCHED without proof")
        require(reconciliation.get("exception_status") == "NONE", "RECONCILIATION_CONFLICT", "MATCHED with exception")


def resolve_pointer(document: Any, pointer: str) -> tuple[Any, str]:
    require(pointer.startswith("/"), "MUTATION_PATH_INVALID", pointer)
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    parent = document
    for part in parts[:-1]:
        parent = parent[int(part)] if isinstance(parent, list) else parent[part]
    return parent, parts[-1]


def materialize_invalid_fixture(descriptor: dict[str, Any]) -> dict[str, Any]:
    require(descriptor.get("fixture_type") == "INVALID_MUTATION", "FIXTURE_TYPE_INVALID", "invalid descriptor")
    base_name = descriptor.get("base")
    require(isinstance(base_name, str) and Path(base_name).name == base_name, "FIXTURE_BASE_INVALID", str(base_name))
    document = copy.deepcopy(load_json(EXAMPLES / base_name))
    for mutation in descriptor.get("mutations", []):
        parent, key = resolve_pointer(document, mutation.get("path", ""))
        operation = mutation.get("operation")
        if operation == "replace":
            if isinstance(parent, list):
                parent[int(key)] = mutation.get("value")
            else:
                require(key in parent, "MUTATION_TARGET_MISSING", mutation["path"])
                parent[key] = mutation.get("value")
        elif operation == "append":
            target = parent[int(key)] if isinstance(parent, list) else parent[key]
            require(isinstance(target, list), "MUTATION_TARGET_NOT_ARRAY", mutation["path"])
            target.append(mutation.get("value"))
        else:
            fail("MUTATION_OPERATION_INVALID", str(operation))
    return document


def main() -> int:
    definition_schema = load_json(ROOT / "sop-definition.schema.json")
    execution_schema = load_json(ROOT / "sop-execution-instance.schema.json")
    validate_schema_document(definition_schema, "sop-definition.schema.json")
    validate_schema_document(execution_schema, "sop-execution-instance.schema.json")
    print("PASS schema sop-definition.schema.json")
    print("PASS schema sop-execution-instance.schema.json")

    schemas = {
        "SOP_DEFINITION": definition_schema,
        "SOP_EXECUTION_INSTANCE": execution_schema,
    }
    validators = {
        "SOP_DEFINITION": validate_definition,
        "SOP_EXECUTION_INSTANCE": validate_execution,
    }
    manifest = load_json(EXAMPLES / "manifest.json")
    passed = 2

    for case in manifest["valid"]:
        data = load_json(EXAMPLES / case["file"])
        validators[case["kind"]](data, schemas[case["kind"]])
        print(f"PASS valid {case['file']}")
        passed += 1

    for case in manifest["invalid"]:
        descriptor = load_json(EXAMPLES / case["file"])
        require(descriptor.get("expected_error") == case["expected_error"], "MANIFEST_EXPECTATION_MISMATCH", case["file"])
        data = materialize_invalid_fixture(descriptor)
        try:
            validators[case["kind"]](data, schemas[case["kind"]])
        except ContractError as error:
            require(
                error.code == case["expected_error"],
                "UNEXPECTED_ERROR_CODE",
                f"{case['file']}: expected {case['expected_error']}, got {error.code}",
            )
            print(f"PASS invalid {case['file']} -> {error.code}")
            passed += 1
        else:
            fail("INVALID_FIXTURE_ACCEPTED", case["file"])

    total = 2 + len(manifest["valid"]) + len(manifest["invalid"])
    print(f"RESULT {passed}/{total} checks passed")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ContractError, FileNotFoundError, json.JSONDecodeError, KeyError, TypeError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        raise SystemExit(1)
