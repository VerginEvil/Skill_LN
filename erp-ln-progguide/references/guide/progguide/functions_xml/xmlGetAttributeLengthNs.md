# xmlGetAttributeLengthNs()

## Syntax:
`function long xmlGetAttributeLengthNs( long node, void namespaceOrURI, const string attributeName )`

## Description
Get the length of the value of an attribute of the specified node. If an attribute with the specified *attributeName* and with a namespace whose URI matches the URI specified by *namespaceOrURI* exists, then the length of its value is returned. The function fails if the *node* is invalid or the *namespaceOrURI* is invalid.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node.  |
| `void` | `namespaceOrURI` |  *namespaceOrURI* is either a reference to an XML namespace, or it is a URI. If the *namespaceOrURI* parameter is of type *long* then it is a reference to an XML namespace; if it is of type *string* then it is a URI; otherwise the function fails.  |
| `const string` | `attributeName` |  *attributeName* is the *local name* of the attribute of the *node*.  |

## Return values
| | |
|---|---|
| >= 0 | Success; The length of the value. |
| -1 | The *node* is invalid, or the node has no attribute with the specified *attributeName* or with a namespace whose URI does not match the URI specified by *namespaceOrURI*.  |

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
length = xmlGetAttributeLengthNs( xml_envelope, "http://www.w3.org/2001/12/soap-envelope", "encodingStyle" )

| length now contains 39, the length of the string "http://www.w3.org/2001/12/soap-encoding"
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [XML object synopsis (namespace support)](synopsis_namespace.md)
