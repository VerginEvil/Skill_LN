# rdi.date.input.format$()

## Syntax:
`function string rdi.date.input.format$( string date_format(7), [ ref string display_format() ] )`

## Description
This returns the input format defined in the data dictionary for a specified date format. The input format can be any combination of day-in-week (D), week-in-year (W), and year (Y), or any combination of day-in-month (D), month-in-year (M), and year (Y). For example, if the function returns MDY, the input format on a form field must be month, day-in-month, and year (for example, 12311998).

## Arguments
| | | |
|---|---|---|
| `string` | `date_format(7)` |  A date format defined in the data dictionary. This must be specified as %D *n* [, *lang*], where *n* is the date format code and *lang* is the language code. See sprintf$()sprintf.  |
| `[ ref string` | `display_format() ]` |  Optional argument which returns the display format for the specified date format.  |

## Return values
The input format defined in the data dictionary for the specified date format.

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
string inpformat(3)
inpformat = rdi.date.input.format$( "D002,3" )
| inpformat e.g. now contains DWY.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
