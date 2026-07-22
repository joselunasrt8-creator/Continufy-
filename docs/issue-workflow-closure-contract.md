# Issue Workflow Closure Contract

## Purpose

Prevent implemented code, completed contracts, frozen artifacts, execution records, and research outputs from becoming unmerged, unreachable, unverified, undocumented, or unowned.

An issue is not complete merely because work exists. It is complete only when the required artifact is integrated, verified, connected, and preserved according to its issue class.

## Universal workflow

```text
Owned Issue
        ↓
Produce Artifact or Change
        ↓
Merge, Freeze, or Publish
        ↓
Verify Required Properties
        ↓
Connect Downstream Consumer
        ↓
Preserve Evidence
        ↓
Record Terminal Determination
        ↓
Close
```

## Required issue metadata

Every issue must declare:

```text
Type:
Role:
Owner:
Parent anchor:
Upstream inputs:
Downstream consumer:
Blocked by:
Blocks:
Owned output:
Non-responsibilities:
Final determination:
Stopping rule:
```

## Code-producing issues

Required terminal outcome:

```text
MERGED_AND_CONNECTED
```

Required evidence:

```text
Repository:
Issue:
Owner:
Branch:
Commit:
Pull request:
Merged default-branch revision:
Declared entry point:
Required test or workflow:
Execution result:
Preserved evidence:
Documentation updated:
Downstream consumer:
Known limitations:
Follow-up issue:
```

Required reachability states:

```text
COMMIT_EXISTS
PR_OPENED
PR_MERGED
DEFAULT_BRANCH_CONTAINS_CHANGE
ENTRY_POINT_REACHABLE
REQUIRED_TEST_SELECTED
EXECUTION_SUCCEEDED
RESULT_PRESERVED
DOWNSTREAM_CONSUMER_NAMED
```

```text
Code Written
≠
Merged
≠
Reachable
≠
Executed
≠
Consumed
```

Non-terminal states:

```text
IMPLEMENTED_BUT_NOT_INTEGRATED
MERGED_BUT_NOT_EXECUTED
EXECUTED_BUT_NOT_CONSUMED
```

## Contract and documentation issues

Required terminal outcome:

```text
DOCUMENTATION_CONTRACT_COMPLETE
```

Required evidence:

```text
Canonical documents changed
Pull request merged
Default branch contains contract
Valid and invalid examples included
Owner boundary explicit
Downstream consumer references contract
Superseded definitions identified
Final determination recorded
```

Runtime execution is required only where explicitly part of the issue contract.

## Freeze issues

Required terminal outcome:

```text
FROZEN_FOR_REFERENCE_EXECUTION
```

Required evidence:

```text
Exact commit, tag, release, or immutable artifact identity
Canonical artifact list
Inputs and outputs
Accepted limitations
Deferred work
Repository-local determination
Continufy reference-manifest connection
```

## Execution issues

Required terminal outcomes:

```text
VALIDATED_BY_REFERENCE_EXECUTION
BLOCKED_WITH_PRESERVED_EVIDENCE
EXECUTION_INVALID
INDETERMINATE
```

Required evidence:

```text
Frozen input identity
Frozen method or instrument version
Execution identity
Produced outputs
Manual judgments
Negative and unresolved results
Stopping-rule application
Preserved execution record
Downstream routing
```

## Evaluation and calibration issues

Required terminal outcomes:

```text
EVALUATION_COMPLETE
NO_CHANGE_JUSTIFIED
REVISION_REQUIRED
BLOCKED_WITH_PRESERVED_EVIDENCE
```

Every recommendation must trace to execution evidence. Accepted changes require a separate future implementation issue and may not mutate a frozen execution.

## Synthesis and publication issues

Required terminal outcomes include:

```text
REPORT_PUBLISHED_AND_TRACEABLE
REFERENCE_CORPUS_FROZEN
PUBLICATION_ARTIFACT_COMPLETE
```

Every conclusion or included artifact must bind to immutable source evidence.

## Replication issues

Required terminal outcomes:

```text
REPRODUCED
REPRODUCED_WITH_LIMITATIONS
NOT_REPRODUCED
BLOCKED_WITH_PRESERVED_EVIDENCE
```

Replication packaging may close only when the surface is complete, versioned, and connected to a named reproduction or external-replication workflow.

## Universal closure rule

```text
No owner
or
No immutable result
or
No verification
or
No downstream connection
        ↓
Issue is not complete
```

Where a required field or state is genuinely inapplicable, the closure record must state why rather than omit it.
