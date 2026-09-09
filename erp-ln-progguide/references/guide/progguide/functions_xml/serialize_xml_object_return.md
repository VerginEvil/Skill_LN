# Serialize XML Object to Returned String

## Syntax:
`function string xmlString$( long fromNode, [ long toNode ] )`
`function string xmlStringUtf8$( long fromNode, [ long toNode ] )`

## Description
Serialize an XML object and write the resulting unformatted XML document to an in-memory string. Any TSS encoded string information in the XML object is encoded in UTF-8 in the XML document.
Use [xmlPrettyString$](serialize_xml_object_return_pretty.md) instead to serialize the XML object to a formatted XML document.

## Arguments
| | | |
|---|---|---|
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See [fromNode and toNode](api.md#fromnode_tonode).  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See [fromNode and toNode](api.md#fromnode_tonode).  |

## Return values
A temporary single byte string with the resulting UTF-8 encoded unformatted XML document. An empty string is returned if there is not enough temporary memory available for the result, or if the serialization fails.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
