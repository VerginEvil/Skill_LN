# xmlGetDataElementLengthNs()

## Syntax:
`function long xmlGetDataElementLengthNs( long node, void namespaceOrURI, const string name, [ long data.separator.length, long element.separator.length ] )`

## Description
Get the length of the data of all child nodes of type XML_DATA of those child nodes of type XML_ELEMENT of the *node* whose *local name* matches the specified *name* and whose URI matches the URI specified by *namespaceOrURI*. All data of the XML_DATA nodes is concatenated into a single string. If an XML_ELEMENT node has multiple XML_DATA nodes, then a single space is used as separator.
This function may be used to determine the required size of the *data* argument supplied to [xmlGetDataElementNs()](xmlGetDataElementNs.md).

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node.  |
| `void` | `namespaceOrURI` |  *namespaceOrURI* is either a reference to an XML namespace, or it is a URI. If the *namespaceOrURI* parameter is of type *long* then it is a reference to an XML namespace; if it is of type *string* then it is a URI; otherwise the function fails.  |
| `const string` | `name` |  *name* is the *local name* of the child node(s) of type XML_ELEMENT.  |
| `[ long` | `data.separator.length ]` |  Optional argument (available as of [porting set TIV](../tiv/tiv_overview.md) [level 2500](../tiv/tiv_2500.md)) specifying the length in bytes of the separator string used to separate the data of different XML_DATA nodes that are descendants of the same XML_ELEMENT node matching the specified *name* and *namespaceOrURI*. If this argument is not supplied, default value 1 is used, corresponding to the default data separator string, which contains exactly one space character.  |
| `[ long` | `element.separator.length ]` |  Optional argument (available as of [porting set TIV](../tiv/tiv_overview.md) [level 2500](../tiv/tiv_2500.md)) specifying the length in bytes of the separator string used to separate the data of XML_DATA nodes that are descendants of different XML_ELEMENT nodes matching the specified *name* and *namespaceOrURI*. If this argument is not supplied and the *data.separator.length* argument *is* supplied, then default value 0 is used, corresponding to the default element separator string, which is the empty string. If both this argument and the *data.separator.length* argument are not supplied, then this function has the original behavior (as before [porting set TIV](../tiv/tiv_overview.md) [level 2500](../tiv/tiv_2500.md)): for both arguments default value 1 is used, corresponding to the default data separator string, which contains exactly one space character, but *not* corresponding to the default element separator string, which is the empty string.  |

## Return values
| | |
|---|---|
| >= 0 | Success; The length of the value. |
| -1 | The *node* is invalid, or the *namespaceOrURI* is invalid, or there is no child XML_ELEMENT node of the *node* whose *local name* matches the specified *name* and whose URI matches the URI specified by *namespaceOrURI* with an XML_DATA node as child, |

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

long length
length = xmlGetDataElementLengthNs( xml_stockprice, "http://www.example.org/stock", "StockName" )

| length now contains 3, the length of "IBM"
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
