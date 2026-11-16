# alloc.mem()

## Syntax:
`function long alloc.mem( ref variable, long dimension1, [ long dimension2,... ] )`

## Description
This allocates memory space to the specified variable at run time. The variable can be a string or an array (of any type). It must be declared as BASED. With multi-dimensional arrays, each dimension must be initialized to 1 at declaration. Once *alloc.mem()* has allocated memory for a variable, that variable behaves in the same way as any other variable.
*Behavior when TIV level of object is below 1700*
When you call *alloc.mem()* a second time for the same variable, information already present is retained, but the variable is reallocated to a different part of memory. This is relevant only if you want to increase or decrease the memory space assigned to an array. Because the contents of array elements are contiguous in memory, you can change only the number of elements in the array (the first index in the case of longs and doubles; the second index in the case of strings). Changing the size of array elements during reallocation causes loss of information.
*Behavior when TIV level of object is 1700 or higher*
When you call alloc.mem() a second time for the same variable, information already present is retained, but the variable may be reallocated to a different part of memory, if one of the dimensions is different from the first time. The information in the array is retained in such a way that when an item is available at a certain point (identified by a number of indices) in the old array, that item can be found at the same point in the new array, when the dimensions of the new array allow. All points in the new array that have no corresponding point in the old array will have a 0 or empty value.
For backward compatibility the function alloc.mem.deprecated() is available from TIV 1700. Regardless the object TIV the alloc.mem.deprecated() function behaves the same as alloc.mem() when the object TIV is less than 1700.

## Arguments
| | | |
|---|---|---|
| `ref` | `variable` |    |
| `long` | `dimension1` |    |
| `[ long` | `dimension2,... ]` |    |

## Return values
0 success
-1 insufficient memory available

## Context
This function is implemented in the porting set and can be used in all script types.
Note  Remember to use [free.mem()](free.mem.md) to deallocate memory space when it is no longer required.

## Example
```

long     i, j, k
string   c(1)     based
string   st(1,1)  based
double   d(1,1,1) based

alloc.mem(c, 10)        | Allocate a string with length 10
alloc.mem(st, 20, 5)    | Allocate 5 strings of length 20
alloc.mem(d, 2, 5, 6)   | Allocate an array of doubles with 3 dimensions
for i=1 to 2
        for j=1 to 5
                for k=1 to 6
                        d(i,j,k) = k*j
                endfor
        endfor
endfor

alloc.mem(d, 4, 5, 6)   | Reallocate array of doubles
alloc.mem(st, 20, 8)    | Reallocate 8 strings
```

## Example when object TIV is 1700 or higher
```

long array(1,1) based

alloc.mem(array, 2, 3 )

array(1,1) = 11
array(1,2) = 12
array(1,3) = 13
array(2,1) = 21
array(2,2) = 22
array(2,3) = 23

alloc.mem( array, 3, 2 )

| The array will have the following contents:
| array(1,1) = 11
| array(1,2) = 12
| array(2,1) = 21
| array(2,2) = 22
| array(3,1) = 0
| array(3,2) = 0
```

## Related topics
- [Memory operations overview and synopsis](overview_and_synopsis.md)
