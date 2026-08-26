# De-serialize XML Object from String

## Syntax:
`function long xmlReadFromString( string xmlString, ref string error, [ long whitespacehandling ] )`

## Description
De-serialize an XML object by parsing an XML document and creating an in-memory object tree.
The default encoding is [UTF-8](../misc/utf8.md). Encodings [UTF-16](../misc/utf16.md) and ISO-8859-1 are supported as well.
Unicode Normalization Form C (NFC: Canonical Decomposition, followed by Canonical Composition) is applied during the de-serialization. See Unicode Standard Annex #15: Unicode Normalization Forms

## Arguments
| | | |
|---|---|---|
| `string` | `xmlString` |  *xmlString* must be a string buffer which contains an XML document.  |
| `ref string` | `error` |  *error* contains a description of the error in case a parsing error occurs. This is an English text, which can be used for logging purposes. Maximum length of this error string is 512 characters.  |
| `[ long` | `whitespacehandling ]` |  whitespacehandling can have one of the three values XmlWhiteSpaceLegacyMode, XmlPreserveWhiteSpace, and XmlReplaceWhiteSpaceBySingleSpace. When this optional argument is not supplied, the value XmlWhiteSpaceLegacyMode is assumed. The meaning of the allowed values is as follows:  |

## Return values
| | |
|---|---|
| <> 0 | Success; A reference to the first in-memory node when successful.  |
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
