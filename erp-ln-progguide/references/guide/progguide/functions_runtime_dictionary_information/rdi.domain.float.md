# rdi.domain.float()

## Syntax:
`function long rdi.domain.float( string domain_name(14), ref long digits_before, ref long digits_after, ref long divide_factor, ref long round_code )`

## Description
This returns information about a domain of type DB.FLOAT.

## Arguments
| | | |
|---|---|---|
| `string` | `domain_name(14)` |  The name of the domain.  |
| `ref long` | `digits_before` |  This returns the number of digits before the decimal point in the specified domain.  |
| `ref long` | `digits_after` |  This returns the number of digits after the decimal point.  |
| `ref long` | `divide_factor` |  This returns the divide factor for the specified domain.  |
| `ref long` | `round_code` |  This returns the rounding mode for the specified domain. Possible values are: 0 truncate (for example, both 1.5 and 1.49 are rounded down to 1) 1 normal round (for example, 1.5 is rounded up to 2; 1.49 is rounded down to 1) 2 round up (for example, both 1.5 and 1.49 are rounded up to 2)  |

## Return values
0 success
-1 error

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
