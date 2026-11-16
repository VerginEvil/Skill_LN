# xmlGetAttributePrefix()

## Syntax:
`function long xmlGetAttributePrefix( long node, long attributeNr, ref string prefix )`

## Description
Get the prefix of an attribute of the specified node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node.  |
| `long` | `attributeNr` |  *attributeNr* identifies the attribute of the *node*. The value 1 identifies the first attribute.  |
| `ref string` | `prefix` |  *prefix* is the return argument to receive the prefix.  |

## Return values
| | |
|---|---|
| <> 0 | Success; The value of *node*. The *prefix* contains the prefix if the *node* is valid, the *attributeNr* is valid and the attribute is in a namespace. It contains the empty string otherwise. |
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

string prefix(10)
long ret
ret = xmlGetAttributePrefix( xml_envelope, 1, prefix )

| ret now contains 0
| prefix now contains "soap"
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
