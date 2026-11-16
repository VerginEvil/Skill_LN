# set.node.class.color()

## Syntax:
`function void set.node.class.color( string tree_name, long node_class, long class_color, [ long process_id ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
The node class assigned to a node determines the color in which the node is displayed. You use this function to define the color for a specified node class. You use [set.node.class()](set.node.class.md) to assign a class to a particular node.

## Arguments
| | | |
|---|---|---|
| `string` | `tree_name` |  The name of the tree for which the node class must be defined.  |
| `long` | `node_class` |  This is the identifier of the node class. It can be any number in the range 1 to 9.  |
| `long` | `class_color` |  This specifies the color for the node class. It consists of either a number returned by the [rgb()](../functions_color/rgb.md) function or one of the following predefined colors: RGB.BLACK RGB.MAGENTA RGB.RED RGB.BLUE RGB.GREEN RGB.WHITE RGB.YELLOW RGB.GRAY RGB.CYAN  |
| `[ long` | `process_id ]` |  This optional argument indicates the process ID of the tree for which the node class must be defined. If you do not include this argument, the new color is assigned to the specified node class in all trees with the name *tree_name*.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Structure Chart Manager overview](overview.md)

- [Structure ChartManager synopsis](synopsis.md)

- [Tree structures: example](example.md)
