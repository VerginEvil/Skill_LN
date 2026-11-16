# xmlGetAttributeURILength()

## Syntax:
`function long xmlGetAttributeURILength( long node, long attributeNr )`

## Description
Get the length of the URI of an attribute of the specified node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node.  |
| `long` | `attributeNr` |  *attributeNr* identifies the attribute of the *node*. The value 1 identifies the first attribute.  |

## Return values
| | |
|---|---|
| >= 0 | Success; The length of the URI. |
| -1 | The *node* is invalid or *attributeNr* is invalid or the attribute is not in a namespace. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope
string error(100)
xml_envelope = xmlReadFromStringNs(
	"<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope"" "
	& " soap:encodingStyle=""http://www.w3.org/2001/12/soap-encoding"" > , error)

long length
length = xmlGetAttributeURILength( xml_envelope, 1 )

| length now contains 39
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
