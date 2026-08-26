# str.substring$()

## Syntax:
`function string str.substring$( const string string$, long beginpos, [ long endpos ] )`

## Description
Returns a substring from the specified string. The substring starts at the specified begin position. When an end position is specified, the substring extends to the character at position `endpos - 1`.
Note that when using the `var(x;y)` construction, the `y` is the size of the substring, but when calling `str.substring$(var, x, y)`, the `y` is the end position in `var`. See the example code below to see the difference.

## Arguments
-
-
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |
| `long` | `beginpos` |  the begin position, inclusive; note that: if `beginpos <= 0`, then `beginpos` is set to 1 if `beginpos > len(string$)`, then an empty string is returned  |
| `[ long` | `endpos ]` |  optional, the end position, exclusive; note that: if `endpos <= beginpos`, then an empty string is returned if `endpos > len(string$)`, then `endpos` is not taken into account  |
-
-

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

string source(50)
string substr(50)
long p1, p2

|                  1         2         3         4         5
| pos     12345678901234567890123456789012345678901234567890
source = "the quick brown fox jumps over the lazy dog"

substr = str.substring$(source, 41)
| substr now contains "dog"

substr = str.substring$(source, 5, 10)
| substr now contains "quick" and contains 5 chars

| see the difference with the sub string operator (;)
substr = source(5;10)
| substr now contains "quick brow" and contains 10 chars

substr = str.substring$(source, -1, 4)
| substr now contains "the"

substr = str.substring$(source, 36, 50)
| substr now contains "lazy dog"

substr = str.substring$(source, 1, 1)
| substr now contains ""

substr = str.substring$(source, 50)
| substr now contains ""

|                  1         2         3         4         5
| pos     12345678901234567890123456789012345678901234567890
source = "Once upon a time, there was a ..."
p1 = pos(source, "time")
| p1 equals 13
p2 = pos(source, ",")
| p2 equals 17
substr = str.substring$(source, p1, p2)
| substr now contains "time"
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
