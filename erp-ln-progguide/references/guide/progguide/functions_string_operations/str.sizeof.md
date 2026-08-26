# str.sizeof()

## Syntax:
`function long str.sizeof( const string string$ )`

## Description
Returns the size of the specified string, i.e. the number of bytes the string can contain.

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |

## Return values
the number of bytes the specified string can contain; or zero in case the string is not allocated.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

string source(50)
string other(1) based
long size

|                  1         2         3         4         5
| pos     12345678901234567890123456789012345678901234567890
source = "the quick brown fox jumps over the lazy dog"

size = str.sizeof(source)
| size equals 50 ( len(source) would return 43 )

size = str.sizeof(other)
| size equals 0 ( not allocated )

alloc.mem(other, 10)
size = str.sizeof(other)
| size equals 10

free.mem(other)

size = str.sizeof(other)
| size equals 0 again ( not allocated )
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
