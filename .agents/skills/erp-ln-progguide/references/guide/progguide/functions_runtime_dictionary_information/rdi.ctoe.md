# rdi.ctoe()

## Syntax:
`function long rdi.ctoe( string domain_name(14), string enum_name )`

## Description
This gets an enum as string and returns the enum-value as long belonging to it in the specified domain.

## Arguments
| | | |
|---|---|---|
| `string` | `domain_name(14)` |  The name of the domain.  |
| `string` | `enum_name` |  A string representing an enum-value in the domain.  |

## Return values
Enum-value as long on success
-1 Domain name hasn't been found
-2 Incorrect domain information found
-3 Enum-name not found in domain

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

domain tcynna	enum_val

enum_val = ltoe( rdi.ctoe( "ttaad.yeno", "not.app" ))

The value of enum_val is now: 3
```

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
