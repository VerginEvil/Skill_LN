# xmlFindFirstNs()

## Syntax:
`function long xmlFindFirstNs( void namespaceOrURI, const string name, long fromNode, [ long toNode ] )`

## Description
In an XML tree, or a list of XML trees, find the first XML node of type XML_ELEMENT or XML_DTD, whose *local name* matches the specified *name* and whose URI matches the URI specified by *namespaceOrURI*. This is a *depth first* search.

## Arguments
| | | |
|---|---|---|
| `void` | `namespaceOrURI` |  *namespaceOrURI* is either a reference to an XML namespace, or it is a URI. If the *namespaceOrURI* parameter is of type *long* then it is a reference to an XML namespace; if it is of type *string* then it is a URI; otherwise the function fails.  |
| `const string` | `name` |  *name* is the *local name* of the node(s) of type XML_ELEMENT or XML_DTD.  |
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See fromNode and toNode.  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See fromNode and toNode.  |

## Return values
| | |
|---|---|
| <> 0 | Success; the XML node that matches the criteria. |
| 0 | Error; either the *namespaceOrURI* is invalid, or the *fromNode* is invalid, or the *toNode* is invalid, or no XML node that matches the criteria could be found.  |

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

| xml_stockprice now contains a reference to the "GetStockPrice" node
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [XML object synopsis (namespace support)](synopsis_namespace.md)
