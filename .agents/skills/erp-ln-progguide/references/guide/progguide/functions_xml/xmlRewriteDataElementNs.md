# xmlRewriteDataElementNs()

## Syntax:
`function long xmlRewriteDataElementNs( long node, void namespaceOrURI, const string name, void data )`

## Description
If *node* has no child node of type XML_ELEMENT whose *local name* equals *name* and whose URI equals the URI specified by *namespaceOrURI*, then a new XML node of type XML_ELEMENT is created, with an XML node of type XML_DATA with the specified *data*.
Otherwise, for each child node of type XML_ELEMENT whose *local name* equals *name* and whose URI equals the URI specified by *namespaceOrURI* do the following: if the child node has no child node of type XML_DATA, then create such a node with the specified *data*; otherwise, all child nodes of type XML_DATA are replaced by a single child node of type XML_DATA with the specified *data*.
The function fails if *node* is invalid or *namespaceOrURI* is invalid.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node.  |
| `void` | `namespaceOrURI` |  *namespaceOrURI* is either a reference to an XML namespace, or it is a URI. If the *namespaceOrURI* parameter is of type *long* then it is a reference to an XML namespace; if it is of type *string* then it is a URI; otherwise the function fails.  |
| `const string` | `name` |  *name* is the *local name* of the child node(s) of type XML_ELEMENT.  |
| `void` | `data` |  *data* is the new data of the node(s) of type XML_DATA.  |

## Return values
| | |
|---|---|
| <> 0 | Success; The value of *node*. |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope, xml_body, xml_stockprice, xmlns_soap, xmlns_m
xml_envelope = xmlNewNode("Envelope")
xmlns_soap = xmlNewNamespace( xml_envelope, "soap", "http://www.w3.org/2001/12/soap-envelope" )
xmlSetNamespace( xml_envelope, xmlns_soap )
xmlSetAttributeNs( xml_envelope, xmlns_soap, "EncodingStyle", "http://www.w3.org/2001/12/soap-encoding" )
xml_body = xmlNewNodeNs( xmlns_soap, "Body", XML_ELEMENT, xml_envelope )
xmlns_m = xmlNewNamespace( xml_body, "m", "http://www.example.org/stock" )
xml_stockprice = xmlNewNodeNs( xmlns_m, "GetStockPrice", XML_ELEMENT, xml_body )

long ret
ret = xmlNewDataElementNs( xmlns_m, "StockName", "IBM", xml_stockprice )
ret = xmlRewriteDataElementNs( xml_stockprice, xmlns_m, "StockName", "SUN" )
| ret now contains the value of xml_stockprice
```
The *xml_envelope* node would serialize to the following XML. Note that the call to xmlRewriteDataElementNs() has updated the data of the element *StockName* with the supplied data.
```

<soap:Envelope
	xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
	soap:EncodingStyle="http://www.w3.org/2001/12/soap-encoding">
	<soap:Body
		xmlns:m="http://www.example.org/stock">
		<m:GetStockPrice>
			<m:StockName>SUN</m:StockName>
		</m:GetStockPrice>
	</soap:Body>
</soap:Envelope>
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
