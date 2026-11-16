# xmlSetNamespace()

## Syntax:
`function long xmlSetNamespace( long node, long namespace )`

## Description
Set the namespace of an XML node to the specified namespace. The specified node does not become the *carrier* of the namespace. In other words, the node does not declare the namespace, but it is put in the namespace. If the XML node is not of type XML_ELEMENT then the function fails.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node. If *node* is invalid or not of type XML_ELEMENT then the function fails.  |
| `long` | `namespace` |  *namespace* contains a reference to the namespace as created by the [xmlNewNamespace()](xmlNewNamespace.md) function or as returned by the [xmlGetPredefinedNamespace()](xmlGetPredefinedNamespace.md) function. If the *namespace* is invalid then the function fails.  |

## Return values
| | |
|---|---|
| <> 0 | Success; A reference to the node when successful. |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope, xml_body, xmlns_soap
xml_envelope = xmlNewNode("Envelope")
xmlns_soap = xmlNewNamespace( xml_envelope, "soap", "http://www.w3.org/2001/12/soap-envelope" )
xmlSetNamespace( xml_envelope, xmlns_soap )
```
The *xml_envelope* node would serialize to the following XML. Note that the *Envelope* node has the "soap" prefix, and is thus in the namespace with URI "http://www.w3.org/2001/12/soap-envelope".
```

<soap:Envelope xmlns:soap="http://www.w3.org/2001/12/soap-envelope"/>
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
