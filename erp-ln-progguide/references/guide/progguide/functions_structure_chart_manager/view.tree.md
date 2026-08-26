# view.tree()

## Syntax:
`function void view.tree( string tree_name, string node_id, long depth, [ long process_id ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This changes which levels are visible in a specified tree.

## Arguments
| | | |
|---|---|---|
| `string` | `tree_name` |  The name of the tree whose visible levels you want to change.  |
| `string` | `node_id` |  This specifies the ID of node that you want to become the new root node of the visible part of the tree.  |
| `long` | `depth` |  This specifies the number of levels that you want to be visible. The recommended number of visible levels is four.  |
| `[ long` | `process_id ]` |  This optional argument indicates the process ID of the tree whose visible levels you want to change. If you do not include this argument, the new settings are applied to all trees with the name *tree_name*.  |

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Structure Chart Manager overview](overview.md)
- [Structure ChartManager synopsis](synopsis.md)
- [Tree structures: example](example.md)
