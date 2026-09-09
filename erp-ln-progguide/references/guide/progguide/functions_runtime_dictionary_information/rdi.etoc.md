# rdi.etoc$()

## Syntax:
`function string rdi.etoc$( string domain_name(14), long enum_value as long )`

## Description
This gets an enum-value as long and returns a string representing it in the specified domain.

## Arguments
| | | |
|---|---|---|
| `string` | `domain_name(14)` |  The name of the domain.  |
| `long` | `enum_value as long` |  An enum-value in the specified domain.  |

## Return values
filled string, success
empty string, error occurred

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
Domain: tcynna
| | | |
|---|---|---|
| `Constant` | `Constant Name` |  `Description`  |
| `1` | `yes` |  `Yes`  |
| `2` | `no` |  `No`  |
| `3` | `not.app` |  `Not Applicable`  |
```

string  enum_name(15)

enum_name = rdi.etoc$("tcynna", 3)

The value of enum_name is now: not.app
```

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
