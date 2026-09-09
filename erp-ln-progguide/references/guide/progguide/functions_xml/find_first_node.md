# Find first Node

## Syntax:
`function long xmlFindFirst( string tagName, long fromNode, [ long toNode ] )`

## Description
Search in a tree or a list of trees and return the first XML_ELEMENT or XML_DTD, which name is equal to the string *tagName*.

## Arguments
| | | |
|---|---|---|
| `string` | `tagName` |    |
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See [fromNode and toNode](api.md#fromnode_tonode).  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See [fromNode and toNode](api.md#fromnode_tonode).  |

## Return values
| | |
|---|---|
| <> 0 | Success; Reference to first matching Node. |
| 0 | Error or no match found. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
