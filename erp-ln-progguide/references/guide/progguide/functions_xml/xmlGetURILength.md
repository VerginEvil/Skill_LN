# xmlGetURILength()

## Syntax:
`function long xmlGetURILength( long node )`

## Description
Get the length of the URI of the namespace of the specified node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node.  |

## Return values
| | |
|---|---|
| >= 0 | Success; The length of the URI. |
| -1 | The *node* is invalid or the node *node* is not in a namespace.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope
string error(100)
xml_envelope = xmlReadFromStringNs( "<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope""/>", error )

long length
length = xmlGetURILength( xml_envelope )
| length now contains 39
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [XML object synopsis (namespace support)](synopsis_namespace.md)
