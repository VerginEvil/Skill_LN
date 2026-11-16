# str.startswith()

## Syntax:
`function boolean str.startswith( const string string$, const string part$, [ boolean ignorecase ] )`

## Description
Determines whether the beginning of the specified string matches the specified part. Optionally the test can be done case insensitive.

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |
| `const string` | `part$` |  another string  |
| `[ boolean` | `ignorecase ]` |  when `true` is specified the comparison is done case-insensitive; when this argument is not specified the comparison is case sensitive  |

## Return values
| | |
|---|---|
| true | the specified part matches the beginning of the specified string or is empty |
| false | in any other case |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

string source(50)
boolean ret

|                  1         2         3         4         5
| pos     12345678901234567890123456789012345678901234567890
source = "the quick brown fox jumps over the lazy dog"

ret = str.startswith(source, "the")
| ret now equals true

ret = str.startswith(source, "a")
| ret now equals false

ret = str.startswith(source, "")
| ret now equals true

ret = str.startswith(source, "THE")
| ret now equals false

ret = str.startswith(source, "THE", true) | case insensitive
| ret now equals true

string file(100)

file = "c:\data\picture.gif"
ret = str.startswith(file, "C:\", true)
| ret = true
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
