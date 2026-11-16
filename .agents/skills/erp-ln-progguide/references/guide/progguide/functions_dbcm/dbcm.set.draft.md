# dbcm.set.draft()

## Syntax:
`function long dbcm.set.draft( const string toid$ )`

## Description
Assigns the *Draft* status to the checked-out Business Object that is identified by the given Typed Object Id.
This is only allowed for objects that have the *Approval Received* or *Rejected* status.
This function is typically used in the communication between ION Workflow and Infor LN when processing BODs.

## Arguments
| | | |
|---|---|---|
| `const string` | `toid$` |  A Typed Object Id.  |

## Return values
| | |
|---|---|
| 0 | In case of success. |
| `DBCM_INVALID_STATE` (-1) | The object is in a state in which it is not allowed to perform this function. |
| > 0 | A database error occurred. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
