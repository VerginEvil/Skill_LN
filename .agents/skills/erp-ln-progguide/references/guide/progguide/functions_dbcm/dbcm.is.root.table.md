# dbcm.is.root.table()

## Syntax:
`function boolean dbcm.is.root.table( const string tbl.name$ )`

## Description
Tests whether the given table is an Object Type root table, as defined in the Object Configuration Management model for the current package combination.

## Arguments
| | | |
|---|---|---|
| `const string` | `tbl.name$` |  A table code, like "tdsls400".  |

## Return values
| | |
|---|---|
| true | In case the given table is a root table. |
| false | In any other case. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
