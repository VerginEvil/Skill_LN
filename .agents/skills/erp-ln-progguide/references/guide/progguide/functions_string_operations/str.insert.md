# str.insert$()

## Syntax:
`function string str.insert$( const string string$, long offset, const string part$ )`

## Description
Returns a copy of a string having a specified part inserted at a specified character position.

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |
| `long` | `offset` |  the character position of the insertion; note that: if `offset <= 1`, then `part$` prepended if `offset > len(string$)`, then `part$` appended  |
| `const string` | `part$` |  the string to insert at the specified offset  |

## Return values
A string equivalent to the specified string but with the specified part inserted at the specified offset

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

string source(50)
string target(100)

|                  1         2         3         4         5
| pos     12345678901234567890123456789012345678901234567890
source = "the quick brown fox jumps over the lazy dog"

target = str.insert$(source, 27, "two times ")
| target now contains "the quick brown fox jumps two times over the lazy dog"

target = str.insert$(source, -1, "oh oh, ")
| target now contains "oh oh, the quick brown fox jumps over the lazy dog"

target = str.insert$(source, 1, "ah, ")
| target now contains "ah, the quick brown fox jumps over the lazy dog"

target = str.insert$(source, 44, "?")
| target now contains "the quick brown fox jumps over the lazy dog?"

target = str.insert$(source, 9999, "!")
| target now contains "the quick brown fox jumps over the lazy dog!"
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
