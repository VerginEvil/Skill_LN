# Get attribute name

## Syntax:
`function string xmlAttributeName$( long node, long attributeNr, [ string default.value ] )`

## Description
Get an attribute name of an XML_ELEMENT or XML_DTD node by specifying its position.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the attribute name is obtained.  |
| `long` | `attributeNr` |  *attributeNr* is the 1 based index in the list of attributes for this node.  |
| `[ string` | `default.value ]` |  *default.value* is the value that will be returned by xmlAttributeName$ or will be stored in *basedString* when the *node* or the *attributeNr* is invalid. When *default.value* is not specified, an empty string is used.  |

## Return values
| | |
|---|---|
|  | A temporary multibyte string with the name of the specified attribute.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
