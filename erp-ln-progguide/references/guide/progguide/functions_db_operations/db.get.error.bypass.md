# db.get.error.bypass()

## Syntax:
`function boolean db.get.error.bypass( [ ref boolean with.retry ] )`

## Description
This function returns the current value of error.bypass and, optionally, the current value of error.bypass.with.retry. It is allowed to call this function without having called the db.set.error.bypass.on() function.

## Arguments
| | | |
|---|---|---|
| `[ ref boolean` | `with.retry ]` |  The current value of error.bypass.with.retry.  |

## Return values
The current value of error.bypass.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2020.

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
