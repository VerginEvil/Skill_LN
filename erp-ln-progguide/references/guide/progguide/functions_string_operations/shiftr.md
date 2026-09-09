# shiftr$()

## Syntax:
`function string shiftr$( string str )`

## Description
This function moves the contents of the specified string to the right, if there are trailing spaces. The length of the result is always the same as the length of the input string (this is not necessarily the declaration length).
See also [shiftl$()](shiftl.md) and [shiftc$()](shiftc.md).

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

shiftr$("    ABC    ")     | result  "        ABC"
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
