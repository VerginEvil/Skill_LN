# xmlNamespacePrefix$()

## Syntax:
`function string xmlNamespacePrefix$( long namespace )`

## Description
Get the prefix of the specified namespace.

## Arguments
| | | |
|---|---|---|
| `long` | `namespace` |  *namespace* is a reference to an XML namespace.  |

## Return values
| | |
|---|---|
| string | Success; A temporary string containing the prefix of the namespace. |
| "" | The *namespace* is invalid or the *namespace* is the *default* namespace. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope
string error(100)
xml_envelope = xmlReadFromStringNs( "<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope""/>", error )
long xmlns_soap
xmlns_soap = xmlFindNamespace( xml_envelope, "http://www.w3.org/2001/12/soap-envelope" )

string prefix(10)
prefix = xmlNamespacePrefix$( xmlns_soap )
| prefix now contains "soap"
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
