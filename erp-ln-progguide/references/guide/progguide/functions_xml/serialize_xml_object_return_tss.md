# Serialize XML Object to Returned Tss String

## Syntax:
`function string xmlStringTss$( long fromNode, [ long toNode ] )`

## Description
Serialize an XML object and write the resulting unformatted XML document to an in-memory string. Any TSS encoded string information in the XML object is also encoded in TSS in the XML document.
Use [xmlString$](serialize_xml_object_return.md) instead to serialize the XML object to an unformatted UTF-8 encoded XML document.

## Arguments
| | | |
|---|---|---|
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See fromNode and toNode.  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See fromNode and toNode.  |

## Return values
A temporary multibyte string with the resulting TSS encoded unformatted XML document. An empty string is returned if there is not enough temporary memory available for the result, or if the serialization fails.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
