# Get attribute value

## Syntax:
`function long xmlGetAttribute( long node, string attributeName, ref void data )`

## Description
Get an attribute of an XML_ELEMENT or XML_DTD node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the attribute is obtained.  |
| `string` | `attributeName` |  *attributeName* is the name of the attribute.  |
| `ref void` | `data` |  *data* is a parameter which contains the attribute value on return. The function [Get attribute length](get_attribute_length.md) may be used to determine the required size of *data*.  |

## Return values
| | |
|---|---|
| <> 0 | Success; Value of parameter *node* when successful.  |
| 0 | Error or the indicated attribute does not exist. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related
```

long	xmlGetAttribute(long node, string attributeName, ref string data)
string	xmlAttribute$(long node, string attributeName, [ string default.value ] )
long	xmlAllocAttribute(ref string basedString(), long node, string attributeName, [ string default.value ] )
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
