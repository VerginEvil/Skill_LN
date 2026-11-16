# set.tree.linewidth()

## Syntax:
`function void set.tree.linewidth( string tree_name, long visible_level, long linewidth, [ long process_id ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This changes the line width (in pixels) used for nodes at a particular level in a specified tree. The default line widths are:
level 1 – 4 pixels
level 2 – 2 pixels
level 3 – 1 pixel
level 4 – 1 pixel

## Arguments
| | | |
|---|---|---|
| `string` | `tree_name` |  The name of the tree for which you want to change the line width.  |
| `long` | `visible_level` |  This is a number, in the range 1 to 3, that specifies the node level to which the new line width is to be applied. Visible level 1 specifies the highest level currently visible in the tree. Visible level 3 specifies levels three and below. See [view.tree()](view.tree.md).  |
| `long` | `linewidth` |  The new line width (in pixels) to be applied to the specified node level.  |
| `[ long` | `process_id ]` |  This optional argument indicates the process ID of the tree for which the line width must be changed. If you do not include this argument, the new line width is applied to the specified level in all trees with the name *tree_name*.  |

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Structure Chart Manager overview](overview.md)

- [Structure ChartManager synopsis](synopsis.md)

- [Tree structures: example](example.md)
