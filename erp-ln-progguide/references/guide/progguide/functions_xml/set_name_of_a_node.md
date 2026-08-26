# Set name of a Node

## Syntax:
`function long xmlSetName( long node, string name )`

## Description
Set the name of an XML_ELEMENT or XML_DTD node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the name is set.  |
| `string` | `name` |  *name* contains the new name.  |

## Return values
| | |
|---|---|
| <> 0 | Success; Value of parameter *node* when successful.  |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
