# xmlNextNamespaceDecl()

## Syntax:
`function long xmlNextNamespaceDecl( long namespace )`

## Description
Get the next namespace declaration of an XML node.

## Arguments
| | | |
|---|---|---|
| `long` | `namespace` |  *namespace* is a reference to an XML namespace.  |

## Return values
| | |
|---|---|
| <> 0 | Success; A reference to the next namespace declaration of an XML node that carries the specified *namespace*.  |
| 0 | Error. The *namespace* is invalid or it does not have a next namespace declaration, within the context of the same XML node.  |

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

xmlns = xmlNextNamespaceDecl( xmlns )
| xmlns is now 0, because the soap:Envelope node has only one namespace declaration
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [XML object synopsis (namespace support)](synopsis_namespace.md)
