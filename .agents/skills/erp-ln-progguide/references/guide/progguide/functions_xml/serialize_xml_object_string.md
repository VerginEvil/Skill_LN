# Serialize XML Object to String

## Syntax:
`function long xmlWriteToString( ref string buffer$, long fromNode, [ long toNode ] )`

## Description
Serialize an XML object and write the resulting unformatted XML document to an in-memory string. Any TSS encoded string information in the XML object is encoded in UTF-8 in the XML document.
Use [xmlWritePrettyToString](serialize_xml_object_string_pretty.md) instead to serialize the XML object to a formatted XML document.

## Arguments
| | | |
|---|---|---|
| `ref string` | `buffer$` |  Ref string argument that receives the UTF-8 encoded unformatted XML document. As its contents will not be encoded in TSS, it is desirable that this argument is of type string, rather than type multibyte string. The function [xmlGetStringLength()](get_serialize_length.md) may be used to determine the required size of the buffer.  |
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See [fromNode and toNode](api.md#fromnode_tonode).  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See [fromNode and toNode](api.md#fromnode_tonode).  |

## Return values
| | |
|---|---|
| -1 | Incorrect argument. For example, *fromNode* or *toNode* is not a valid xml node. |
| -3 | The ref string *buffer$* argument is too small, or a TSS conversion error occurred. If TSS conversion of a certain text element (e.g. an attribute name or value) fails, then the output of bytes stops before that text element. |
| -4 | An invalid character was encountered. The output of bytes stops just before that character. See the [xmlContainsValidCharactersOnly()](contains_valid_characters_only.md) function. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
