# Get number of left sibling Nodes

## Syntax:
`function long xmlGetNumLeftSiblings( long node )`

## Description
Get the number of left sibling nodes.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the number of left siblings is returned.  |

## Return values
| | |
|---|---|
| > 0 | Success; Number of left sibling nodes found. |
| 0 | When an error occurred or when node does not have any left siblings. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
