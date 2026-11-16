# rdi.domain.byte()

## Syntax:
`function long rdi.domain.byte( string domain_name(14), ref long digits )`

## Description
This returns information about a domain of type DB.BYTE.

## Arguments
| | | |
|---|---|---|
| `string` | `domain_name(14)` |  The name of the domain.  |
| `ref long` | `digits` |  This returns the number of digits defined for the byte-type domain.  |

## Return values
0 success
-1 error

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
