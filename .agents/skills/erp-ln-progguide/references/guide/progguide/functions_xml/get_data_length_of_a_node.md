# Get data length of a Node

## Syntax:
`function long xmlGetDataLength( long node, [ long separator.length ] )`

## Description
Get the data length of a node. When *node* is of type XML_DATA or XML_PI, only the length of the data from this node is obtained. When node is of type XML_ELEMENT or XML_DTD, the length of the data from all child XML_DATA and XML_PI nodes is counted.
This function may be used to determine the required size of the *data* argument supplied to [xmlGetData()](get_data_of_a_node.md).

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the data length is obtained.  |
| `[ long` | `separator.length ]` |  Optional argument (available as of [porting set TIV](../tiv/tiv_overview.md) [level 2500](../tiv/tiv_2500.md)) specifying the length in bytes of the separator string used to separate the data of different XML_DATA nodes. If this argument is not supplied, default value 1 is used, corresponding to the default separator string, which contains exactly one space character.  |

## Return values
| | |
|---|---|
| >= 0 | Success; Length of the data in the *node*. |
| -1 | Error, the specified *node* is incorrect. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
