# dbcm.reject()

## Syntax:
`function long dbcm.reject( const string toid$, const string reason$ )`

## Description
Rejects any changes and/or actions done to the checked-out business object that is identified by the given Typed Object Id and sets the given reason for rejecting.
This is possible for *Pending* objects (which will then become Rejected), and for objects having the status *Recall Requested* (which will then become Pending again).
This function is typically used in the communication between ION Workflow and Infor LN when processing BODs.

## Arguments
| | | |
|---|---|---|
| `const string` | `toid$` |  A Typed Object Id.  |
| `const string` | `reason$` |  A text stating the reason for rejecting the previous changes and/or actions made on the object.  |

## Return values
| | |
|---|---|
| 0 | In case of success. |
| `DBCM_INVALID_STATE` (-1) | The object is in a state in which it is not allowed to perform a reject. |
| > 0 | A database error occurred. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
