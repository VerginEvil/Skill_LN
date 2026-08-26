# tt.table.desc()

## Syntax:
`function string tt.table.desc( string table(8), ref string desc() mb )`

## Description
This retrieves the description (in the user's current language) of a specified table ( *table*). It is returned, and optionally also stored in the *desc* argument. (The optional argument is only present for backward compatibility.)

## Arguments
| | | |
|---|---|---|
| `string` | `table(8)` |  |
| `ref string` | `desc() mb` |  |

## Return values
The description is returned.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
