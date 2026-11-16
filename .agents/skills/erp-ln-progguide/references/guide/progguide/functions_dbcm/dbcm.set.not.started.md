# dbcm.set.not.started()

## Syntax:
`function long dbcm.set.not.started( const string toid$ )`

## Description
Assigns the *Not Started* status to the checked-in Business Object that is identified by the given Typed Object Id and has the *Approved* status. This indicates that a previous request to recall the already started workflow process has been processed and acknowledged.
This function is primarily intended for an object with the status *Approved*. However, it can also be called for an object with the status *Not Applicable*. In that case the function does change the status of the object but will still return value 0.
This function is typically used in a UI-session.

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
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
