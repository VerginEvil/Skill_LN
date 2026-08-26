# Create an Element Node with Data Node

## Syntax:
`function long xmlNewDataElement( string name, string data, [ long parentNode ] )`

## Description
Create a new XML_ELEMENT node and new XML_DATA node. The XML_DATA node is the first child of the XML_ELEMENT node.

## Arguments
| | | |
|---|---|---|
| `string` | `name` |  *name* contains the name of the XML_ELEMENT node.  |
| `string` | `data` |  *data* contains the data for the XML_DATA node.  |
| `[ long` | `parentNode ]` |  *parentNode* when specified this refers to the parent node of the new XML_ELEMENT node. This node is appended to the list of child nodes. When omitted, the new XML_ELEMENT node is not added to any parent node.  |

## Return values
| | |
|---|---|
| <> 0 | Success; A reference to the new XML_ELEMENT node when successful.  |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
