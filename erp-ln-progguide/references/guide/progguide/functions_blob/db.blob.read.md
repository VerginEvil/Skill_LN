# db.blob.read()

## Syntax:
`function long db.blob.read( const string blob.locator, long offset, long num.bytes, ref string bytes.array, ref long num.bytes.read )`

## Description
This function reads data from the BLOB, to which the BLOB locator refers. Before calling *db.blob.read()*, the BLOB locator must be read from the database. For example, the following code retrieves the BLOB locator that refers to a certain picture from a table, and then retrieves the first 256 bytes of the picture:
```

    string bytes.array(256)
    long num.bytes
    long ret
    select dbtst000.photo from dbtst000 where dbtst000.item = "001"
    selectdo
        ret = db.blob.read(dbtst000.photo, 1, 256, bytes.array, num.bytes)
    endselect
```

## Arguments
| | | |
|---|---|---|
| `const string` | `blob.locator` |  The BLOB locator, which is fetched from the database by e.g. *db.eq* or by a SQL statement  |
| `long` | `offset` |  The offset at which to read data from the BLOB  |
| `long` | `num.bytes` |  The number of bytes to read from the BLOB  |
| `ref string` | `bytes.array` |  The buffer for the BLOB data  |
| `ref long` | `num.bytes.read` |  Returns the number of bytes read. This can be lower than *num.bytes* when reading at or beyond the end of a BLOB value  |

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
