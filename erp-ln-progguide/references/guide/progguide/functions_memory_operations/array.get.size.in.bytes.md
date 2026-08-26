# array.get.size.in.bytes()

## Syntax:
`function long array.get.size.in.bytes( void var )`

## Description
This function returns the number of bytes available for a specified array or string
NOTE: Despite the name, the function also works for non-array types of symbols, and will return the size in bytes such an object occupies when used as an element of an array.
NOTE: The number of elements in an array can be obtained by dividing the size of the array (in bytes) by the size of an element of the array (also in bytes). Another way to obtain this information is using [array.info()](array.info.md).

## Arguments
| | | |
|---|---|---|
| `void` | `var` |  The name of the array or string.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Return value
If *var* is an array or string, then the number of bytes available for it is returned.
If *var* is a long or a double, the underlying size of the object is returned. For example, for a 64-bit long 8 is returned, for a 32-bit long 4.
If *var* is not a valid symbol, or an empty based array, then the value 0 is returned.

## Example
```

long    a3(3,5,7)
string  s3(3,5,7)
long    size.in.bytes
string  b4(1,1,1,1) based
long    some.long

size.in.bytes = array.get.size.in.bytes( a3 )
        | Returns 3x5x7xBitCountOfLong/8

size.in.bytes = array.get.size.in.bytes( s3 )
        | Returns 3x5x7x1=105

size.in.bytes = array.get.size.in.bytes( b4 )
        | Returns 0

alloc.mem(b4, 2, 3, 5, 7)

size.in.bytes = array.get.size.in.bytes( b4 )
        | Returns 2*3*5*7=210

size.in.bytes = array.get.size.in.bytes( "abcde" )
        | Returns 5

size.in.bytes = array.get.size.in.bytes( some.long )
        | Returns 4xBitCountOfLong/8
```

## Related topics
- A similar function, which does not work for array types of symbols, and with a different result only for multi language string variables: [get.size.in.bytes()](get.size.in.bytes.md)
- [Memory operations overview and synopsis](overview_and_synopsis.md)
