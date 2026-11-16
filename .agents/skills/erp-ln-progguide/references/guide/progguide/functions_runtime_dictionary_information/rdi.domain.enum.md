# rdi.domain.enum()

## Syntax:
`function long rdi.domain.enum( string domain_name(14), ref long no_enum_items )`

## Description
This returns information about a domain of type DB.ENUM.

## Arguments
| | | |
|---|---|---|
| `string` | `domain_name(14)` |  The name of the domain.  |
| `ref long` | `no_enum_items` |  The number of enum items in the specified domain.  |

## Return values
0 success
-1 error

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
