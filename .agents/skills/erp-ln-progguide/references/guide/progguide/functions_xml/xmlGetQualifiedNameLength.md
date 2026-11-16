# xmlGetQualifiedNameLength()

## Syntax:
`function long xmlGetQualifiedNameLength( long node )`

## Description
Get the length of the qualified name of the specified node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node.  |

## Return values
| | |
|---|---|
| >= 0 | Success; The length of the qualified name. |
| -1 | The *node* is invalid. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope
string error(100)
xml_envelope = xmlReadFromStringNs( "<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope""/>", error )

long length
length = xmlGetQualifiedNameLength( xml_envelope )
| length now contains 13, which is the length of the string "soap:Envelope"
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
