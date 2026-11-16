# xmlAllocAttributeQualifiedName()

## Syntax:
`function long xmlAllocAttributeQualifiedName( ref string basedString, long node, long attributeNr, [ const string default.value ] )`

## Description
Get the qualified name of an attribute of the specified node.

## Arguments
| | | |
|---|---|---|
| `ref string` | `basedString` |  *basedString* is the return argument to receive the qualified name. It must be declared *based*.  |
| `long` | `node` |  *node* is a reference to an XML node.  |
| `long` | `attributeNr` |  *attributeNr* identifies the attribute of the *node*. The value 1 identifies the first attribute.  |
| `[ const string` | `default.value ]` |  *default.value* is a string that is used as return value when the function fails.  |

## Return values
| | |
|---|---|
| 0 | Success; The *basedString* contains the qualified name if the *node* is valid, the *attributeNr* is valid and the attribute is in a namespace. It contains the *default.value*, or when this is omitted, the empty string otherwise. |
| -1 | The *basedString* is not declared *based*. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope
string error(100)
xml_envelope = xmlReadFromStringNs(
	"<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope"" "
	& " soap:encodingStyle=""http://www.w3.org/2001/12/soap-encoding"" > , error)

string qname based
long ret
ret = xmlAllocAttributeQualifiedName( qname, xml_envelope, 1 )

| ret now contains 0
| qname now contains "soap:encodingStyle"
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
