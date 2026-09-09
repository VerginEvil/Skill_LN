# dbcm.is.action.active()

## Syntax:
`function boolean dbcm.is.action.active( )`

## Description
Tests whether the currently selected object action (as selected with [dbcm.select.object.action()](dbcm.select.object.action.md)) is active according to the Object Configuration Management deployment.

## Return values
| | |
|---|---|
| true | The currently selected object action is active. |
| false | In any other case. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
