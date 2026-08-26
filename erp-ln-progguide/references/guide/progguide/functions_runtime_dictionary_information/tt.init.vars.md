# tt.init.vars()

## Syntax:
`function void tt.init.vars( ref void variable, [ ... ] )`

## Description
This sets 1 or more variables to the 0 or empty value. This works for arrays as well.
Strings are set to emptry string and numbers are set to 0 and enums are set to empty.

## Arguments
| | | |
|---|---|---|
| `ref void` | `variable` |  Reference argument to be initialized. This can be a single variable or an array.  |
| `[` | `... ]` |  0 or more time  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2360.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
