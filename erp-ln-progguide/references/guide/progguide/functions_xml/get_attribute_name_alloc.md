# Get attribute name

## Syntax:
`function long xmlAllocAttributeName( ref string basedString(), long node, long attributeNr, [ string default.value ] )`

## Description
Get an attribute name of an XML_ELEMENT or XML_DTD node by specifying its position.

## Arguments
| | | |
|---|---|---|
| `ref string` | `basedString()` |  *node* is the node for which the attribute name is obtained.  |
| `long` | `node` |  *attributeNr* is the 1 based index in the list of attributes for this node.  |
| `long` | `attributeNr` |  *default.value* is the value that will be returned by xmlAttributeName$ or will be stored in *basedString* when the *node* or the *attributeNr* is invalid. When *default.value* is not specified, an empty string is used.  |
| `[ string` | `default.value ]` |  *basedString* is a based string buffer (either or not multibyte) which will implicitly be allocated to the correct size (see [alloc.mem()](../functions_memory_operations/alloc.mem.md)) and will be filled with the attribute name.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error: the supplied *basedString* argument is not a based string.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
