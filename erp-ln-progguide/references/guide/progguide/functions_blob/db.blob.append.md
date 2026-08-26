# db.blob.append()

## Syntax:
`function long db.blob.append( const string blob.locator, long num.bytes, const string bytes.array, [ long mode, long eflag ] )`

## Description
This function appends data to the BLOB, to which the BLOB locator refers. Before calling *db.blob.append()*, the BLOB locator must be read from the database.
It is required to lock the record. if the lock is a delayed lock then db.blob.append() will promote the delayed lock to a lock in the database automatically (limitation: without EROWCHANGED check on the BLOB data).
A call to db.blob.append() causes a flush of buffered updates. Such a flush can cause a jump to the retry point. Errors that occur in db.blob.append() itself do not cause a jump to the retry point.
For example, the following code retrieves the BLOB locator that refers to a certain picture from a table, and then appends data to the BLOB:
```

    long num.bytes
    long ret
    string blobdata(100)

    blobdata = "the quick brown fox jumps over the lazy dog"
    num.bytes = len(blobdata)

    select dbtst000.photo from dbtst000 for update where dbtst000.item = "001"
    selectdo
    	ret = db.blob.append(dbtst000.photo, num.bytes, blobdata)
    endselect
    commit.transaction()
```

## Arguments
| | | |
|---|---|---|
| `const string` | `blob.locator` |  The BLOB locator, which is fetched from the database by e.g. *db.eq* or by a SQL statement  |
| `long` | `num.bytes` |  The number of bytes to append to the BLOB  |
| `const string` | `bytes.array` |  The buffer with the BLOB data  |
| `[ long` | `mode ]` |  This has one possible value:  |
| `[ long` | `eflag ]` |  For some errors, it is possible to indicate the action the system must perform when the error occurs. You use this argument to specify the required action(s). See [Error handling](../functions_database_handling/error_handling.md)  |

## Return values
| | |
|---|---|
| 0 | Success. |
| <> 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [BLOB handling overview](overview.md)
- [BLOB handling synopsis](synopsis.md)
