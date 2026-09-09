# xmlGetPredefinedNamespace()

## Syntax:
`function long xmlGetPredefinedNamespace( const string prefix )`

## Description
Get one of the predefined XML namespaces. This function returns a reference to it. The reference can be used in for example the [xmlNewNodeNs()](xmlNewNodeNs.md) function.
According to [Namespaces in XML 1.0 (Third Edition)](https://www.w3.org/TR/REC-xml-names), Chapter 3 Declaring Namespaces, there are two predefined namespaces:
| | |
|---|---|
| prefix | URI |
| xml | http://www.w3.org/XML/1998/namespace |
| xmlns | http://www.w3.org/2000/xmlns/ |

## Arguments
| | | |
|---|---|---|
| `const string` | `prefix` |  *prefix* is the prefix used to identify the predefined namespace.  |

## Return values
| | |
|---|---|
| <> 0 | Success. A reference to the predefined namespace when successful. |
| 0 | Error. The *prefix* is not the prefix of a predefined namespace. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2500.

## Example
```

long xml_root
string error(100)
xml_root = xmlReadFromStringNs( "<root xml:space=""preserve""/>", error )
long xmlns_xml
xmlns_xml = xmlGetPredefinedNamespace( "xml" )

| xmlNamespacePrefix$( xmlns_xml ) would return "xml".
| xmlNamespaceURI$( xmlns_xml ) would return "http://www.w3.org/XML/1998/namespace".
| xmlAttributeNs$( xml_root, xmlns_xml, "space" ) would return "preserve".
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
