# xmlNewNodeNs()

## Syntax:
`function long xmlNewNodeNs( long namespace, const string name, [ long type, long parentNode ] )`

## Description
Create a new XML node in the specified namespace.

## Arguments
| | | |
|---|---|---|
| `long` | `namespace` |  *namespace* contains a handle to the namespace as created by the [xmlNewNamespace()](xmlNewNamespace.md) function or as returned by the [xmlGetPredefinedNamespace()](xmlGetPredefinedNamespace.md) function. It is ignored if *type* does not equal XML_ELEMENT.  |
| `const string` | `name` |  *name* contains the name of this node (in case type is XML_ELEMENT or XML_DTD) or the data for this node (in case type is XML_DATA or XML_PI).  |
| `[ long` | `type ]` |  *type* must be one of: XML_ELEMENT, XML_DTD, XML_DATA or XML_PI. The default value is XML_ELEMENT.  |
| `[ long` | `parentNode ]` |  *parentNode* when specified this refers to the parent node. The new node is appended to the list of child nodes. When omitted, the new node is not added to any parent node.  |

## Return values
| | |
|---|---|
| <> 0 | Success; A reference to the new node when successful. |
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
The *xml_body* node would serialize to the following XML. Note that the *Body* node has the "soap" prefix, and is in the namespace with URI "http://www.w3.org/2001/12/soap-envelope".
```

<soap:Body xmlns:soap="http://www.w3.org/2001/12/soap-envelope"><soap:Body/></Envelope>
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
