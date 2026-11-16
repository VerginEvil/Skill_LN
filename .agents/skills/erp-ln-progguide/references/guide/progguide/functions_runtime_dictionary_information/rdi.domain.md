# rdi.domain()

## Syntax:
`function long rdi.domain( string domain_name(14), ref string oformat(.), ref string lechar(.), ref string ilchar(.), ref long adjust, ref string errmess(.), ref long range_expr_id, [ ref long plen, ref string iformat(.) ] )`

## Description
This returns information about a specified domain.

## Arguments
| | | |
|---|---|---|
| `string` | `domain_name(14)` |  The name of the domain for which you want to retrieve information.  |
| `ref string` | `oformat(.)` |  This returns the output format of the domain.  |
| `ref string` | `lechar(.)` |  This returns the legal characters for the domain.  |
| `ref string` | `ilchar(.)` |  This returns the illegal characters for the domain.  |
| `ref long` | `adjust` |  This returns the domain's alignment mode. Possible values are: RDI.NONE RDI.LEFT RDI.RIGHT RDI.CENTER  |
| `ref string` | `errmess(.)` |  This returns the domain's error message.  |
| `ref long` | `range_expr_id` |  This returns the ID of the compiled expression for the range check.  |
| `[ ref long` | `plen ]` |  This returns the maximum field length (in display width) used on forms and reports.  |
| `[ ref string` | `iformat(.) ]` |  This returns the domain's internal format.  |

## Return values
The function returns the domain type, or -1 if an errors occurs. The possible domain types are:
| | | |
|---|---|---|
| DB.BYTE | DB.DOUBLE | DB.ENUM |
| DB.INTEGER | DB.STRING | DB.BITSET |
| DB.LONG | DB.DATE | DB.COMBINED |
| DB.FLOAT | DB.TEXT | DB.MULTIBYTE |
| DB.TIME | DB.RAW |  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
