# set.node.class()

## Syntax:
`function void set.node.class( string tree_name, string node_id, long node_class, [ long process_id ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
Use this function to assign a different class to a particular node. The node class determines the color in which a node is displayed.

## Arguments
| | | |
|---|---|---|
| `string` | `tree_name` |  The name of the tree to which the specified node belongs.  |
| `string` | `node_id` |  The ID of the node to which you want to assign a new class.  |
| `long` | `node_class` |  This is a number, in the range 1 to 9, that indicates the node class that must assigned to the node. You use [set.node.class.color()](set.node.class.color.md) to define node classes.  |
| `[ long` | `process_id ]` |  This optional argument indicates the process ID of the tree for which you want to change the class of the specified node. If you do not include this argument, the node class is changed for the specified node in all trees with the name *tree_name*.  |

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Structure Chart Manager overview](overview.md)

- [Structure ChartManager synopsis](synopsis.md)

- [Tree structures: example](example.md)
