# Duplicate and Append Nodes to Children

## Syntax:
`function long xmlDuplicateAndAppendToChilds( long parentNode, long fromNode, [ long toNode ] )`

## Description
Duplicate a tree or a list of trees and append this list as the last child of the node referred to by *parentNode*.

## Arguments
| | | |
|---|---|---|
| `long` | `parentNode` |    |
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See [fromNode and toNode](api.md#fromnode_tonode).  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See [fromNode and toNode](api.md#fromnode_tonode).  |

## Return values
| | |
|---|---|
| <> 0 | Success; Reference to first node in tree or list of trees, which has been created. |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
