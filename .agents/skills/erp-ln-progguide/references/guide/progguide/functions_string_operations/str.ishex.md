# str.ishex()

## Syntax:
`function boolean str.ishex( const string string$ )`

## Description
Returns true if the given string is a valid hex encoded string. A hex encoded string has a length which is a multiple of 2. An empty string is considered a valid hex encoded string.

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |

## Return values
*true* if the string is a valid hex encoded string, else *false*

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Example
```

boolean	result

result = str.ishex("FadeBeef")
|* result = true

result = str.ishex("013DZY")
|* result = false
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
