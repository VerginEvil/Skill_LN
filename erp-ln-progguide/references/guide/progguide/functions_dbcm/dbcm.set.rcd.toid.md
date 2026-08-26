# dbcm.set.rcd.toid()

## Syntax:
`function void dbcm.set.rcd.toid( long tbl.id, const string toid$ )`

## Description
Sets the given Typed Object ID in the (default) record buffer the given table.

## Arguments
| | | |
|---|---|---|
| `long` | `tbl.id` |  A table id as returned by [db.bind()](../functions_db_operations/db.bind.md), or a standard table id, like ttdsls400.  |
| `const string` | `toid$` |  A Typed Object ID.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Preconditions
CM should be active for the given table.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
