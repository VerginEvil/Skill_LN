# dbcm.get.object.id$()

## Syntax:
`function string dbcm.get.object.id$( )`

## Description
Returns the id of the currently selected object instance (as selected with [dbcm.select.object.instance()](dbcm.select.object.instance.md)), or an empty string in case no object instance is selected or if a previously selected object instance is out of scope.

## Return values
The id of the currently selected object instance, or an empty string in case no object instance is set.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
