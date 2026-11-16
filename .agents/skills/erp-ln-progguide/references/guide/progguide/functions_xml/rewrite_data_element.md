# Rewrite Data Element

## Syntax:
`function long xmlRewriteDataElement( long node, string name, string data )`

## Description
Find first child XML_ELEMENT node that has a name equal to name. If a matching node is found and this node does not have any child node, a new XML_DATA node with value data is added as a child node.
If a matching node is found and this node already has one or more child nodes, these child nodes are all replaced by a single new XML_DATA child node with value data.
When no matching node is found, a new child XML_ELEMENT node is appended to the list of child nodes. To this new child node a new XML_DATA node with value data is added.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the parent node for which a matching XML_ELEMENT child node is searched.  |
| `string` | `name` |  *name* contains the name of the XML_ELEMENT node to be found.  |
| `string` | `data` |  *data* contains the data for the new XML_DATA node.  |

## Return values
| | |
|---|---|
| <> 0 | Success; Value of parameter *node* when successful. |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
