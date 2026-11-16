# Find set of Sibling Nodes

## Syntax:
`function long xmlFindSetOfSiblingNodes( long node, string criteria, long maxFound, [ ref long numFound ] )`

## Description
Traverse the tree starting at *node* and return all occurrences of XML_ELEMENT or XML_DTD nodes of which the name matches the *criteria* argument. Searching will stop when *maxFound* number of Nodes have been found. When *maxFound* has value 0, searching will stop when the complete tree has been traversed. The tree is traversed in the breadth first order as shown in [Figure 3 - Breadth first Tree traversal order](api.md#breadth_first).
On return, the optional argument *numFound* contains the number of matching nodes that were found.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  Reference to the top node of the XML tree that is traversed.  |
| `string` | `criteria` |  String that the name of the returned nodes must match.  |
| `long` | `maxFound` |  Maximum number of nodes to return in the result. If this argument has value 0, then all matching nodes are returned.  |
| `[ ref long` | `numFound ]` |  Optional reference argument that receives the number of nodes in the returned result.  |

## Return values
The return value refers to a new tree, which contains the Node Ids of the nodes of which the name matches the *criteria* argument. This new tree corresponds to an XML document as shown below:
```

<Enumeration TYPE="Enumeration" >
        <e0>
                <Enumeration TYPE="InMemory XmlNodeId">
                        <e0>id0</e0>
                        <e1>id1</e1>
                        ...
                        <en>idn</en>
                </Enumeration>
        </e0>
        <e1>
                <Enumeration TYPE="InMemory XmlNodeId">
                        <e0>id0</e0>
                        <e1>id1</e1>
                        ...
                        <em>idm</em>
                </Enumeration>
        </e1>
        ...
        <ek>
               ...
        </ek>
</Enumeration>
```
In this example *idn* is the decimal string representation of the Node Id of a node of which the name matches the *criteria* argument. All matching nodes found on the same level (sibling nodes) will be grouped together in one <Enumeration TYPE="InMemory XmlNodeId"> element.
Like any other tree of Nodes, the returned tree must be freed from memory by using xmlDelete().
| | |
|---|---|
| <> 0 | Success; The new tree containing references to the found nodes. In case no match is found, the tree consists of a single node. |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
