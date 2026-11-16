# array.info()

## Syntax:
`function void array.info( void var, ref long nr.dims, ref long dim.info(), [ ref long declared.length ] )`

## Description
This function returns the number of dimensions in a specified array variable and the size of each dimension.

## Arguments
| | | |
|---|---|---|
| `void` | `var` |  Any variable, typically (but not restricted to) an array variable.  |
| `ref long` | `nr.dims` |  Reference parameter which receives the number of dimensions of *var*. If *var* is a non-array variable, then *nr.dims* returns 0. If *var* is a string variable, then *nr.dims* returns 1. If *var* is an array variable, then the value returned by *nr.dims* is at least 1 and at most 4.  |
| `ref long` | `dim.info()` |  Reference array parameter which receives the sizes of the dimensions of *var*. The number of elements of *dim.info* must not be less than the value returned by *nr.dims* The first *nr.dims* elements of *dim.info* are filled with the size of the corresponding dimension of *var*. Any further elements of *dim.info* (but not further than dim.info(4)) are set to value 0.  |
| `[ ref long` | `declared.length ]` |  Reference parameter which receives the declared length of *var*. This optional parameter is available as of [bshell TIV](../tiv/tiv_overview.md) [level 2340](../tiv/tiv_2340.md). If *var* is a string variable (be it an explicitly named variable or an anonymous temporary variable containing some intermediate result), then *declared.length* receives the declared length of *var*. If *var* is a string array variable, (be it an explicitly named variable or an anonymous temporary variable containing some intermediate result), then *declared.length* receives the declared length of the individual strings in the string array, i.e. the declared first (least significant) dimension of the string array. In all other cases, *declared.length* is set to 0.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long    a3(3,5,7)
string  s3(3,5,7)
string  mbs3(3,5,7) mb
long    nr.dims
long    dim.info(4)
long    declared.length
string  b4(1,1,1,1) based

array.info( a3, nr.dims, dim.info )
        | Returns:
        |  nr.dims = 3
        |  dim.info(1) = 3
        |  dim.info(2) = 5
        |  dim.info(3) = 7

array.info( s3, nr.dims, dim.info, declared.length )
        | Returns:
        |  nr.dims = 3
        |  dim.info(1) = 3
        |  dim.info(2) = 5
        |  dim.info(3) = 7
        |  declared.length = 3

array.info( mbs3, nr.dims, dim.info, declared.length )
        | Returns:
        |  nr.dims = 3
        |  dim.info(1) = 3 * internal mb factor
        |  dim.info(2) = 5
        |  dim.info(3) = 7
        |  declared.length = 3

array.info( b4, nr.dims, dim.info )
        | Returns:
        |  nr_dims = 4
        |  dim.info(1) = 0
        |  dim.info(2) = 0
        |  dim.info(3) = 0
        |  dim.info(4) = 0
```

## Related topics
- [Memory operations overview and synopsis](overview_and_synopsis.md)
