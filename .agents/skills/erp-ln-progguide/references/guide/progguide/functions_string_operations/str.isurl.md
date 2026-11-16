# str.isurl()

## Syntax:
`function boolean str.isurl( const string string$ )`

## Description
Returns true if the given string is a valid URL in the form:
```

scheme://host[:port][/path][?query]
```
The port, if provided, must be in the range 1-65535.

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |

## Return values
*true* if the string is a valid URL, else *false*

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Example
```

boolean	result

result = str.isurl("https://www.infor.com:443/pages/default.html?search=LN")
|* result = true

result = str.isurl("https://www.infor.com:443345/pages/default.html?search=LN")
|* result = false

result = str.isurl("//example.com/page/1")
|* result = false
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
