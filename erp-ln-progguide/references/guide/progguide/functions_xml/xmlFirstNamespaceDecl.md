# xmlFirstNamespaceDecl()

## Syntax:
`function long xmlFirstNamespaceDecl( long node )`

## Description
Get the first namespace declaration from an XML node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is an XML node.  |

## Return values
| | |
|---|---|
| <> 0 | Success; A reference to the first namespace declaration of the *node*.  |
| 0 | Error. The *node* does not carry any namespace declaration.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope
string error(100)
xml_envelope = xmlReadFromStringNs(
  "<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope"" " &
		 " soap:encodingStyle=""http://www.w3.org/2001/12/soap-encoding"">" &
		 "<soap:Body xmlns:m=""http://www.example.org/stock"">" &
			 "<m:GetStockPrice>" &
				 "<m:StockName>IBM</m:StockName>" &
			 "</m:GetStockPrice>" &
		 "</soap:Body>" &
  "</soap:Envelope>"
	, error )

long xmlns
xmlns = xmlFirstNamespaceDecl( xml_envelope )

| xmlns now contains a reference to the xmlns:soap declaration
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [XML object synopsis (namespace support)](synopsis_namespace.md)
