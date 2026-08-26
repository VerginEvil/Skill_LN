# Find Nodes using a Match Pattern

## Syntax:
`function long xmlFindMatch( string pattern, long fromNode, [ long toNode ] )`

## Description
Search in a tree or a list of trees and create a new tree containing references to all occurrences of XML_ELEMENT or XML_DTD nodes, which match with the *pattern*. The *pattern* contains a search path relative to the starting node. The starting node is the list of nodes indicated by *fromNode* to *toNode*.

## Arguments
| | | |
|---|---|---|
| `string` | `pattern` |  See [Find first Node using a Match Pattern](find_first_node_using_a_match_pattern.md)  |
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See fromNode and toNode.  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See fromNode and toNode.  |

## Return values
The return value refers to a new tree, which contains the NodeId's of the nodes which match the *pattern*. This new tree corresponds to an XML document as shown below:
```

<Enumeration TYPE="InMemory XmlNodes">
        <e0>id0</e0>
        <e1>id1</e1>
        ...
        <en>idn</en>
</Enumeration>
```
In this example *idn* is the decimal string representation of a nodeId of a node, which matches the *pattern*.
Like any other tree of Nodes, the returned tree must be freed from memory by using xmlDelete().
| | |
|---|---|
| <> 0 | Success; The new tree containing references to the found nodes. In case no match is found the tree consists of a single node.  |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
