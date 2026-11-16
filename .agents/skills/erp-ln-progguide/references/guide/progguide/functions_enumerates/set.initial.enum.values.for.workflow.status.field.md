# set.initial.enum.values.for.workflow.status.field()

## Syntax:
`function void set.initial.enum.values.for.workflow.status.field( long ALL_ENUMS_EXCEPT, enum workflow_status,... )`

## Description
This function applies to a workflow status field that is displayed as listbox. It limits the number of workflow statuses to the specified set. Any workflow status not specified will be *hidden*. Function set.initial.enum.values.for.workflow.status.field is equivalent to [set.initial.enum.values.for.field()](set.initial.enum.values.for.field.md) with the field.name argument set to “ttocm999.stts”

## Arguments
| | | |
|---|---|---|
| `long` | `ALL_ENUMS_EXCEPT` |  This optional macro specifies that the succeeding list of workflow statuses represents those statuses that are to be *excluded*. Otherwise, the list of workflow statuses represents the statuses that are to be *included*.  |
| `enum` | `workflow_status,...` |  The workflow statuses to be displayed on the form, separated by commas [,]. This is an optional argument. If not included, all workflow statuses are available. There are 9 workflow statuses predefined. Use these predefined statuses by specifying: DBCM_STATUS_NOT_STARTED DBCM_STATUS_DRAFT DBCM_STATUS_DRAFT_REV DBCM_STATUS_PENDING DBCM_STATUS_RECALL_REQ DBCM_STATUS_REJECTED DBCM_STATUS_APPRV_RECVD DBCM_STATUS_APPROVED DBCM_STATUS_NOT_APPL  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2150.
Notes  This function can only be called in the *after.form.read* section. Refer to function [set.initial.enum.values.for.field()](set.initial.enum.values.for.field.md) for additional information.

## Example
```

after.form.read:
        if SOME_CONDITION then
			set.initial.enum.values.for.workflow.status.field(
                       DBCM_STATUS_NOT_STARTED, DBCM_STATUS_DRAFT, DBCM_STATUS_PENDING,
                       DBCM_STATUS_REJECTED, DBCM_STATUS_APPROVED, DBCM_STATUS_NOT_APPL)
		| Session only works with specified workflow statuses
        endif
```

## Related topics
- [Enumerates overview and synopsis](overview_and_synopsis.md)

- [Enumerate and set constants](../3gl_features/enumerate_and_set_constants.md)
