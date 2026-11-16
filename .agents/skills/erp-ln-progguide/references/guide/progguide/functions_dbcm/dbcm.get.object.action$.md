# dbcm.get.object.action$()

## Syntax:
`function string dbcm.get.object.action$( )`

## Description
Returns the currently selected object action (as selected with [dbcm.select.object.action()](dbcm.select.object.action.md)), or an empty string in case no object action has been selected.

## Return values
The currently selected object action, or an empty string in case no object action is set.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
