# tt.index.desc()

## Syntax:
`function string tt.index.desc( string tabl(8), long indexnr, [ ref string desc() mb ] )`

## Description
This returns information about a specified table index. It is returned, and optionally also stored in the *desc* argument. (The optional argument is only present for backward compatibility.)

## Arguments
| | | |
|---|---|---|
| `string` | `tabl(8)` |  The table name.  |
| `long` | `indexnr` |  The index number.  |
| `[ ref string` | `desc() mb ]` |  This returns the description (in the user's current language) of the specified index.  |

## Return values
The description is returned.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
