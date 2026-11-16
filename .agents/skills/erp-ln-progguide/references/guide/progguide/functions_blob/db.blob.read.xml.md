# db.blob.read.xml()

## Syntax:
`function long db.blob.read.xml( const string blob.locator, long offset, ref long bytes.read, ref long xml.node, ref string error, long whitespacehandling )`

## Description
This function reads data from the BLOB, to which the BLOB locator refers, and parses it to an XML tree. Before calling *db.blob.read.xml()*, the BLOB locator must be read from the database. For example, the following code retrieves the BLOB locator that refers to a certain picture from a table, and then retrieves the first 256 bytes of the picture:
```

    string bytes.array(256)
    string error(120)
    long bytes.read
    long xml.node
    long ret
    select dbtst000.photo from dbtst000 where dbtst000.item = "001"
    selectdo
        ret = db.blob.read.xml(dbtst000.photo, 1, bytes.read, xml.node, error, XmlPreserveWhiteSpace)
    endselect
```
Note: A parse error is returned when the BLOB is empty; this is similar to parsing an empty string using *XmlReadFromString()*.

## Arguments
| | | |
|---|---|---|
| `const string` | `blob.locator` |  The BLOB locator, which is fetched from the database by e.g. *db.eq* or by a SQL statement  |
| `long` | `offset` |  The offset into the BLOB where the XML parsing starts. The most common pattern is to have a single XML document in a BLOB value; in that case the offset is 1.  |
| `ref long` | `bytes.read` |  Returns the number of bytes that was read by the XML parser.  |
| `ref long` | `xml.node` |  Returns a new xml node that contains the data (don't forget to xmlDelete the node later)  |
| `ref string` | `error` |  contains a description of the error in case a parsing error occurs. This is an English text, which can be used for logging purposes. Maximum length of this error string is 120 characters (this is just like the function *xmlRead*)  |
| `long` | `whitespacehandling` |  whitespacehandling can have one of the three values XmlWhiteSpaceLegacyMode, XmlPreserveWhiteSpace, and XmlReplaceWhiteSpaceBySingleSpace. When this optional argument is not supplied, the value XmlWhiteSpaceLegacyMode is assumed (these values are described in detail for the function *xmlRead*).  |

## Return values
| | |
|---|---|
| 0 | Success. |
| <> 0 | Error, e.g. E_BDB_INVALID_BLOB or E_BDB_XML_PARSE_ERROR |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [BLOB handling overview](overview.md)

- [BLOB handling synopsis](synopsis.md)
