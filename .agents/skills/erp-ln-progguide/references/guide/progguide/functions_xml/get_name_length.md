# Get name length of a node

## Syntax:
`function long xmlGetNameLength( long node )`

## Description
Get the length of a node name.
This function may be used to determine the required size of the *name* argument supplied to [Get name of a Node](get_name_of_a_node.md).

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the length of its name is obtained.  |

## Return values
| | |
|---|---|
| >= 0 | Success; Length of the node name |
| -1 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
