# Get number of attributes

## Syntax:
`function long xmlGetNumAttributes( long node )`

## Description
Get the number of attributes of an XML_ELEMENT or XML_DTD node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the number of attributes is returned.  |

## Return values
| | |
|---|---|
| > 0 | Success; Number of attributes for *node*. |
| 0 | Error or no attributes are present for *node*. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
