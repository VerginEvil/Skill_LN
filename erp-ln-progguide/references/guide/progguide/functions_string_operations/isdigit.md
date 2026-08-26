# isdigit()

## Syntax:
`function boolean isdigit( string str_expr )`

## Description
This function tests whether the supplied string is the textual representation of an integer value.

## Arguments
| | | |
|---|---|---|
| `string` | `str_expr` |  |

## Return values
TRUE string contains the textual representation of an integer value
FALSE string does not contain the textual representation of an integer value

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

string str1(20)

if ( not isdigit(str1) ) then
message( "'%s' is not a number", str1 )
endif
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
