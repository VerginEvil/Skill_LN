# xmlAllocAttributeNs()

## Syntax:
`function long xmlAllocAttributeNs( ref string basedString, long node, void namespaceOrURI, const string attributeName, [ const string default.value ] )`

## Description
Get the value of an attribute of the specified node. If an attribute with the specified *attributeName* and with a namespace whose URI matches the URI specified by *namespaceOrURI* exists, then its value is returned. The function fails if the *node* is invalid or the *namespaceOrURI* is invalid.

## Arguments
| | | |
|---|---|---|
| `ref string` | `basedString` |  *basedString* is the return argument to receive the value. It must be declared *based*.  |
| `long` | `node` |  *node* is a reference to an XML node.  |
| `void` | `namespaceOrURI` |  *namespaceOrURI* is either a reference to an XML namespace, or it is a URI. If the *namespaceOrURI* parameter is of type *long* then it is a reference to an XML namespace; if it is of type *string* then it is a URI; otherwise the function fails.  |
| `const string` | `attributeName` |  *attributeName* is the *local name* of the attribute of the *node*.  |
| `[ const string` | `default.value ]` |  *default.value* is a string that is used as return value when the function fails.  |

## Return values
| | |
|---|---|
| 0 | Success; The *basedString* contains the value if the *node* is valid, and the node has an attribute with the specified *attributeName* and with a namespace whose URI matches the URI specified by *namespaceOrURI*. It contains the *default.value*, or when this is omitted, the empty string otherwise.  |
| -1 | The *basedString* is not declared *based*.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope
string error(100)
xml_envelope = xmlReadFromStringNs(
	"<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope"" "
	& " soap:encodingStyle=""http://www.w3.org/2001/12/soap-encoding"" > , error)

string value based
long ret
ret = xmlAllocAttributeNs( value, xml_envelope, "http://www.w3.org/2001/12/soap-envelope", "encodingStyle" )

| ret now contains 0
| value now contains "http://www.w3.org/2001/12/soap-encoding"
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [XML object synopsis (namespace support)](synopsis_namespace.md)
