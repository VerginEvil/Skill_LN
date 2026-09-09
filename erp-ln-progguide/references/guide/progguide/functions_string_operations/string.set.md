# string.set$()

## Syntax:
`function string string.set$( string value$, long count )`

## Description
This function returns a string containing the concatenation of *count* copies of *value$*.

## Arguments
| | | |
|---|---|---|
| `string` | `value$` |    |
| `long` | `count` |    |

## Return values
A string containing the concatenation of *count* copies of *value$*.

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

string st(80)
st = string.set$("-", 10)          | st contains "----------"
st = string.set$( string.set$("-",3)&"+", 3 )
                                   | st contains "---+---+---+"
st = string.set$( chr(135), 5 )    | st contains 5 graphic symbols
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
