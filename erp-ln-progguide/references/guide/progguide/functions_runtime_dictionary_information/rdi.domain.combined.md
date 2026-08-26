# rdi.domain.combined()

## Syntax:
`function long rdi.domain.combined( string domain_name(14), ref string child_domains(14, 32) )`

## Description
This returns information about a domain of type DB.COMBINED.

## Arguments
| | | |
|---|---|---|
| `string` | `domain_name(14)` |  The name of the domain.  |
| `ref string` | `child_domains(14, 32)` |  This returns an array containing the names of the children of the specified domain. It can contain the names of up to 32 children.  |

## Return values
The number of filled children.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
