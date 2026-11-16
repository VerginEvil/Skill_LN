# xmlFindFirstMatchNs()

## Syntax:
`function long xmlFindFirstMatchNs( string pattern, const string namespaceList, long fromNode, [ long toNode ] )`

## Description
Search in a tree or a list of trees and return the first XML_ELEMENT or XML_DTD, which matches with the string pattern. The string pattern contains a search path relative to the starting node. The starting node is the list of nodes indicated by *fromNode* to *toNode*.

## Arguments
```

Pattern        ::=   Part [ '.' Part ]*
Part           ::=   DepthSearch | BreadthSearch | ParentSearch | Tag |
                     RightSibling | LeftSibling |  FirstChild | LastChild | Parent
DepthSearch    ::=   '?' Tag
BreadthSearch  ::=   '-' Tag
ParentSearch   ::=   '^' Tag
Tag            ::=   '<' [Name] [Attribute]*  '>'
Name           ::=   Element name, see for a definition:  [XMLSTD].
Attribute      ::=   attname'='attvalue | attname | attname'=' | '='attvalue
RightSibling   ::=   "right"
LeftSibling    ::=   "left"
FirstChild     ::=   "fChild"
LastChild      ::=   "lChild"
Parent         ::=   "parent"
```
| | | |
|---|---|---|
| `string` | `pattern` |  The parameter *pattern* is a string which should conform to the following syntax: Both an element name and an attribute name can be *qualified*. The *namespaceList* is then used to bind the prefix to the corresponding namespace name (URI). The URI of the element or attribute must match the specified URI in the *namespaceList* for a successful match. Attribute values should be surrounded by double quotes. When the text inside a tag starts with a stand alone identifier (not followed by an equals sign '='), then, according to the above syntax, it is ambiguous whether it is an element name or an attribute name. In fact, it is interpreted as an element name. When an attribute name is meant, it should in this case be followed by an equals sign '='. This is not necessary for further attributes.  |
| `const string` | `namespaceList` |  *namespaceList* is a string containing a list of prefix-URI bindings. The string must have the form <prefix>="<URI>"[,<prefix>="<URI>"...], and may be empty. The function [xmlBuildNamespaceList$()](xmlBuildNamespaceList$.md) can be used to build this list.  |
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See [fromNode and toNode](api.md#fromnode_tonode).  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See [fromNode and toNode](api.md#fromnode_tonode).  |

## Return values
| | |
|---|---|
| <> 0 | Success; Reference to first matching Node. |
| 0 | Error or no match found. |

## Context
This function is implemented in the porting set and can be used in all script types.

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

long xml_stockprice
xml_stockprice = xmlFindFirstMatchNs( "?<x:GetStockPrice>", "x=""http://www.example.org/stock""", xml_envelope)
| xml_stockprice now contains a reference to the "m:GetStockPrice" node

xml_stockprice = xmlFindFirstMatchNs( "?<x:GetStockPrice>", xmlBuildNamespaceList$("x","http://www.example.org/stock"), xml_envelope)
| xml_stockprice now contains a reference to the "m:GetStockPrice" node
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
