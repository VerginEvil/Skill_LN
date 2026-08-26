# xmlDeleteAttributeNs()

## Syntax:
`function long xmlDeleteAttributeNs( long node, void namespaceOrURI, const string name )`

## Description
Delete an attribute with a namespace. If an attribute with the specified *name* and with a namespace whose URI matches the URI specified by *namespaceOrURI* exists, then this attribute is deleted. The function fails if the *node* is invalid or the *namespaceOrURI* is invalid.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node. If *node* is invalid then the function fails.  |
| `void` | `namespaceOrURI` |  *namespaceOrURI* is either a reference to an XML namespace, or it is a URI. If the *namespaceOrURI* parameter is of type *long* then it is a reference to an XML namespace; if it is of type *string* then it is a URI; otherwise the function fails.  |
| `const string` | `name` |  *name* is the *local name* of the attribute.  |

## Return values
| | |
|---|---|
| <> 0 | Success; A reference to the node when successful.  |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope
string error(100)
xml_envelope = xmlReadFromStringNs(
   "<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope"" "
   & " soap:encodingStyle=""http://www.w3.org/2001/12/soap-encoding"" />" , error)
long ret
ret = xmlDeleteAttributeNs( xml_envelope, "http://www.w3.org/2001/12/soap-envelope", "encodingStyle" )
| ret now contains the value of xml_envelope
```
The *xml_envelope* node would serialize to the following XML. Note that the *EncodingStyle* attribute no longer exists.
```
<Envelope xmlns:soap="http://www.w3.org/2001/12/soap-envelope"/>
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [XML object synopsis (namespace support)](synopsis_namespace.md)
