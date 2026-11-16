# dbcm.get.rcd.action()

## Syntax:
`function long dbcm.get.rcd.action( long tbl.id )`

## Description
Retrieves the CM Action of the current record of the given table id.
The CM Action of a record is set when the checked-out version of that particular record is different from the checked-in version.

## Arguments
| | | |
|---|---|---|
| `long` | `tbl.id` |  A table id as returned by [db.bind()](../functions_db_operations/db.bind.md), or a standard table id, like ttdsls400.  |

## Return values
| | |
|---|---|
| CMAC_NONE (0) | There is no checked-out version of this record. Note that this particular may still be part of a checked-out business object. Conceptually, the complete business object is checked-out, however on individual record level, some records may still be unchanged, compared to the checked-in version. |
| CMAC_INSERT (1) | The record has been inserted. This means that there is only a checked-out version of this record and no checked-in version. |
| CMAC_UPDATE (2) | The record has been updated. This means that there two versions of this record, a checked-in and a checked-out one, which differ from each other. |
| CMAC_DELETE (3) | The record has been deleted. This means that physically there are two versions of this record, a checked-in and a checked-out one. However, the checked-out one cannot be retrieved from the database with a query. So conceptually, this record has been deleted from the checked-out business object. |
| CMAC_GHOST (11) | Very short lived value that can be visible using a dirty read database |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
