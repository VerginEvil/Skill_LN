# str.isnumeric()

## Syntax:
`function boolean str.isnumeric( const string string$ )`

## Description
Returns true if the given string contains only characters in the range 0-9.
Note that [isdigit()](isdigit.md) treats a string prefixed with a minus sign, like "-10", as a digit, but this function does not.

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |

## Return values
*true* if the string contains only characters in the range 0-9, else *false*

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Example
```

boolean	result

result = str.isnumeric("123")
|* result = true

result = str.isnumeric("123A")
|* result = false
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
- [str.isalpha()](str.isalpha.md)
- [str.isalphanum()](str.isalphanum.md)
- [isdigit()](isdigit.md)
