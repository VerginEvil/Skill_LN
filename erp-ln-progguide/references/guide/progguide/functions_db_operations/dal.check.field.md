# dal.check.field()

## Syntax:
`#include <bic_dam>`
`function long dal.check.field( string fld.name, [ long element, long mode ] )`

## Description
Checks whether the given field has a valid value. This performs the DAL check hooks in the given mode (default is DAL_UPDATE).

## Arguments
| | | |
|---|---|---|
| `string` | `fld.name` |  the name of the field  |
| `[ long` | `element ]` |  optional element of the field in case of array fields (default is 1)  |
| `[ long` | `mode ]` |  mode for the check (default is DAL_UPDATE)  |

## Return values
| | |
|---|---|
| 0 | Field is valid |
| DALHOOKERROR | Field is invalid |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
