# xmlDataElementNs$()

## Syntax:
`function string xmlDataElementNs$( long node, void namespaceOrURI, const string name, [ const string default.value, const string data.separator, const string element.separator ] )`

## Description
Get the data of all child nodes of type XML_DATA of those child nodes of type XML_ELEMENT of the *node* whose *local name* matches the specified *name* and whose URI matches the URI specified by *namespaceOrURI*. All data of the XML_DATA nodes is concatenated into a single string. If an XML_ELEMENT node has multiple XML_DATA nodes, then a single space is used as separator.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node.  |
| `void` | `namespaceOrURI` |  *namespaceOrURI* is either a reference to an XML namespace, or it is a URI. If the *namespaceOrURI* parameter is of type *long* then it is a reference to an XML namespace; if it is of type *string* then it is a URI; otherwise the function fails.  |
| `const string` | `name` |  *name* is the *local name* of the child node(s) of type XML_ELEMENT.  |
| `[ const string` | `default.value ]` |  *default.value* is a string that is used as return value when the function fails. When *default.value* is not specified, an empty string is used.  |
| `[ const string` | `data.separator ]` |  Optional argument (available as of [porting set TIV](../tiv/tiv_overview.md) [level 2500](../tiv/tiv_2500.md)) specifying the string used to separate the data of different XML_DATA nodes that are descendants of the same XML_ELEMENT node matching the specified *name* and *namespaceOrURI*. If this argument is not supplied, the default data separator string is used, which contains exactly one space character.  |
| `[ const string` | `element.separator ]` |  Optional argument (available as of [porting set TIV](../tiv/tiv_overview.md) [level 2500](../tiv/tiv_2500.md)) specifying the string used to separate the data of XML_DATA nodes that are descendants of different XML_ELEMENT nodes matching the specified *name* and *namespaceOrURI*. If this argument is not supplied, then the default element separator string is used, which is the empty string.  |

## Return values
| | |
|---|---|
| string | If the *node* is valid, the *namespaceOrURI* is valid, and there is a child XML_ELEMENT node of the *node* whose *local name* matches the specified *name* and whose URI matches the URI specified by *namespaceOrURI* with an XML_DATA node as child, then a temporary string containing the data is returned. Otherwise, the *default.value*, or when this is omitted, the empty string is returned.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope, xml_stockprice
string error(100)
xml_envelope = xmlReadFromStringNs(
	"<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope"" " &
		" soap:encodingStyle=""http://www.w3.org/2001/12/soap-encoding"">" &
		"<soap:Body xmlns:m=""http://www.example.org/stock"">" &
			"<m:GetStockPrice>" &
				"<m:StockName>IBM</m:StockName>" &
			"</m:GetStockPrice>" &
		"</soap:Body>" &
	"</soap:Envelope>" , error )

xml_stockprice = xmlFindFirstNs( "http://www.example.org/stock", "GetStockPrice", xml_envelope )

string data(10)
data = xmlDataElementNs$( xml_stockprice, "http://www.example.org/stock", "StockName", "Def" )

| data now contains "IBM"
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [XML object synopsis (namespace support)](synopsis_namespace.md)
