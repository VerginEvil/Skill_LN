# dbcm.is.deployed.root.table()

## Syntax:
`function boolean dbcm.is.deployed.root.table( const string tbl.name$, [ long comp ] )`

## Description
Tests whether the given table is an Object Type root table for any of the object types deployed for the (implicitly or explicitly) given company number, as defined in the Object Configuration Management model for the current package combination.

## Arguments
| | | |
|---|---|---|
| `const string` | `tbl.name$` |  A table code, like "tdsls400".  |
| `[ long` | `comp ]` |  (optional) The company, if not specified: the current company.  |

## Return values
| | |
|---|---|
| true | In case the given table is a root table for the specified company. |
| false | In any other case. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2470.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Availability  This function is available from bshell TIV 2470 (Porting set 9.4h). With an older bshell, it returns false.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
