# Get attribute name

## Syntax:
`function long xmlGetAttributeName( long node, long attributeNr, ref string attributeName )`

## Description
Get an attribute name of an XML_ELEMENT or XML_DTD node by specifying its position.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the attribute name is obtained.  |
| `long` | `attributeNr` |  *attributeNr* is the 1 based index in the list of attributes for this node.  |
| `ref string` | `attributeName` |    |

## Return values
| | |
|---|---|
| <> 0 | Success; Value of parameter *node* when successful. |
| 0 | Error or the indicated attribute does not exist. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related
```

long	xmlGetAttributeName(long node, long attributeNr, ref string attributeName)
string	xmlAttributeName$(long node, long attributeNr, [ string default.value ] )
long	xmlAllocAttributeName(ref string basedString(), long node, long attributeNr,[ string default.value ] )
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
