# Get number of sibling Nodes

## Syntax:
`function long xmlGetNumSiblings( long node )`

## Description
Get the total number of sibling nodes.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the number of siblings is returned.  |

## Return values
| | |
|---|---|
| > 0 | Success; Number of sibling nodes found. |
| 0 | When an error occurred or when node does not have any siblings. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
