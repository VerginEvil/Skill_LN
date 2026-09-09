# dbcm.set.workflow.definition()

## Syntax:
`function long dbcm.set.workflow.definition( const string toid$, const string wf.def$ )`

## Description
Sets the workflow definition id of the checked-out business object that is identified by the given Typed Object Id. This id is a reference to a Workflow Process Definition in ION Workflow. On submit (and in case ION Workflow should be involved), an instance of this process will be started in ION Workflow.
This function should only be called in case the status of the object is *Draft*, *Draft (Revision)*, or *Rejected*.
This function is typically used in the communication between ION Workflow and Infor LN when publishing BODs.

## Arguments
| | | |
|---|---|---|
| `const string` | `toid$` |  A Typed Object Id.  |
| `const string` | `wf.def$` |  A workflow definition id. This is a reference to a Workflow Process definition in ION Workflow.  |

## Return values
| | |
|---|---|
| 0 | In case of success. |
| `DBCM_INVALID_STATE` (-1) | The object is in a state in which it is not allowed to perform this function. |
| > 0 | A database error occurred. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
