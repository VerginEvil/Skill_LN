# Get data of a Node

## Syntax:
`function long xmlGetData( long node, ref string data, [ const string separator ] )`

## Description
Get the data of a node. When *node* is of type XML_DATA or XML_PI, only the data from this node is obtained. When node is of type XML_ELEMENT or XML_DTD, the data from all child XML_DATA and XML_PI nodes is concatenated.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the data is obtained.  |
| `ref string` | `data` |  *data* is a string buffer which contains the data on return. The function [xmlGetDataLength()](get_data_length_of_a_node.md) may be used to determine the required size of *data*.  |
| `[ const string` | `separator ]` |  Optional argument (available as of [porting set TIV](../tiv/tiv_overview.md) [level 2500](../tiv/tiv_2500.md)) specifying the string used to separate the data of different XML_DATA nodes. If this argument is not supplied, the default separator string is used, which contains exactly one space character.  |

## Return values
| | |
|---|---|
| <> 0 | Success; Value of parameter *node* when successful.  |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related
```

string	xmlData$( long node, [ const string default.value, const string separator ] )
long	xmlAllocData( ref string basedString(), long node, [ const string default.value, const string separator ] )
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
