# rdi.domain.raw()

## Syntax:
`function long rdi.domain.raw( string domain_name(14), ref long length )`

## Description
This returns information about a domain of type DB.RAW.

## Arguments
| | | |
|---|---|---|
| `string` | `domain_name(14)` |  The name of the domain.  |
| `ref long` | `length` |  This returns the defined length of the raw string (in bytes).  |

## Return values
0 success
-1 error

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
