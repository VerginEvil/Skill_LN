# Get data length of all Elements

## Syntax:
`function long xmlGetDataElementLength( long node, const string name, [ long data.separator.length, long element.separator.length ] )`

## Description
Get the data length of a node. For each child XML_ELEMENT node that has a name equal to *name*, the length of the data contained in XML_DATA child nodes is counted.
This function may be used to determine the required size of the *data* argument supplied to [xmlGetDataElement()](get_data_of_all_elements.md).

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the parent node for which all matching XML_ELEMENT child nodes are searched.  |
| `const string` | `name` |  *name* contains the name of the XML_ELEMENT node to be found.  |
| `[ long` | `data.separator.length ]` |  Optional argument (available as of [porting set TIV](../tiv/tiv_overview.md) [level 2500](../tiv/tiv_2500.md)) specifying the length in bytes of the separator string used to separate the data of different XML_DATA nodes that are descendants of the same XML_ELEMENT node matching the specified *name*. If this argument is not supplied, default value 1 is used, corresponding to the default data separator string, which contains exactly one space character.  |
| `[ long` | `element.separator.length ]` |  Optional argument (available as of [porting set TIV](../tiv/tiv_overview.md) [level 2500](../tiv/tiv_2500.md)) specifying the length in bytes of the separator string used to separate the data of XML_DATA nodes that are descendants of different XML_ELEMENT nodes matching the specified *name*. If this argument is not supplied and the *data.separator.length* argument *is* supplied, then default value 0 is used, corresponding to the default element separator string, which is the empty string. If both this argument and the *data.separator.length* argument are not supplied, then this function has the original behavior (as before [porting set TIV](../tiv/tiv_overview.md) [level 2500](../tiv/tiv_2500.md)): for both arguments default value 1 is used, corresponding to the default data separator string, which contains exactly one space character, but *not* corresponding to the default element separator string, which is the empty string.  |

## Return values
| | |
|---|---|
| >= 0 | Success; Length of the concatenated data for all found nodes.  |
| -1 | Error, the specified *node* is incorrect.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
