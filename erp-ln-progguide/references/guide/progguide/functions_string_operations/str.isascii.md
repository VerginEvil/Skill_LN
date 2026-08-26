# str.isascii()

## Syntax:
`function boolean str.isascii( const string string$ )`

## Description
Returns true if the given string contains only ASCII characters. These are characters in the range 0x01-0x7f (1-127).
Note that 0x00 in the middle of a string cannot be checked, as this is the string terminator character, but an empty string ("") is treated as containing a (single) 0x00 ASCII character.

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |

## Return values
*true* if the string contains only characters in the ASCII range, else *false*

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Example
```

boolean	result

result = str.isascii("abcDEF@-&2034")
|* result = true

result = str.isascii("abc123" & chr$(140))
|* result = false
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
