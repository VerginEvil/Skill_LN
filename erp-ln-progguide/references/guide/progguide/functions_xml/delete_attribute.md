# Delete attribute

## Syntax:
`function long xmlDeleteAttribute( long node, string attribute )`

## Description
Delete an attribute of an XML_ELEMENT or XML_DTD node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the attribute is deleted.  |
| `string` | `attribute` |  *attribute* is the name of the attribute to be deleted.  |

## Return values
| | |
|---|---|
| <> 0 | Success; Value of parameter *node* when successful. |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
