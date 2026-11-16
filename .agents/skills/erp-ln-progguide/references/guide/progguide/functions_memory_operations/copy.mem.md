# copy.mem()

## Syntax:
`function void copy.mem( ref void destination, void source, [ long count ] )`

## Description
This copies the memory space from the *source* argument to the *destination* argument. By default, the total length of *source* is copied. But, if the *destination* argument is shorter than the *source* argument, then *source* is truncated. Use the optional *count* argument to copy a specified number of array elements only.
You can use this function to copy single variables or entire arrays. You cannot copy variables of different types. It you attempt to do this, the *destination* argument remains unchanged.

## Arguments
| | | |
|---|---|---|
| `ref void` | `destination` |    |
| `void` | `source` |    |
| `[ long` | `count ]` |  Optional argument for the specification of the number of array elements to be copied. Default value is the minimum of the element counts of the destination and source arguments.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long i,j
long src(5,5)
long des(3,3)
for i=1 to 5
        for j=1 to 5
                src(i,j)=i*j
        endfor
endfor
copy.mem(des,src)    | des contains the first 9 elements of src
```

## Related topics
- [Memory operations overview and synopsis](overview_and_synopsis.md)
