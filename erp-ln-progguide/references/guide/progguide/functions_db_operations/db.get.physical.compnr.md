# db.get.physical.compnr()

## Syntax:
`function long db.get.physical.compnr( string tblname, long logical.compnr )`

## Description
Use this to retrieve the physical company number for the specified table ( *tblname*) and logical company number ( *logical.compnr*).
Note: the function doesn't check whether the table *tblname* exists or not.

## Arguments
| | | |
|---|---|---|
| `string` | `tblname` |  The name of the table.db.bind  |
| `long` | `logical.compnr` |  The name of the logical company.  |

## Return values
| | |
|---|---|
| >= 0 | Success: the company number. |
| -1 | Error. The *tblname* or the *logical.compnr* is not correct. (e is set to E_BADARG) |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
