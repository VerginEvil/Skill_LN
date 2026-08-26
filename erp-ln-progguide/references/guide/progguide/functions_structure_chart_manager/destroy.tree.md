# destroy.tree()

## Syntax:
`function void destroy.tree( string tree_name, [ long process_id ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This ends the Structure Chart Manager for the specified tree.

## Arguments
| | | |
|---|---|---|
| `string` | `tree_name` |  The name of the tree that you want to kill.  |
| `[ long` | `process_id ]` |  This optional argument indicates the process ID of the tree that you want to end, as returned by [create.tree()](create.tree.md). If you do not include this argument, all trees with the name *tree_name* are killed.  |

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Structure Chart Manager overview](overview.md)
- [Structure ChartManager synopsis](synopsis.md)
- [Tree structures: example](example.md)
