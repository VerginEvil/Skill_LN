# cmp.mem()

## Syntax:
`function long cmp.mem( void var1, void var2, [ long count ] )`

## Description
This compares the values of two variables or arrays. By default, the values are compared for the length of the shortest argument. If you specify the optional *count* argument, the function compares the first *count* numbers or characters of both arguments. The number of numbers or characters compared will, however, never exceed the length of the shortest argument.
Note that when the shorter array equals the first part of the longer array, they will be considered equal.
A special situation occurs when two arrays of strings are compared. In this situation by default only the first string in the arrays is compared. To compare the complete arrays (limited by the length of the shortest array) specify the *count* argument, with a value exceeding the length of the larger array.

## Arguments
| | | |
|---|---|---|
| `void` | `var1` |  |
| `void` | `var2` |  |
| `[ long` | `count ]` |  |

## Return values
The return values depend on the types of the variables.
Variables are of different types:
1
Variables are longs or doubles:
0: values are equal
1: values are different
Variables are strings or arrays of type long, double, or string:
< 0: first argument is less than second
= 0: arguments are equal
> 0: first argument is greater than second

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long l_arr(2,2), lng_arr(3,5), ret
fill_long_arrays()
ret = cmp.mem( lng_arr, l_arr )  | The first 4 elements are checked
if ret = 0 then
        message( "values are equal" )
else
        if ret > 0 then
                message( "First array greater than second" )
        else
                message( "First array less than second" )
        endif
endif
```

## Related topics
- [Memory operations overview and synopsis](overview_and_synopsis.md)
