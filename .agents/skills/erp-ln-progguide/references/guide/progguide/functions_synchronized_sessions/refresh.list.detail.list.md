# refresh.list.detail.list()

## Syntax:
`function void refresh.list.detail.list( )`

## Description
This function refreshes the list of a list-detail session. On an user update action the list is automatically updated. But if an update of a record is done outside the save action, on a form command action or in another session (satellite), the list is not automatically updated. In these situations this function can be used to refresh the list.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2350.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Synchronized sessions synopsis](synopsis.md)
