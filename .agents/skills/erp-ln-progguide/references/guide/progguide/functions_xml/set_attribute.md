# Set attribute

## Syntax:
`function long xmlSetAttribute( long node, string attributeName, void data )`

## Description
Set an attribute of an XML_ELEMENT or XML_DTD node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the attribute is set.  |
| `string` | `attributeName` |  *attributeName* is the name of the attribute. When this attribute does already exist for this node, it gets a new value, else a new attribute is added to this node. This guarantees that attribute names are always unique for a given node.  |
| `void` | `data` |  *data* contains the new attribute value.  |

## Return values
| | |
|---|---|
| <> 0 | Success; Value of parameter *node* when successful |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
