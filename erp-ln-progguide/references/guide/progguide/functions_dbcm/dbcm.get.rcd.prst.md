# dbcm.get.rcd.prst()

## Syntax:
`function enum dbcm.get.rcd.prst( long tbl.id )`

## Description
Retrieves the checked-in value of the workflow application status field (identified by dbcm.get.app.status.field())of business object related to the current record buffer.

## Arguments
| | | |
|---|---|---|
| `long` | `tbl.id` |  A table id as returned by [db.bind()](../functions_db_operations/db.bind.md), or a standard table id, like ttdsls400.  |

## Return values
| | |
|---|---|
| empty |  The current record buffer is not a record of the root table of any object type or the object type does not have workflow application status field or no checked-in version of the business object related to this current record buffer.  |
| <> empty |  the current record buffer is a record of the root table and the related object type has a workflow application status field.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
