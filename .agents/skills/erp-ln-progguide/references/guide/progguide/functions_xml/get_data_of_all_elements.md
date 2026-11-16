# Get data of all Elements

## Syntax:
`function long xmlGetDataElement( long node, const string name, ref string data, [ const string data.separator, const string element.separator ] )`

## Description
For each child XML_ELEMENT node that has a name equal to *name*, get the data contained in XML_DATA child nodes. The data from all matching nodes is concatenated.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the parent node for which all matching XML_ELEMENT child nodes are searched.  |
| `const string` | `name` |  *name* contains the name of the XML_ELEMENT node to be found.  |
| `ref string` | `data` |  *data* contains the concatenated data for all found nodes on return. The function [xmlGetDataElementLength()](get_data_length_of_all_elements.md) may be used to determine the required size of *data*.  |
| `[ const string` | `data.separator ]` |  Optional argument (available as of [porting set TIV](../tiv/tiv_overview.md) [level 2500](../tiv/tiv_2500.md)) specifying the string used to separate the data of different XML_DATA nodes that are descendants of the same XML_ELEMENT node matching the specified *name*. If this argument is not supplied, the default data separator string is used, which contains exactly one space character.  |
| `[ const string` | `element.separator ]` |  Optional argument (available as of [porting set TIV](../tiv/tiv_overview.md) [level 2500](../tiv/tiv_2500.md)) specifying the string used to separate the data of XML_DATA nodes that are descendants of different XML_ELEMENT nodes matching the specified *name*. If this argument is not supplied, then the default element separator string is used, which is the empty string.  |

## Return values
| | |
|---|---|
| <> 0 | Success; Value of parameter node when successful. |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related
```

string	xmlDataElement$( long node, const string name, [ const string default.value, const string data.separator, const string element.separator ] )
long	xmlAllocDataElement( ref string basedString(), long node, const string name, [ const string default.value, const string data.separator, const string element.separator ] )
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
