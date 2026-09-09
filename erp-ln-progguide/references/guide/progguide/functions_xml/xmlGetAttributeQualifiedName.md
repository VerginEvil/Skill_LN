# xmlGetAttributeQualifiedName()

## Syntax:
`function long xmlGetAttributeQualifiedName( long node, long attributeNr, ref string name )`

## Description
Get the qualified name of an attribute of the specified node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node.  |
| `long` | `attributeNr` |  *attributeNr* identifies the attribute of the *node*. The value 1 identifies the first attribute.  |
| `ref string` | `name` |  *name* is the return argument to receive the qualified name.  |

## Return values
| | |
|---|---|
| <> 0 | Success; The value of *node*. The *name* contains the qualified name if the *node* is valid, the *attributeNr* is valid and the attribute is in a namespace. It contains the empty string otherwise. |
| 0 | The *node* is invalid, the *attributeNr* is invalid or the namespace of the namespace is invalid or the *default* namespace. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope
string error(100)
xml_envelope = xmlReadFromStringNs(
	"<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope"" "
	& " soap:encodingStyle=""http://www.w3.org/2001/12/soap-encoding"" > , error)

string qname(30)
long ret
ret = xmlGetAttributeQualifiedName( xml_envelope, 1, qname )

| ret now contains 0
| qname now contains "soap:encodingStyle"
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
