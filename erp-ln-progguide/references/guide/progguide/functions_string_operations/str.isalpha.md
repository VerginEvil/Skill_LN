# str.isalpha()

## Syntax:
`function boolean str.isalpha( const string string$ )`

## Description
Returns true if the given string contains only characters in the range a-zA-Z.

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |

## Return values
*true* if the string contains only characters in the range a-zA-Z, else *false*

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Example
```

boolean	result

result = str.isalpha("abcDEF")
|* result = true

result = str.isalpha("abc123")
|* result = false
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
- [str.isalphanum()](str.isalphanum.md)
- [str.isnumeric()](str.isnumeric.md)
