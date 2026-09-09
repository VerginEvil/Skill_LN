# rdi.domain.set.value()

## Syntax:
`function long rdi.domain.set.value( string domain_name(14), long enum_item, string language, ref string keyword(.), string descr(.), ref long value )`

## Description
This returns information about a specified item in a set-type domain.

## Arguments
| | | |
|---|---|---|
| `string` | `domain_name(14)` |  The name of the domain.  |
| `long` | `enum_item` |  The numeric code of the set item for which you want to retrieve information.  |
| `string` | `language` |  The language code for the set domain.  |
| `ref string` | `keyword(.)` |  This returns the name of the specified set item.  |
| `string` | `descr(.)` |  This returns the description of the specified set item.  |
| `ref long` | `value` |  This returns the value of the specified set item.  |

## Return values
0 success
-1 error

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
