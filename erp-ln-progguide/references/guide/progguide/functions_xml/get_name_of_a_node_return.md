# Get name of a Node

## Syntax:
`function string xmlName$( long node, [ string default.value ] )`

## Description
Get the name of an XML_ELEMENT or XML_DTD node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the name is obtained.  |
| `[ string` | `default.value ]` |  *default.value* is the value that will be returned by xmlName$ or will be stored in *basedString* when the *node* is invalid. When *default.value* is not specified, an empty string is used.  |

## Return values
| | |
|---|---|
|  | A temporary multibyte string with the name of the specified node. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related
```

long	xmlGetName(long node, ref string name)
string	xmlName$(long node, [ string default.value ] )
long	xmlAllocName(ref string basedString(), long node, [ string default.value ] )
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
