# dbcm.set.object.type()

## Syntax:
`function long dbcm.set.object.type( const string obj.type$ )`

## Description
Sets the specified Object Type in a 4GL session.
This function allows you to overrule the Object Type that would normally be selected when the session starts. Normally the Object Type that is returned by the function [dbcm.get.type.name()](dbcm.get.type.name.md)) will be selected.
Important Note  Use this function only in the before.program section.

## Arguments
| | | |
|---|---|---|
| `const string` | `obj.type$` |  An object type code as defined in the Object Configuration Management model. This is a string of max 6 characters.  |

## Return values
| | |
|---|---|
| 0 | In case of success. |
| <> 0 | In case of an error; variable *e* contains the error code. See [Database Change Management (DBCM) error codes](error_codes.md) for more information about the error codes and their meaning.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
