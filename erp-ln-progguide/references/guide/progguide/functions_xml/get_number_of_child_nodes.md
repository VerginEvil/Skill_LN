# Get number of child Nodes

## Syntax:
`function long xmlGetNumChilds( long node )`

## Description
Get the number of child nodes of an XML_ELEMENT or XML_DTD node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the number of child nodes is obtained.  |

## Return values
| | |
|---|---|
| > 0 | Success; The number of child nodes. |
| 0 | Error or no child nodes present. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
