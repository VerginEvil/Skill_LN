# set.tree.name()

## Syntax:
`function void set.tree.name( string tree_name, string tree_title, [ long process_id ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This changes the title of a specified tree.

## Arguments
| | | |
|---|---|---|
| `string` | `tree_name` |  The name of the tree whose title you want to change.  |
| `string` | `tree_title` |  This specifies the new title for the tree.  |
| `[ long` | `process_id ]` |  This optional argument indicates the process ID of the tree whose title you want to change. If you do not include this argument, the new title is applied to all trees with the name *tree_name*.  |

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Structure Chart Manager overview](overview.md)
- [Structure ChartManager synopsis](synopsis.md)
- [Tree structures: example](example.md)
