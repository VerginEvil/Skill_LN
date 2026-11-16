# dal.get.field.mode()

## Syntax:
`#include <bic_dam>`
`function long dal.get.field.mode( string tbl.name, [ long element ] )`

## Description
Returns the mode of the given field. The mode indicates if the field has changed.
This function is equivalent to:
`dal.get.property.flag(tbl.name, tbl.cursor, fld.name)`

## Arguments
| | | |
|---|---|---|
| `string` | `tbl.name` |  the name of the field  |
| `[ long` | `element ]` |  optional element of the field in case of arrays (default is 1)  |

## Return values
| | |
|---|---|
| 0 | Field is not changed |
| DAL_NEW | Field has changed during insert of a record |
| DAL_UPDATE | Field has changed during update of a record |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  This function should not be used after the actual insert/update has been done. E.g. it should not be used in any 'after' hook in the DAL, Table Extension DLL or DB DLL.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
