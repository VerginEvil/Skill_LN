# str.remove$()

## Syntax:
`function string str.remove$( const string string$, long offset, long nchars )`

## Description
Returns a copy of a string having a number of characters deleted, beginning at a specified character position.

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |
| `long` | `offset` |  the character position to begin deleting characters; note that: if `offset < 1`, then nothing is removed if `offset > len(string$)`, then nothing is removed  |
| `long` | `nchars` |  the number of characters to remove; note that: if `nchars < 0`, then all characters starting at `offset` are removed if `nchars = 0`, then nothing is removed if `offset + nchars > len(string$)`, then all characters starting at `offset` are removed  |

## Return values
A string equivalent to the specified string less the specified number of characters

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

string source(50)
string target(50)

|                  1         2         3         4         5
| pos     12345678901234567890123456789012345678901234567890
source = "the quick brown fox jumps over the lazy dog"

target = str.remove$(source, 5, 6)
| "quick " is removed
| target now contains "the brown fox jumps over the lazy dog"

target = str.remove$(source, -1, 6)
| nothing is removed
| target now contains "the quick brown fox jumps over the lazy dog"

target = str.remove$(source, 50, 6)
| nothing is removed
| target now contains "the quick brown fox jumps over the lazy dog"

target = str.remove$(source, 10, 0)
| nothing is removed
| target now contains "the quick brown fox jumps over the lazy dog"

target = str.remove$(source, 26, -1)
| all after "jumps" is removed
| target now contains "the quick brown fox jumps"

target = str.remove$(source, 26, 100)
| all after "jumps" is removed
| target now contains "the quick brown fox jumps"
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
