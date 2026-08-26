# Duplicate Nodes

## Syntax:
`function long xmlDuplicate( long fromNode, [ long toNode ] )`

## Description
Duplicate a tree or a list of trees.

## Arguments
| | | |
|---|---|---|
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See fromNode and toNode.  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See fromNode and toNode.  |

## Return values
| | |
|---|---|
| <> 0 | Success; Reference to first node in tree or list of trees, which has been created.  |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
