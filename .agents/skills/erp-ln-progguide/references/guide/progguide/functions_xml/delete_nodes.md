# Delete Nodes

## Syntax:
`function long xmlDelete( long fromNode, [ long toNode ] )`

## Description
Delete a tree or a list of trees. When this tree is a sub-tree of a larger tree, it is unlinked from this larger tree.

## Arguments
| | | |
|---|---|---|
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See [fromNode and toNode](api.md#fromnode_tonode).  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See [fromNode and toNode](api.md#fromnode_tonode).  |

## Return values
| | |
|---|---|
| 0 | Success. |
| < 0 | When an error occurred. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
