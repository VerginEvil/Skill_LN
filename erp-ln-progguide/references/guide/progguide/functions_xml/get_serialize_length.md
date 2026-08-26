# Get length of a serialized XML Object

## Syntax:
`function long xmlGetStringLength( long fromNode, [ long toNode ] )`

## Description
Get the length of the serialized form of an XML Object.
This function may be used to determine the required size of the argument supplied to [Serialize XML Object (xmlWrite)](serialize_xml_object.md).

## Arguments
| | | |
|---|---|---|
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See fromNode and toNode.  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See fromNode and toNode.  |

## Return values
| | |
|---|---|
| >= 0 | Success; Length of the generated XML document. |
| < 0 |  Error. Some specific values:  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
