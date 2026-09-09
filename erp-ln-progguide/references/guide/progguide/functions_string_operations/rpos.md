# rpos()

## Syntax:
`function long rpos( string source, string part, [ long offset ] )`

## Description
This returns the start position of a specified substring ( *part*) in a specified string ( *source*). *source* and *part* can be either strings or string expressions.
*rpos()* starts searching for the substring at the last position in the source string, searching backward. It returns the start position relative to the beginning of the source string. To start searching at the first position instead, use [pos()](pos.md).
As of [TIV 1700](../tiv/tiv_1700.md), *rpos()* can start the search at the specified *offset*. In this way it is possible to not only find the first occurrence of a substring, but also the next one(s). The returned start position is also in this case relative to the beginning of the source string. See the example below for how to use this optional parameter. The string effectively searched in is a substring from *source*, ending at *offset*.
As of [TIV 2200](../tiv/tiv_2200.md), an alternative to this function exists ( [str_rpos()](str_rpos.md)), which finds the same parts in the source string as *rpos()* does, but always returns a start position in the source which can be used as offset in the source string. For more information see [str_rpos()](str_rpos.md).

## Arguments
| | | |
|---|---|---|
| `string` | `source` |  The string to search in  |
| `string` | `part` |  The part to search  |
| `[ long` | `offset ]` |  Optional search starting position; when not specified the search starts at the end of the source string. Note that: If `offset < 1`, then 0 is returned. If `offset > len(source)`, then searching start at the end of the source string (position `len(source)`). This parameter can be used as of [TIV 1700](../tiv/tiv_1700.md).  |

## Return values
The start position of the substring in the string. Or 0 if the substring is not found.

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long index
string source(50)
string part(10)
long part_len

|                  1         2         3         4
| index   1234567890123456789012345678901234567890123
source = "the quick brown fox jumps over the lazy dog"

index = rpos(source, "the")    | index contains 32
index = pos(source, "the")     | index contains 1

index = rpos(source, "fox")     | index contains 17

| Optional offset parameter (as of TIV 1700)
index = rpos(source, "the", -1) | index contains 0
index = rpos(source, "the", 1)  | index contains 0
index = rpos(source, "the", 10) | index contains 1
index = rpos(source, "the", 50) | index contains 32

| Now find all occurrences in a repetitive string using a loop
source   = "ababababa"
part     = "aba"	| can be found at offsets 1, 3, 5 an 7 in source
part_len = len(part)

| Find all non-overlapping occurrences
index = rpos( source, part )
while index > 0
	| do something with this index
	...
	| get the next "aba"
	index = rpos( source, part, index - 1 )
endwhile
| the following offsets have been found in this order: 7 and 3

| Find all overlapping occurrences
index = rpos( source, part )
while index > 0
	| do something with this index
	...
	| get the next "aba"
	index = rpos( source, part, index + part_len - 2 )
endwhile
| the following offsets have been found in this order: 7, 5, 3 and 1
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)

- [pos()](pos.md)

- [str_pos()](str_pos.md)

- [str_rpos()](str_rpos.md)
