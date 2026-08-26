# str.isbase64()

## Syntax:
`function boolean str.isbase64( const string string$ )`

## Description
Returns true if the given string is a valid base64 encoded string.
According to RFC 4648:
- a base64 encoded string has a length which is a multiple of 4;
- only characters in the range a-zA-Z0-9+/= are allowed;
- the '=' is only used for padding;
- if padding is required the string ends with either 1 or 2 '=' characters;
- an empty string is a valid base64 encoded string.

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |

## Return values
*true* if the string is a valid base64 encoded string, else *false*

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Example
```

boolean	result

result = str.isbase64("QQ==")	|* the letter A
|* result = true

result = str.isbase64("QQ=")	|* missing equals (=) sign
|* result = false
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
