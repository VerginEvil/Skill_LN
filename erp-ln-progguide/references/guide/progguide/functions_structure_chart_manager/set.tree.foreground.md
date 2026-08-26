# set.tree.foreground()

## Syntax:
`function void set.tree.foreground( string tree_name, long color, [ long process_id ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This changes the foreground color of a specified tree.

## Arguments
| | | |
|---|---|---|
| `string` | `tree_name` |  The name of the tree whose foreground color you want to change.  |
| `long` | `color` |  This specifies the new foreground color for the tree. The value can be a number returned by the [rgb()](../functions_color/rgb.md) function or one of the following predefined colors: RGB.BLACK RGB.MAGENTA RGB.RED RGB.BLUE RGB.GREEN RGB.WHITE RGB.YELLOW RGB.GRAY RGB.CYAN  |
| `[ long` | `process_id ]` |  This optional argument indicates the process ID of the tree whose foreground color you want to change. If you do not include this argument, the new foreground color is applied to all trees with the name *tree_name*.  |

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Structure Chart Manager overview](overview.md)
- [Structure ChartManager synopsis](synopsis.md)
- [Tree structures: example](example.md)
