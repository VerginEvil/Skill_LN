# rdi.format.digits()

## Syntax:
`function long rdi.format.digits( string format(), ref long digits.before, ref long digits.after, [ ref string display.format() ] )`

## Description
This returns information about a specified format.

## Arguments
| | | |
|---|---|---|
| `string` | `format()` |  The format code of a double or float.  |
| `ref long` | `digits.before` |  Number of digits before the decimal point  |
| `ref long` | `digits.after` |  Number of digits after the decimal point  |
| `[ ref string` | `display.format() ]` |  Optional argument where the display format is stored  |

## Return values
0 success
-1 error

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
