# Create a new Node

## Syntax:
`function long xmlNewNode( string name, [ long type, long parentNode ] )`

## Description
Create a new XML node.

## Arguments
| | | |
|---|---|---|
| `string` | `name` |  *name* contains the name of this node (in case type is XML_ELEMENT or XML_DTD) or the data for this node (in case type is XML_DATA or XML_PI).  |
| `[ long` | `type ]` |  *type* must be one of: XML_ELEMENT, XML_DTD, XML_DATA or XML_PI. The default value is XML_ELEMENT.  |
| `[ long` | `parentNode ]` |  *parentNode* when specified this refers to the parent node. The new node is appended to the list of child nodes. When omitted, the new node is not added to any parent node.  |

## Return values
| | |
|---|---|
| <> 0 | Success; A reference to the new node when successful.  |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
