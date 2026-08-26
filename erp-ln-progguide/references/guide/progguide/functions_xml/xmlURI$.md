# xmlURI$()

## Syntax:
`function string xmlURI$( long node, [ const string default.value ] )`

## Description
Get the URI of the namespace of the specified node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node.  |
| `[ const string` | `default.value ]` |  *default.value* is a string that is used as return value when the function fails.  |

## Return values
| | |
|---|---|
| string | If the *node* is valid and is in a namespace, then a temporary string containing the URI of the namespace is returned. Otherwise, the *default.value*, or when this is omitted, the empty string is returned.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example:
```

 long   xml_envelope
 string error(100)
 xml_envelope = xmlReadFromStringNs( "<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope""/>", error )

 string URI(100)
 URI = xmlURI$( xml_envelope )
 | URI now contains "http://www.w3.org/2001/12/soap-envelope"
```
A slightly more involved example:
```

 long xml_doc, node, xml_book
 string URI(100)

 xml_doc = xmlReadFromStringNs(
	 "<?xml version=""1.0""?>"
	 &   "<doc>"
	 &      "<book xmlns=""http://books.nu"">"
	 &         "<b:chapter xmlns:b=""http://books.chapter.nu""/>"
	 &         "<b:chapter xmlns:b=""http://books.chapter.net""/>"
	 &      "</book>"
	 &   "</doc>"
	 , error )

 | Find the first node with local name "book", ignoring the namespace
 xml_book = xmlFindFirstNs( 0, "book", xml_doc )

 | retrieve the URI
 URI = xmlURI$(xml_book)
 | The string URI now contains "http://books.nu"
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [XML object synopsis (namespace support)](synopsis_namespace.md)
