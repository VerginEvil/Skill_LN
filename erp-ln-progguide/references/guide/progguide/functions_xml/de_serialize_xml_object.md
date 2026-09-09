# De-serialize XML Object

## Syntax:
`function long xmlRead( long fp, ref string error, [ long whitespacehandling ] )`

## Description
De-serialize an XML object by parsing an XML document and creating an in-memory object tree.
The default encoding is [UTF-8](../misc/utf8.md). Encodings [UTF-16](../misc/utf16.md) and ISO-8859-1 are supported as well.
Unicode Normalization Form C (NFC: Canonical Decomposition, followed by Canonical Composition) is applied during the de-serialization. See [Unicode Standard Annex #15: Unicode Normalization Forms](http://www.unicode.org/reports/tr15/tr15-23.html)

## Arguments
| | |
|---|---|
| whitespacehandling |  |
| XmlWhiteSpaceLegacyMode | *XmlWhiteSpaceLegacyMode* means that white space is handled the same way as it was done in older versions of these functions, which did not have the whitespacehandling argument. This means (1) that each newline character in the input starts a new data node, (2) that leading white space in a data node is removed, and (3) that empty data nodes are removed. |
| XmlPreserveWhiteSpace | *XmlPreserveWhiteSpace* means that all white space in the XML document is preserved. However, it should be noted that any carriage-return line-feed character pair and any carriage-return character that is not followed by a line-feed character is translated to a single line-feed character. See also [XMLSTD], section 2.11. |
| XmlReplaceWhiteSpaceBySingleSpace | *XmlReplaceWhiteSpaceBySingleSpace* means (1) that leading and trailing white space in a data node is removed, (2) that empty data nodes are removed, and (3) that internal white space in a data node is replaced by one single space character. |
It is possible to switch between the two modes XmlPreserveWhiteSpace and XmlReplaceWhiteSpaceBySingleSpace by means of the xml:space attribute. The value "preserve" switches the mode to XmlPreserveWhiteSpace. The value "default" (or any other value than "preserve") switches the mode to XmlReplaceWhiteSpaceBySingleSpace. The value of the xml:space attribute is considered to apply to all elements within the content of the element where it is specified, unless overridden with another instance of the xml:space attribute. See also [XMLSTD], Section 2.10. In XmlWhiteSpaceLegacyMode, the xml:space attribute is ignored.

## Return values
| | |
|---|---|
| <> 0 | Success; A reference to the first in-memory node when successful. |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related
```

long	xmlRead(long fp, ref string error, [ long whitespacehandling ] )
long	xmlReadFromString(string xmlString, ref string error, [ long whitespacehandling ] )
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
