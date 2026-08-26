# shiftc$()

## Syntax:
`function string shiftc$( string str )`

## Description
This centers the specified string by equaling the number of leading and trailing spaces. If there is an odd number of spaces, the extra space becomes a trailing space. The returned string always has the same length as the input string.
See also [shiftl$()](shiftl.md) and [shiftr$()](shiftr.md).

## Arguments
| | | |
|---|---|---|
| `string` | `str` |  |

## Context
This function is implemented in the porting set and can be used in all script types.
Note  This function does not change the input string.
This function does not work on multibyte strings.

## Example
```

shiftc$("  ABC      ")     | result  "    ABC    "
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
