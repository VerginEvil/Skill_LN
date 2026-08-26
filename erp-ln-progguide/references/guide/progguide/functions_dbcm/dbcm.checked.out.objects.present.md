# dbcm.checked.out.objects.present()

## Syntax:
`function boolean dbcm.checked.out.objects.present( long comp, [ string tbl.name$ ] )`

## Description
Checks if checked-out objects exist in given company and (if provided) given table.

## Arguments
| | | |
|---|---|---|
| `long` | `comp` |  Company number.  |
| `[ string` | `tbl.name$ ]` |  A table code, like "tdsls400", if not specified, tables are not checked.  |

## Return values
| | |
|---|---|
| true | Checked out objects are present in given company (and table). |
| false | In any other case. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
