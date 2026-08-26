# dbcm.get.cm.action$()

## Syntax:
`function string dbcm.get.cm.action$( const string toid$ )`

## Description
Retrieves the Change Management action id of the Object that is identified by the given Typed Object Id.

## Arguments
| | | |
|---|---|---|
| `const string` | `toid$` |  A Typed Object Id; this is a string of 34 characters identifying a business object.  |

## Return values
The action id of the Object as string; or an empty string in case the Object is not checked-out.
For the standard actions UI Create, UI Change and UI Delete, the action ids are predefined:
- `DBCM_ACTION_CREATE`
- `DBCM_ACTION_CHANGE`
- `DBCM_ACTION_DELETE`

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
