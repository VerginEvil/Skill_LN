# rdi.domain.string()

## Syntax:
`function long rdi.domain.string( string domain_name(14), ref long length, ref long convert )`

## Description
This returns information about a domain of type DB.STRING.

## Arguments
| | | |
|---|---|---|
| `string` | `domain_name(14)` |  The name of the domain.  |
| `ref long` | `length` |  This returns the defined length of the string (in bytes).  |
| `ref long` | `convert` |  This returns the conversion mode of the domain. Possible values are: RDI.UPPER RDI.LOWER RDI.NONE  |

## Return values
0 success
-1 error

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
