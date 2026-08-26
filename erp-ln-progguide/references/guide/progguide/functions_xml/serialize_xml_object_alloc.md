# Serialize XML Object to Based String

## Syntax:
`function long xmlAllocString( ref string basedString$, long fromNode, [ long toNode ] )`

## Description
Serialize an XML object and write the resulting unformatted XML document to an in-memory string. Any TSS encoded string information in the XML object is encoded in UTF-8 in the XML document.
Use [xmlAllocPrettyString](serialize_xml_object_alloc_pretty.md) instead to serialize the XML object to a formatted XML document.

## Arguments
| | | |
|---|---|---|
| `ref string` | `basedString$` |  Ref string argument that receives the UTF-8 encoded unformatted XML document. As its contents will not be encoded in TSS, it is desirable that this argument is of type string, rather than type multibyte string. The argument must be declared as BASED. It is implicitly allocated to the correct size (see [alloc.mem](../functions_memory_operations/alloc.mem.md)).  |
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See fromNode and toNode.  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See fromNode and toNode.  |

## Return values
| | |
|---|---|
| 0 | Success. Even if the serialization fails, this value is returned. In that case *basedString$* will be an empty string.  |
| 1 | Error: the supplied *basedString$* argument is not a based string.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
