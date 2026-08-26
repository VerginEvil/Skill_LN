# xmlNewDataElementNs()

## Syntax:
`function long xmlNewDataElementNs( long namespace, const string name, void data, [ long parentNode ] )`

## Description
Create a new XML node of type XML_ELEMENT with *local name* as specified by *name* and in the namespace as specified by *namespace*. A new XML node of type XML_DATA is created as the first child of the newly created XML_ELEMENT node, with data as specified by *data*. The function fails if *namespace* is invalid or *parentNode* is invalid.

## Arguments
| | | |
|---|---|---|
| `long` | `namespace` |  *namespace* contains a reference to the namespace as created by the [xmlNewNamespace()](xmlNewNamespace.md) function or as returned by the [xmlGetPredefinedNamespace()](xmlGetPredefinedNamespace.md) function. If the *namespace* is invalid then the function fails.  |
| `const string` | `name` |  *name* is the *local name* of the new node of type XML_ELEMENT.  |
| `void` | `data` |  *data* is the data of the new node of type XML_DATA.  |
| `[ long` | `parentNode ]` |  *parentNode* when specified this refers to the parent node. The new node is appended to the list of child nodes. When omitted, the new node is not added to any parent node.  |

## Return values
| | |
|---|---|
| <> 0 | Success; A reference to the newly created XML_ELEMENT node when successful.  |
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
```
The *xml_envelope* node would serialize to the following XML. Note that the call to xmlNewDataElementNs() has created the element *StockName* in the proper namespace and with the data.
```

<soap:Envelope
	xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
	soap:EncodingStyle="http://www.w3.org/2001/12/soap-encoding">
	<soap:Body
		xmlns:m="http://www.example.org/stock">
		<m:GetStockPrice>
			<m:StockName>IBM</m:StockName>
		</m:GetStockPrice>
	</soap:Body>
</soap:Envelope>
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [XML object synopsis (namespace support)](synopsis_namespace.md)
