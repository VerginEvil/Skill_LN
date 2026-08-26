# str.endswith()

## Syntax:
`function boolean str.endswith( const string string$, const string part$, [ boolean ignorecase ] )`

## Description
Determines whether the end of the specified string matches the specified part. Optionally the test can be done case insensitive.

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |
| `const string` | `part$` |  another string  |
| `[ boolean` | `ignorecase ]` |  when `true` is specified the comparison is done case-insensitive; when this argument is not specified the comparison is case sensitive  |

## Return values
| | |
|---|---|
| true | the specified part matches the end of the specified string or is empty |
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

ret = str.endswith(source, "dog")
| ret now equals true

ret = str.endswith(source, "cat")
| ret now equals false

ret = str.endswith(source, "")
| ret now equals true

ret = str.endswith(source, "DOG")
| ret now equals false

ret = str.endswith(source, "DOG", true) | case insensitive
| ret now equals true

string file(100)

file = "c:\data\picture.GIF"
ret = str.endswith(file, ".gif", true)
| ret = true
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
