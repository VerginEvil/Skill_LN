# Get attribute value

## Syntax:
`function string xmlAttribute$( long node, string attributeName, [ ref string default.value ] )`

## Description
Get an attribute of an XML_ELEMENT or XML_DTD node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the attribute is obtained.  |
| `string` | `attributeName` |  *attributeName* is the name of the attribute.  |
| `[ ref string` | `default.value ]` |  *default.value* is the value that will be returned by xmlAttribute$ when the *node* is invalid or does not have an attribute with the specified name. When *default.value* is not specified, an empty string is used.  |

## Return values
| | |
|---|---|
|  | A temporary multibyte string with the value of the specified attribute.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
