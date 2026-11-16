# dbcm.select.session.object.type()

## Syntax:
`function long dbcm.select.session.object.type( const string obj.type$ )`

## Description
Selects the specified Object Type for the complete session.
When a particular Object Type is selected, checked-out objects of that type are taken into account, when the database is accessed.
Important Note  The selected object type remains selected until the end of the session.
This function must only be used in the before.program section of a UI-script and must only used if the session does not have a main table or the session has a main table that is not CM enabled.

## Arguments
| | | |
|---|---|---|
| `const string` | `obj.type$` |  An object type code as defined in the Object Configuration Management model. This is a string of max 6 characters.  |

## Return values
| | |
|---|---|
| 0 | In case of success. |
| <> 0 | In case of an error; variable *e* contains the error code. See [Database Change Management (DBCM) error codes](error_codes.md) for more information about the error codes and their meaning. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2461.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
