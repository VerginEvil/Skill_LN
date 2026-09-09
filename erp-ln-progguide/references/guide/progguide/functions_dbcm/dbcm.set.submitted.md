# dbcm.set.submitted()

## Syntax:
`function long dbcm.set.submitted( const string toid$, const string wf.id$ )`

## Description
Sets the workflow instance id of the checked-out business object that is identified by the given Typed Object Id. This indicates that a previous submit has been confirmed and that the Workflow has been started.
This function should only be called in case the status of the object is *Pending*.
This function is typically used in the communication between ION Workflow and Infor LN when processing BODs.

## Arguments
| | | |
|---|---|---|
| `const string` | `toid$` |  A Typed Object Id.  |
| `const string` | `wf.id$` |  A workflow instance id as received from ION Workflow. This is a reference to the Workflow Process that has been started in ION.  |

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
