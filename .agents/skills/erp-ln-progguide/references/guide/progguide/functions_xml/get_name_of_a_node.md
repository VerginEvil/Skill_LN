# Get name of a Node

## Syntax:
`function long xmlGetName( long node, ref string name )`

## Description
Get the name of an XML_ELEMENT or XML_DTD node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the name is obtained.  |
| `ref string` | `name` |  *name* is a string buffer which contains the node name on return. The function xmlGetNameLengthname may be used to determine the required size of *name*.  |

## Return values
| | |
|---|---|
| <> 0 | Success; Value of parameter *node* when successful. |
| 0 | Error. |

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
