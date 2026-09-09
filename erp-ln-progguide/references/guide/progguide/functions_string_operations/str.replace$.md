# str.replace$()

## Syntax:
`function string str.replace$( const string string$, const string oldstr$, const string newstr$ )`

## Description
Returns a (null terminated) copy of `string$` that will have all instances of `oldstr$` replaced with `newstr$`.
As this function returns a string value that can become larger than the input string, you have to use a variable that is large enough to store the result.

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |
| `const string` | `oldstr$` |  the part to replace  |
| `const string` | `newstr$` |  the part to replace `oldstr$` with  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Preconditions
Note: The following preconditions no longer apply when `get.tools.tiv()` returns 2210 or higher.

- In case one of the variables passed to `string$`, `oldstr$`, or `newstr$` is declared as a multibyte string, then the variable passed to `result$` must be declared as a multibyte string as well.

## Example
```

string source(50)
string target(100)
string temp(10)

|                  1         2         3         4         5
| pos     12345678901234567890123456789012345678901234567890
source = "the quick brown fox jumps over the lazy dog"

target = str.replace$(source, "dog", "cat")
| target now contains "the quick brown fox jumps over the lazy cat"

target = str.replace$(source, "the", "a")
| target now contains "a quick brown fox jumps over a lazy cat"

target = str.replace$(source, "o", "O")
| target now contains "the quick brOwn fOx jumps Over the lazy dOg"

target = str.replace$(source, " ", "  ")
| target now contains "the  quick  brown  fox  jumps  over  the  lazy  dog"

target = str.replace$(source, "the", "")
| target now contains "quick brown fox jumps over lazy dog"

temp = str.replace$(source, "", "the")
| nothing replaced
| target now contains "the quick brown fox jumps over the lazy dog"

temp = str.replace$(source, "the", "")
| temp now contains "quick brow" as temp can contain only 10 chars
```

## Related topics
- [str.replace()](str.replace.md)

- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
