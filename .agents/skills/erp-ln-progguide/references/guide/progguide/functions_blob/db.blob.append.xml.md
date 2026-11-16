# db.blob.append.xml()

## Syntax:
`function long db.blob.append.xml( const string blob.locator, long xml.node, [ long mode, long eflag ] )`

## Description
This function appends data from an XML tree to the BLOB, to which the BLOB locator refers. Before calling *db.blob.append.xml()*, the BLOB locator must be read from the database.
It is required to lock the record. if the lock is a delayed lock then db.blob.append.xml() will promote the delayed lock to a lock in the database automatically (limitation: without EROWCHANGED check on the BLOB data).
A call to db.blob.append.xml() causes a flush of buffered updates. Such a flush can cause a jump to the retry point. Errors that occur in db.blob.append.xml() itself do not cause a jump to the retry point.

## Arguments
| | |
|---|---|
| DB.RETRY | Set this value if retry points are being used. The function can now jump to the retry point under the usual conditions. |

## Return values
| | | |
|---|---|---|
| 0 | Success. |  |
| <> 0 | Error. | for some negative return values additional information can be found with function [xmlWrite()](../functions_xml/serialize_xml_object.md). |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [BLOB handling overview](overview.md)

- [BLOB handling synopsis](synopsis.md)
