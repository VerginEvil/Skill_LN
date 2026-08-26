# dbcm.get.user()

## Syntax:
`function long dbcm.get.user( const string toid$, ref string user$ )`

## Description
Retrieves the user who last 'touched' the Business object which is identified by the specified type object id.
In case the Business Object is Draft, this is the user who caused the check-out of this Object.
Once the Business Object is Submitted, this is the user who did Submit the changes.

## Arguments
| | | |
|---|---|---|
| `const string` | `toid$` |  A Typed Object Id. A Typed Object Id is a string of 34 characters identifying a checked-out business object.  |
| `ref string` | `user$` |  The returned user code. In case of an error this parameter is not reset.  |

## Return values
| | |
|---|---|
| 0 | The user code is retrieved successfully. |
| ENOREC | The object cannot be found; probably the object is not checked-out. |
| <> 0 | Any other database error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
