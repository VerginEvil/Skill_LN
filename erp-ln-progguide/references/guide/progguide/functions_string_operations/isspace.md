# isspace()

## Syntax:
`function boolean isspace( string str_expr )`

## Description
This tests whether the result of *string_expr* contains only spaces or is empty.

## Arguments
| | | |
|---|---|---|
| `string` | `str_expr` |  |

## Return values
TRUE string is empty or contains only spaces
FALSE string is not empty and contains characters other than spaces

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

string str1(20)

if ( not isspace(str1) ) then
                message( "'%s' is not empty", str1 )
endif
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
