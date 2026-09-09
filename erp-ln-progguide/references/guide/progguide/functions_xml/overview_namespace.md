# XML object overview (namespace support)

## Purpose
The purpose of the XML object api with namespace support is to offer namespace support in XML to 3GL/4GL applications. The first target application is support for SOAP, but there is no restriction on the use of this interface.
For a good description of namespace support in XML see [Namespaces in XML 1.0](https://www.w3.org/TR/REC-xml-names/).

## Example
What follows is an example of the use of the XML object api with namespace support.
```

#define ASSERTSEQ(x,y)
^ if (x) <> (y)
^ then message("oops, " & str$(x) & " does not equal " & str$(y))
^ else
^ endif

function main()
{
	long ret

	|
	| Build the following example SOAP request:
	|
	|  <soap:Envelope
	|       xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
	|       soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">
	|       <soap:Body
	|               xmlns:m="http://www.example.org/stock">
	|               <m:GetStockPrice>
	|                       <m:StockName>IBM</m:StockName>
	|               </m:GetStockPrice>
	|       </soap:Body>
	|  </soap:Envelope>
	|

	| Create the "Envelope" node. After the xmlNewNode() functions this node does
	| not carry any namespace (no namespace declaration) and it is not in a
	| namespace.
	long xml_envelope
	xml_envelope = xmlNewNode("Envelope")

	| The "soap" namespace is defined on the "Envelope" node, which becomes the
	| carrier (or owner) of this namespace. The node is still not in a
	| namespace.
	long xmlns_soap
	xmlns_soap = xmlNewNamespace( xml_envelope,
		"soap", "http://www.w3.org/2001/12/soap-envelope")

	| Put the xml_envelope in the "soap" namespace.
	ret = xmlSetNamespace( xml_envelope, xmlns_soap )

	| Create the encodingStyle attribute in the "soap" namespace, with its value.
	ret = xmlSetAttributeNs( xml_envelope, xmlns_soap,
		"encodingStyle", "http://www.w3.org/2001/12/soap-encoding" )

	| Create the "Body" node, in the "soap" namespace.
	long xml_body
	xml_body = xmlNewNodeNs(xmlns_soap, "Body", XML_ELEMENT, xml_envelope)

	| Create the "m" namespace; the "Body" node becomes the carrier of this
	| namespace. The "Body" node now declares the "m" namespace, but is still in
	| in the "soap" namespace.
	long xmlns_m
	xmlns_m = xmlNewNamespace( xml_body, "m", "http://www.example.org/stock" )

	| Create the "GetStockPrice" node in the "m" namespace.
	long xml_GetStockPrice
	xml_GetStockPrice = xmlNewNodeNs(xmlns_m, "GetStockPrice", XML_ELEMENT,
		xml_body)

	| Create the "StockName" node in the "m" namespace, with an XML_DATA child
	| node containing the data "IBM".
	long xml_StockName
	xml_StockName = xmlNewDataElementNs(xmlns_m, "StockName", "IBM",
		xml_GetStockPrice)

	| Verify the serialization of the xml_envelope.
	string xml(1000)
	xml = xmlString$(xml_envelope)
	ASSERTSEQ( xml,
		  "<?xml version=""1.0""?>"
		& "<soap:Envelope "
		&    "xmlns:soap=""http://www.w3.org/2001/12/soap-envelope"" "
		&    "soap:encodingStyle=""http://www.w3.org/2001/12/soap-encoding"">"
		&    "<soap:Body "
		&       "xmlns:m=""http://www.example.org/stock"">"
		&       "<m:GetStockPrice>"
		&          "<m:StockName>IBM</m:StockName>"
		&       "</m:GetStockPrice>"
		&    "</soap:Body>"
		& "</soap:Envelope>" )

	|
	| Inspect node properties
	|

	string property(100)

	property = xmlName$(xml_body)
	ASSERTSEQ( property, "Body" )

	property = xmlQualifiedName$(xml_body)
	ASSERTSEQ( property, "soap:Body" )

	property = xmlPrefix$(xml_body)
	ASSERTSEQ( property, "soap" )

	property = xmlURI$(xml_body)
	ASSERTSEQ( property, "http://www.w3.org/2001/12/soap-envelope" )

	|
	| Use xmlFindFirst (it ignores namespaces)
	|

	ret = xmlFindFirst("Body", xml_envelope)
	ASSERTSEQ( ret, xml_body )

	ret = xmlFindFirst("GetStockPrice", xml_envelope)
	ASSERTSEQ( ret, xml_GetStockPrice )

	ret = xmlFindFirst("soap:Body", xml_envelope)
	ASSERTSEQ( ret, 0 )  | Not found, because the name is "Body", not "soap:Body"

	| Use xmlFindFirstNs
	ret = xmlFindFirstNs("http://www.w3.org/2001/12/soap-envelope", "Body",
		xml_envelope)
	ASSERTSEQ( ret, xml_body )

	ret = xmlFindFirstNs(xmlns_soap, "Body", xml_envelope)
	ASSERTSEQ( ret, xml_body )

	| Search with an incorrect URI binding
	ret = xmlFindFirstNs("http://atwt", "Body", xml_envelope)
	ASSERTSEQ( ret, 0 )

	|
	| Use xmlFindFirstMatch (it ignores namespaces)
	|

	ret = xmlFindFirstMatch( "?<GetStockPrice>.<StockName>", xml_envelope )
	ASSERTSEQ( ret, xml_StockName )

	|
	| Use xmlFindFirstMatchNs
	|

	| Search with prefixes and correct URI bindings.
	ret = xmlFindFirstMatchNs( "?<soap:Body>.<m:GetStockPrice>.<m:StockName>",
			"soap=""http://www.w3.org/2001/12/soap-envelope"","  &
			"m=""http://www.example.org/stock"" ",
			xml_envelope )
	ASSERTSEQ( ret, xml_StockName )

	| Search with prefixes and correct URI bindings. Use different prefixes than
	| in the XML tree.
	ret = xmlFindFirstMatchNs( "?<x:Body>.<y:GetStockPrice>.<y:StockName>",
			"x=""http://www.w3.org/2001/12/soap-envelope""," &
			"y=""http://www.example.org/stock"" ",
			xml_envelope )
	ASSERTSEQ( ret, xml_StockName )

	| Search with prefixes and incorrect URI binding.
	ret = xmlFindFirstMatchNs( "?<x:Body>.<y:GetStockPrice>.<y:StockName>",
			"x=""http:gtst"" , y=""http://www.example.org/stock"" ",
			xml_envelope )
	ASSERTSEQ( ret, 0 )

}
```

## Related topics
- [XML object constraints](constraints.md)

- [XML object glossary](glossary.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)

- [XML object API](api.md)
