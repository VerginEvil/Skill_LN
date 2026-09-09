# db.blob.size()

## Syntax:
`function long db.blob.size( const string blob.locator, ref long num.bytes )`

## Description
This function retrieves the size of the BLOB, to which the BLOB locator refers. Before calling *db.blob.size()*, the BLOB locator must be read from the database. For example, the following code retrieves the BLOB locator that refers to a certain picture from a table, and then retrieves the size of the picture:
```

    long num.bytes
    long ret
    select dbtst000.photo from dbtst000 where dbtst000.item = "001"
    selectdo
        ret = db.blob.size(dbtst000.photo, num.bytes)
    endselect
```

## Arguments
| | | |
|---|---|---|
| `const string` | `blob.locator` |  The BLOB locator, which is fetched from the database by e.g. *db.eq* or by a SQL statement  |
| `ref long` | `num.bytes` |  Returns the size of the BLOB in bytes  |

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
