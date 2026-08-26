# refresh.tree.detail.tree()

## Syntax:
`function void refresh.tree.detail.tree( )`

## Description
This function refreshes the tree of a tree-detail session. On an user update action on the detail session the tree is automatically updated. But if an update of a record is done outside the save action, on a form command action or in another session (satellite), the tree is not automatically updated. In that situation this function can be used to refresh the tree.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2350.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Synchronized sessions synopsis](synopsis.md)
