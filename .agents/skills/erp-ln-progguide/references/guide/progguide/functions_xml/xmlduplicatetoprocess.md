# Duplicate Nodes to Process

## Syntax:
`function long xmlDuplicateToProcess( long processId, long fromNode, [ long toNode ] )`

## Description
Duplicate a tree or a list of trees into another 3GL-process space.

## Arguments
| | | |
|---|---|---|
| `long` | `processId` |  *processId* must be a valid 3GL process identifier. This process becomes the owner of the newly created tree or list of trees.  |
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

- [XML object synopsis (namespace support)](synopsis_namespace.md)
