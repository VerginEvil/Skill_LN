# tt.company()

## Syntax:
`function boolean tt.company( long company, ref string comp_desc() mb, ref string deflt_curr(), ref long first_weekday )`

## Description
This returns information about a specified company.

## Arguments
| | | |
|---|---|---|
| `long` | `company` |  The company number.  |
| `ref string` | `comp_desc() mb` |  This returns the company description.  |
| `ref string` | `deflt_curr()` |  This returns a string containing the default currency of the company.  |
| `ref long` | `first_weekday` |  This returns the first day of the week defined for the company in the data dictionary. The returned number is relative to Sunday(=1)  |

## Return values
false error; company not found
true success

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
