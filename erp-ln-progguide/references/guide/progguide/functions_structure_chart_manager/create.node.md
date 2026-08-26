# create.node()

## Syntax:
`function void create.node( string tree_name, string parent_id, string node_id, string node_desc, long node_class, [ long process_id ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This adds a new node to a specified tree. The *node_id*, together with the *parent_id,* determine where the new node is located in the tree.

## Arguments
| | | |
|---|---|---|
| `string` | `tree_name` |  The name of the tree to which the node must be added.  |
| `string` | `parent_id` |  The ID of the parent node. Specify an empty string as the parent ID for the root node.  |
| `string` | `node_id` |  The ID for the new node.  |
| `string` | `node_desc` |  A description for the node. This is the label displayed for the node in the tree structure.  |
| `long` | `node_class` |  This is a number, in the range 1 to 9, that indicates the node class that must assigned to the node. The node class determines the color in which a node is displayed. You can subsequently assign a different class to the node by calling [set.node.class()](set.node.class.md). You use [set.node.class.color()](set.node.class.color.md) to define node classes.  |
| `[ long` | `process_id ]` |  This optional argument indicates the process ID of the server to which the node must be added, as returned by [create.tree()](create.tree.md). If you do not include this argument, the node is added to all servers with the name specified in *tree_name*.  |

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Structure Chart Manager overview](overview.md)
- [Structure ChartManager synopsis](synopsis.md)
- [Tree structures: example](example.md)
