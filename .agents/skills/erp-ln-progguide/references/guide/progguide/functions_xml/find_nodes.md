# Find Nodes

## Syntax:
`function long xmlFindNodes( long node, string criteria, long maxFound, [ ref long numFound ] )`

## Description
Search in a tree starting at *node* and create a new tree containing references to all occurrences of XML_ELEMENT or XML_DTD nodes, which name matches with the string *criteria*. Searching stops when *maxFound* number of Nodes is found. When *maxFound* has value 0, searching stops when the complete tree has been traversed. The tree is traversed in the order as shown in [Figure 2 - Depth first Tree traversal order](api.md#tree_traversal_order).
On return, the optional argument *numFound* contains the number of matching nodes which have been found.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  The tree starting at *node* that will be searched.  |
| `string` | `criteria` |  The string that must match the nodes in the specified tree.  |
| `long` | `maxFound` |  The maximum number of occurrences to be included in the resulting tree. If this value is 0, all occurrences are included.  |
| `[ ref long` | `numFound ]` |  The number of occurrences that has been found.  |

## Return values
The return value refers to a new tree, which contains the NodeId's of the nodes which match the name *criteria*. This new tree corresponds to an XML document as shown below:
```

<Enumeration TYPE="InMemory XmlNodes">
        <e0>id0</e0>
        <e1>id1</e1>
        ...
        <en>idn</en>
</Enumeration>
```
In this example *idn* is the decimal string representation of a nodeId of a node, which matches *criteria*.
Like any other tree of Nodes, the returned tree must be freed from memory by using xmlDelete().
| | |
|---|---|
| <> 0 | Success; The new tree containing references to the found nodes. In case no match is found the tree consists of a single node. |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
