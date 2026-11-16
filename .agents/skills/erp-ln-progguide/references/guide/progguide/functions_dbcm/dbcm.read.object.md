# dbcm.read.object()

## Syntax:
`function long dbcm.read.object( const string toid$, [ long comp ] )`

## Description
Reads and makes the business object current, based on the given typed object id. In case the business object consists of multiple tables, the root table is accessed.
When this function is finished the business object's properties can be accessed by means of the table fields of the root table.

## Arguments
| | | |
|---|---|---|
| `const string` | `toid$` |  A Typed Object Id.  |
| `[ long` | `comp ]` |  The company to read in. If not specified, reading is done in the current company.  |

## Return values
| | |
|---|---|
| 0 | The database read was successful. |
| <> 0 | An error occurred. `cDbcm_UnknownTable` (7) is returned in case no root table can be determined, or in case Change Management is not active for the root table. `ENOREC` (111) is returned in case no record can be found. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
