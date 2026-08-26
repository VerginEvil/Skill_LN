# xmlNewNamespace()

## Syntax:
`function long xmlNewNamespace( long node, const string prefix, const string URI )`

## Description
Create a new namespace with the specified prefix and URI. The specified node becomes the *carrier* of the namespace, but the node itself is not yet *in* the namespace.
Various restrictions apply to the specified prefix and the URI. For example, when the prefix equals "xml", then the URI *must* equal "http://www.w3.org/XML/1998/namespace". For this and other restrictions, see Namespaces in XML 1.0 (Third Edition), chapter 3 Declaring Namespaces.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  The XML node identified by *node* becomes the *carrier* of the newly created namespace. If the XML node is not of type XML_ELEMENT then the function fails.  |
| `const string` | `prefix` |  *prefix* contains the prefix, for example "soap".  |
| `const string` | `URI` |  *URI* contains the URI, for example "http://www.w3.org/2001/12/soap-envelope".  |

## Return values
| | |
|---|---|
| <> 0 | Success; A reference to the new namespace when successful. This value can be used in many functions with a *namespace* argument, such as [xmlNewNodeNs()](xmlNewNodeNs.md).  |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope, xml_body, xmlns_soap
xml_envelope = xmlNewNode("Envelope")
xmlns_soap = xmlNewNamespace( xml_envelope, "soap", "http://www.w3.org/2001/12/soap-envelope" )
xml_body = xmlNewNodeNs(xmlns_soap, "Body", XML_ELEMENT, xml_envelope)
```
The *xml_envelope* node would serialize to the following XML. Note that the *Envelope* node has no prefix, and is not in any namespace.
```

<Envelope xmlns:soap="http://www.w3.org/2001/12/soap-envelope"><soap:Body/></Envelope>
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [XML object synopsis (namespace support)](synopsis_namespace.md)
