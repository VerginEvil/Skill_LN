# Get name of a Node

## Syntax:
`function long xmlAllocName( ref string basedString, long node, [ string default.value ] )`

## Description
Get the name of an XML_ELEMENT or XML_DTD node.

## Arguments
| | | |
|---|---|---|
| `ref string` | `basedString` |  *basedString* is a based string buffer (either or not multibyte) which will implicitly be allocated to the correct size (see [alloc.mem()](../functions_memory_operations/alloc.mem.md)) and will be filled with the node name.  |
| `long` | `node` |  *node* is the node for which the name is obtained.  |
| `[ string` | `default.value ]` |  *default.value* is the value that will be returned by xmlName$ or will be stored in *basedString* when the *node* is invalid. When *default.value* is not specified, an empty string is used.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error: the supplied *basedString* argument is not a based string.  |

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
