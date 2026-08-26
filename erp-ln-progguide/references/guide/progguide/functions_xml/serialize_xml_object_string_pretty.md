# Serialize XML Object to Formatted String

## Syntax:
`function long xmlWritePrettyToString( ref string buffer$, long fromNode, [ long toNode ] )`

## Description
Serialize an XML object and write the resulting formatted XML document to an in-memory string. Any TSS encoded string information in the XML object is encoded in UTF-8 in the XML document.
The XML document is formatted by adding new-lines and tabs in order to show its structure: nested nodes with string-valued attributes. Use [xmlWriteToString](serialize_xml_object_string.md) instead to serialize the XML object to an unformatted XML document.

## Arguments
| | | |
|---|---|---|
| `ref string` | `buffer$` |  Ref string argument that receives the UTF-8 encoded formatted XML document. As its contents will not be encoded in TSS, it is desirable that this argument is of type string, rather than type multibyte string. The function [xmlGetPrettyStringLength()](get_serialize_length_pretty.md) may be used to determine the required size of the buffer.  |
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See fromNode and toNode.  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See fromNode and toNode.  |

## Return values
| | |
|---|---|
| >= 0 | Success; Number of bytes written to output when successful  |
| < 0 |  Error. As many bytes as possible are written to the ref string *buffer$* argument. If the cause of the error is not that the *buffer$* is too small, then the exact place where the output of bytes stops, corresponds to the place in the XML tree where the first serialization error occurred. Some specific values:  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
