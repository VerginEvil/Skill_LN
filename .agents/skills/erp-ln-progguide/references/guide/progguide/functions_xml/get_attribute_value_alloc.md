# Get attribute value

## Syntax:
`function long xmlAllocAttribute( ref string basedString(), long node, string attributeName, string default.value )`

## Description
Get an attribute of an XML_ELEMENT or XML_DTD node.

## Arguments
| | | |
|---|---|---|
| `ref string` | `basedString()` |  *basedString* is a based string buffer (either or not multibyte) which will implicitly be allocated to the correct size (see [alloc.mem()](../functions_memory_operations/alloc.mem.md)) and will be filled with the attribute value.  |
| `long` | `node` |  *node* is the node for which the attribute is obtained.  |
| `string` | `attributeName` |  *attributeName* is the name of the attribute.  |
| `string` | `default.value` |  *default.value* is the value that will be returned by xmlAttribute$ or will be stored in *basedString* when the *node* is invalid or does not have an attribute with the specified name. When *default.value* is not specified, an empty string is used.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error: the supplied *basedString* argument is not a based string. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
