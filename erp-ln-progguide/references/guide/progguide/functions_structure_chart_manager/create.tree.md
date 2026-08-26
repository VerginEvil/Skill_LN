# create.tree()

## Syntax:
`function long create.tree( string tree_name, string tree_title )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This starts the Structure Chart Manager for a specified tree. It returns the process ID of the tree. If there is more than one tree with the same name, you can specify the process ID in the other functions in order to identify a particular tree. The process ID is the unique identifier of a tree.

## Arguments
| | | |
|---|---|---|
| `string` | `tree_name` |  The name of the tree to be started.  |
| `string` | `tree_title` |  The title of the tree. This is displayed in the main window.  |

## Return values
> 0 success; returns the process ID of the new tree
0 error

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  The tree structure is displayed only after you have called [view.tree()](view.tree.md).

## Related topics
- [Structure Chart Manager overview](overview.md)
- [Structure ChartManager synopsis](synopsis.md)
- [Tree structures: example](example.md)
