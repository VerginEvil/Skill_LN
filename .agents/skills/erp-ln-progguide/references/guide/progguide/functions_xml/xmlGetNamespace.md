# xmlGetNamespace()

## Syntax:
`function long xmlGetNamespace( long node )`

## Description
Get the namespace of an XML node. This function returns a reference to the namespace as created by the [xmlNewNamespace()](xmlNewNamespace.md) function or as returned by the [xmlGetPredefinedNamespace()](xmlGetPredefinedNamespace.md) function. The reference can be used in for example the [xmlNewNodeNs()](xmlNewNodeNs.md) function.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node.  |

## Return values
| | |
|---|---|
| <> 0 | Success; A reference to the namespace when successful. |
| 0 | Error. The *node* may be invalid or it may not be in a namespace. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope
string error(100)
xml_envelope = xmlReadFromStringNs( "<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope""/>", error )
long xmlns_soap
xmlns_soap = xmlGetNamespace( xml_envelope )

| xmlNamespacePrefix$( xmlns_soap ) would return "soap"
| xmlNamespaceURI$( xmlns_soap ) would return "http://www.w3.org/2001/12/soap-envelope"
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
