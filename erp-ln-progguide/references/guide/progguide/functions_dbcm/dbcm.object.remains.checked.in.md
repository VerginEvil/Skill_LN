# dbcm.object.remains.checked.in()

## Syntax:
`function long dbcm.object.remains.checked.in( ref long tbl.id, long cmac, ref boolean b.eval )`

## Description
Tests whether the business object related to the current record buffer remains checked in.

## Arguments
| | | |
|---|---|---|
| `ref long` | `tbl.id` |  A table id as returned by [db.bind()](../functions_db_operations/db.bind.md), or a standard table id, like ttdsls400.  |
| `long` | `cmac` |  An CM Action type. Parameter cmac should be one of the following values: `CMAC_INSERT, CMAC_UPDATE, CMAC_DELETE`.  |
| `ref boolean` | `b.eval` |  Indicates whether the business object related to the current record buffer will be checked out ('false') or remains checked in ('true').  |

## Return values
| | |
|---|---|
| 0 | In case of success. |
| <> 0 | In case an error occurred such as: table id is invalid, object could not be determined or CheckOutCondition could not be evaluated. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
