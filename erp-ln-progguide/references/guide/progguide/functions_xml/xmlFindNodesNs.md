# xmlFindNodesNs()

## Syntax:
`function long xmlFindNodesNs( long node, void namespaceOrURI, const string name, long maxFound, [ ref long numFound ] )`

## Description
In an XML tree, find all XML nodes of type XML_ELEMENT or XML_DTD, whose *local name* matches the specified *name* and whose URI matches the URI specified by *namespaceOrURI*. This is a *depth first* search.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node.  |
| `void` | `namespaceOrURI` |  *namespaceOrURI* is either a reference to an XML namespace, or it is a URI. If the *namespaceOrURI* parameter is of type *long* then it is a reference to an XML namespace; if it is of type *string* then it is a URI; otherwise the function fails.  |
| `const string` | `name` |  *name* is the *local name* of the node(s) of type XML_ELEMENT or XML_DTD.  |
| `long` | `maxFound` |  *maxFound* is the maximum number of matches to be returned. When its value is 0 then all matches will be returned.  |
| `[ ref long` | `numFound ]` |  *numFound* is a reference variable, and contains the number of matches found.  |

## Return values
The return value refers to a new tree, which contains the NodeId's of the nodes which match the *pattern*. This new tree corresponds to an XML document as shown below:
```

<Enumeration TYPE="InMemory XmlNodes">
        <e0>id0</e0>
        <e1>id1</e1>
        ...
        <en>idn</en>
</Enumeration>
```
In this example *idn* is the decimal string representation of a nodeId of a node, which matches the *pattern*.
Like any other tree of Nodes, the returned tree must be freed from memory by using xmlDelete().
| | |
|---|---|
| <> 0 | Success; The new tree containing the references to the matching nodes. In case no match is found the tree consists of a single node. |
| 0 | Error; either the *namespaceOrURI* is invalid, or the *node* is invalid. |

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

long numFound
xml_stockprice = xmlFindNodesNs( xml_envelope, "http://www.example.org/stock", "GetStockPrice", 0, numFound )

| numFound now contains 1
| xml_stockprice now contains a reference to the "GetStockPrice" node, in the following XML:
|
|	<Enumeration
|		TYPE="InMemory XmlNodes">
|		<e0>2147483641</e0>
|	<Enumeration>
|
| The value 2147483641 is the reference to the "GetStockPrice" node.
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
