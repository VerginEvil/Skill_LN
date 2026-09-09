# shiftl$()

## Syntax:
`function string shiftl$( string str )`

## Description
This function returns the specified string with any leading spaces removed.
See also [shiftc$()](shiftc.md) and [shiftr$()](shiftr.md).

## Arguments
| | | |
|---|---|---|
| `string` | `str` |    |

## Context
This function is implemented in the porting set and can be used in all script types.
Note  This function does not change the input string.
This function does not work on multibyte strings.

## Example
```

shiftl$("    ABC    ")     | result  "ABC    "
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
