# get.size.in.bytes()

## Syntax:
`function long get.size.in.bytes( void var )`

## Description
This function returns the number of bytes available for the specified variable.
NOTE: This function only works for non-array variables.

## Arguments
| | | |
|---|---|---|
| `void` | `var` |  The name of the variable.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2360.

## Return value
When *var* is a string, the number of bytes available for the caller is returned.
When *var* is a long or a double, the underlying size of the object is returned. For example, for a 64-bit long 8 is returned, for a 32-bit long 4.
When *var* is an array, -1 is returned.
When *var* is an empty based string, the value 0 is returned.

## Noteworthy
The only situation where this function yields (for non-array variables) a value different from that yielded by the function array.get.size.in.bytes(), is for multi language string variables.
The function get.size.in.bytes() returns the maximal size in bytes of a string in a single language, whereas the function array.get.size.in.bytes() returns the number of bytes used for a single element in an array of strings.

## Example
```

long    size	| in bytes

long    a.long
long    some.longs(3,5,7)

string	a.string(11)
string	based.string(1)        based
string	some.strings(3,5,7)
string	based.strings(1,1,1,1) based

size = get.size.in.bytes( a.long )		| size == BitCountOfLong / 8
size = get.size.in.bytes( some.longs )	| size == -1
size = get.size.in.bytes( some.longs(1,1,1) )	| size == BitCountOfLong / 8

size = get.size.in.bytes( a.string )		| size == 11

size = get.size.in.bytes( based.string )	| size == 0
alloc.mem( based.string, 17 )
size = get.size.in.bytes( based.string )	| size == 17
size = get.size.in.bytes( based.string(1) )	| size == 17

size = get.size.in.bytes( some.strings )		| size == -1
size = get.size.in.bytes( some.strings(1,1,1) )	| size == 3

size = get.size.in.bytes( based.strings )		| size == -1
alloc.mem( based.strings, 19, 3, 5, 7 )
size = get.size.in.bytes( based.strings )		| size == -1
size = get.size.in.bytes( based.strings(1,1,1,1) )	| size == 19
```

## Related topics
- [array.get.size.in.bytes()](array.get.size.in.bytes.md)

- [Memory operations overview and synopsis](overview_and_synopsis.md)
