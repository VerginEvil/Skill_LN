# Serialize XML Object to Returned Formatted String

## Syntax:
`function string xmlPrettyString$( long fromNode, [ long toNode ] )`

## Description
Serialize an XML object and write the resulting formatted XML document to an in-memory string. Any TSS encoded string information in the XML object is encoded in UTF-8 in the XML document.
The XML document is formatted by adding new-lines and tabs in order to show its structure: nested nodes with string-valued attributes. Use [xmlString$](serialize_xml_object_return.md) instead to serialize the XML object to an unformatted XML document.

## Arguments
| | | |
|---|---|---|
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See fromNode and toNode.  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See fromNode and toNode.  |

## Return values
A temporary single byte string with the resulting UTF-8 encoded formatted XML document. An empty string is returned if there is not enough temporary memory available for the result, or if the serialization fails.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
