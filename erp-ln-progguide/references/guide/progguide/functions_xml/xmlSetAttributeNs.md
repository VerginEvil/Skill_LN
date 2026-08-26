# xmlSetAttributeNs()

## Syntax:
`function long xmlSetAttributeNs( long node, long namespace, const string name, void value )`

## Description
Set the value of an attribute with a namespace. If no attribute with the specified *name* and with a namespace whose URI matches the URI of the specified *namespace* exists, then a new attribute with the specified *name*, *namespace* and *value* is created. If the XML node is not of type XML_ELEMENT then the function fails.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node. If *node* is invalid or not of type XML_ELEMENT then the function fails.  |
| `long` | `namespace` |  *namespace* contains a reference to the namespace as created by the [xmlNewNamespace()](xmlNewNamespace.md) function or as returned by the [xmlGetPredefinedNamespace()](xmlGetPredefinedNamespace.md) function. If the *namespace* is invalid then the function fails.  |
| `const string` | `name` |  *name* is the *local name* of the attribute.  |
| `void` | `value` |  *value* is the (new) value of the attribute.  |

## Return values
| | |
|---|---|
| <> 0 | Success; A reference to the node when successful.  |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope, xml_body, xmlns_soap
xml_envelope = xmlNewNode("Envelope")
xmlns_soap = xmlNewNamespace( xml_envelope, "soap", "http://www.w3.org/2001/12/soap-envelope" )
long ret
ret = xmlSetAttributeNs( xml_envelope, xmlns_soap, "EncodingStyle", "http://www.w3.org/2001/12/soap-encoding" )
| ret now contains the value of xml_envelope
```
The *xml_envelope* node would serialize to the following XML. Note that the *EncodingStyle* attribute has the "soap" prefix, and is thus in the namespace with URI "http://www.w3.org/2001/12/soap-envelope".
```

<Envelope xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
		soap:EncodingStyle="http://www.w3.org/2001/12/soap-encoding"/>
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [XML object synopsis (namespace support)](synopsis_namespace.md)
