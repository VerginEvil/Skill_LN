# not.fixed()

## Syntax:
`function void not.fixed( string string_var )`

## Description
You can fill a string with or without specifying a start position. If you specify a start position, unused positions in the string are filled with spaces. You can prevent the string from being filled out with spaces by calling *not.fixed()* before filling the string. Note that, when you assign a new value to the string variable, positions after the new value are not changed.

## Arguments
| | | |
|---|---|---|
| `string` | `string_var` |  |

## Context
This function is implemented in the porting set and can be used in all script types.
Note  This function does not work with variables declared as FIXED.

## Example 1
```

string buf(10)

buf(5)    = "***"    | buf contains "    ***   "        (length = 10)
buf       = "***"    | buf contains "***"               (length = 3)
```

## Example 2
```

string buf(10)

not.fixed( buf )
buf(5)    = "***"    | buf contains "    ***"           (length = 7)
buf       = "***"    | buf contains "*** ***"           (length = 7)
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
