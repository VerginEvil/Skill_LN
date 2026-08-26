# str_rpos()

## Syntax:
`function long str_rpos( string source, string part, [ long offset ] )`

## Description
This returns the start position of a specified substring ( *part*) in a specified string ( *source*). *source* and *part* can be either strings or string expressions.
As of [TIV 2200](../tiv/tiv_2200.md), this alternative function to [rpos()](rpos.md) exists which finds the same parts in the source string as *rpos()* does, but always returns a start position in the source which can be used as offset in the source string.
For examples of callling this function, see [rpos()](rpos.md).
When a multibyte part is found in a single-byte source, the start position yielded by the function rpos() is given as if the source was a multibyte string. When more multibyte characters were present in the source, this start position may be different from the start position of the found part in the source, when the source is viewed as single-byte (which it is, in this case). The function str_rpos() yields the start position in the same mode as the source string.
*str_rpos()* starts searching for the substring at the last position in the source string, searching backward. It returns the start position relative to the beginning of the source string. To start searching at the first position instead, use [str_pos()](str_pos.md).
*str_rpos()* can start the search at the specified *offset*. In this way it is possible to not only find the first occurrence of a substring, but also the next one(s). The returned start position is also in this case relative to the beginning of the source string.

## Arguments
| | | |
|---|---|---|
| `string` | `source` |  The string to search in.  |
| `string` | `part` |  The part to search.  |
| `[ long` | `offset ]` |  Optional search starting position; when not specified the search starts at the end of the source string. Note that: If `offset < 1`, then 0 is returned. If `offset > len(source)`, then searching start at the end of the source string (position `len(source)`).  |
-
-

## Return values
The start position of the substring in the string. Or 0 if the substring is not found.

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2200.

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
- [str_pos()](str_pos.md)
- [pos()](pos.md)
- [rpos()](rpos.md)
