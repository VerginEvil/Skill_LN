# Serialize XML Object Formatted

## Syntax:
`function long xmlWritePretty( long fp, long fromNode, [ long toNode ] )`

## Description
Serialize an XML object and write the resulting formatted XML document to an open stream. Any TSS encoded string information in the XML object is encoded in UTF-8 in the XML document.
The XML document is formatted by adding new-lines and tabs in order to show its structure: nested nodes with string-valued attributes. Use [xmlWrite](serialize_xml_object.md) instead to serialize the XML object to an unformatted XML document.

## Arguments
| | | |
|---|---|---|
| `long` | `fp` |  *fp* must be a file pointer opened for write obtained from a call to seq.open(), pipe.open(), ims.openfba() or ims.openvba().  |
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See [fromNode and toNode](api.md#fromnode_tonode).  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See [fromNode and toNode](api.md#fromnode_tonode).  |

## Return values
| | |
|---|---|
| -1 | Incorrect argument. For example, file pointer *fp* is closed, or *fromNode* or *toNode* is not a valid xml node. |
| -3 | Cannot write to *fp* (e.g. it is open for reading instead of writing), or a TSS conversion error occurred. If TSS conversion of a certain text element (e.g. an attribute name or value) fails, then the output of bytes stops before that text element. |
| -4 | An invalid character was encountered. The output of bytes stops just before that character. See the [xmlContainsValidCharactersOnly()](contains_valid_characters_only.md) function. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
