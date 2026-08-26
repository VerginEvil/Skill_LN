# Serialize XML Object (xmlWrite)

## Syntax:
`function long xmlWrite( long fp, long fromNode, [ long toNode ] )`

## Description
Serialize an XML object and write the resulting unformatted XML document to an open stream. Any TSS encoded string information in the XML object is encoded in UTF-8 in the XML document.
Use [xmlWritePretty](serialize_xml_object_pretty.md) instead to serialize the XML object to a formatted XML document.

## Arguments
| | | |
|---|---|---|
| `long` | `fp` |  *fp* must be a file pointer opened for write obtained from a call to seq.open(), pipe.open(), ims.openfba() or ims.openvba().  |
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See fromNode and toNode.  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See fromNode and toNode.  |

## Return values
| | |
|---|---|
| >= 0 | Success; Number of bytes written to output when successful  |
| < 0 |  Error. As many bytes as possible are written to *fp*. The place where the output of bytes stops, corresponds to the place in the XML tree where the first serialization error occurred. Some specific values:  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
