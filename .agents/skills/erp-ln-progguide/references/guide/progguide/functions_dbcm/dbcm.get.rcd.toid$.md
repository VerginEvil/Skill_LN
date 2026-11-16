# dbcm.get.rcd.toid$()

## Syntax:
`function string dbcm.get.rcd.toid$( long tbl.id )`

## Description
Retrieves the Typed Object ID of the current record of the given table id.

## Arguments
| | | |
|---|---|---|
| `long` | `tbl.id` |  A table id as returned by [db.bind()](../functions_db_operations/db.bind.md), or a standard table id, like ttdsls400.  |

## Return values
The Typed Object ID, or an empty string in case no Typed Object ID could be found.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
