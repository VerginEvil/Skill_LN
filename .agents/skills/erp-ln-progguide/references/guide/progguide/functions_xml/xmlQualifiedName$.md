# xmlQualifiedName$()

## Syntax:
`function string xmlQualifiedName$( long node, [ const string default.value ] )`

## Description
Get the qualified name of the specified node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node.  |
| `[ const string` | `default.value ]` |  *default.value* is a string that is used as return value when the function fails.  |

## Return values
| | |
|---|---|
| string | If the *node* is valid, then a temporary string containing the qualified name of the *node* is returned. Otherwise, the *default.value*, or when this is omitted, the empty string is returned. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope
string error(100)
xml_envelope = xmlReadFromStringNs( "<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope""/>", error )

string qname(20)
qname = xmlQualifiedName$( xml_envelope )
| qname now contains "soap:Envelope"
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
