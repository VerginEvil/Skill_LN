# dbcm.get.object.type$()

## Syntax:
`function string dbcm.get.object.type$( )`

## Description
Returns the currently selected object type (as selected with [dbcm.select.object.type()](dbcm.select.object.type.md)), or an empty string in case no object type is selected or if the previously selected object type is out of scope.

## Return values
The currently selected object type, or an empty string in case no object type is set.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
