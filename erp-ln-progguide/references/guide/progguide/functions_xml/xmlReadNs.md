# xmlReadNs()

## Syntax:
`function long xmlReadNs( long fp, ref string error, [ long whitespacehandling ] )`

## Description
De-serialize an XML object by parsing an XML document and creating an in-memory object tree. This function supports XML namespaces, and will create namespace declarations carried by the respective XML nodes, and put XML nodes in their appropriate namespace.
The default encoding is [UTF-8](../misc/utf8.md). Encodings [UTF-16](../misc/utf16.md) and ISO-8859-1 are supported as well.
Unicode Normalization Form C (NFC: Canonical Decomposition, followed by Canonical Composition) is applied during the de-serialization. See Unicode Standard Annex #15: Unicode Normalization Forms

## Arguments
| | | |
|---|---|---|
| `long` | `fp` |  fp must be a file pointer opened for read obtained from a call to seq.open(), pipe.open(), ims.openfba() or ims.openvba().  |
| `ref string` | `error` |  error contains a description of the error in case a parsing error occurs. This is an English text, which can be used for logging purposes. Maximum length of this error string is 120 characters.  |
| `[ long` | `whitespacehandling ]` |  whitespacehandling can have one of the three values XmlWhiteSpaceLegacyMode, XmlPreserveWhiteSpace, and XmlReplaceWhiteSpaceBySingleSpace. When this optional argument is not supplied, the value XmlWhiteSpaceLegacyMode is assumed. The meaning of the allowed values is as follows:  |

## Return values
| | |
|---|---|
| <> 0 | Success; A reference to the first in-memory node when successful.  |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long vba
vba = ims.openvba( "w+" )
ims.write(
  "<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope"" " &
		 " soap:encodingStyle=""http://www.w3.org/2001/12/soap-encoding"">" &
		 "<soap:Body xmlns:m=""http://www.example.org/stock"">" &
			 "<m:GetStockPrice>" &
				 "<m:StockName>IBM</m:StockName>" &
			 "</m:GetStockPrice>" &
		 "</soap:Body>" &
  "</soap:Envelope>", 9999, vba )
ims.rewind( vba )

long xml_envelope
string error(100)
xml_envelope = xmlReadNs( vba, error )

| xml_envelope now contains a reference to an XML tree
```
The tree contains a namespace declaration on the `soap:Envelope` node and one on the `soap:Body` node. The functions [xmlPrefix$()](xmlPrefix$.md), [xmlQualifiedName$()](xmlQualifiedName$.md), [xmlURI$()](xmlURI$.md), [xmlFirstNamespaceDecl()](xmlFirstNamespaceDecl.md), and others can be used to inspect the created XML tree.

## Related
```

long	xmlRead(long fp, ref string error, [ long whitespacehandling ] )
long	xmlReadFromString(string xmlString, ref string error, [ long whitespacehandling ] )
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [XML object synopsis (namespace support)](synopsis_namespace.md)
