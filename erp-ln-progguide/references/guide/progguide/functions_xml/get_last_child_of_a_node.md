# Get last child of a Node

## Syntax:
`function long xmlGetLastChild( long node )`

## Description
Get the last (most right) child node of an XML_ELEMENT or XML_DTD node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  node is the node for which the last child is obtained.  |

## Return values
| | |
|---|---|
| <> 0 | Success; Reference to the found child *node* when successful.  |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
