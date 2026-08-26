# qss.sort()

## Syntax:
`function long qss.sort( ref void array, const long def(,), [ long dept ] )`

## Description
This function performs a fast sort of a specified array.
Note that the order in the result array of two elements that compare identical is unpredictable.

## Arguments
```
void  qss.start(
   ref long def,
   long     field_number,
   long     position
)
```
```
void qss.way(
   ref long def,
   long     field_number,
   long     way
)
```
```
void qss.type(
   ref long def,
   long     field_number,
   long     type
)
```
```
void qss.length(
   ref long def,
   long     field_number,
   long     length
)
```
****
| | | |
|---|---|---|
| `ref void` | `array` |  The name of the array to be sorted.  |
| `const long` | `def(,)` |  This determines how the array is to be sorted. The argument must be declared as follows: long def(x,4) | x is the number of sort fields You can define several sort fields (1 to *x*). When performing a sort, the system sorts on the first sort field. Then, if there are duplicate values in the first sort field, the system sorts on the second sort field, and so on. For each sort field, you define the four sort properties by using the following functions. In each case, the *field_number* argument specifies the sequence number (1 to *x*) of the sort field.  |
| `[ long` | `dept ]` |  This indicates the number of array elements to be sorted if the function is not intended to sort the entire array. By default, the function sorts the entire array.  |

## Return values
| | |
|---|---|
| 0 | success |
| -1 | error, *array* and/or *def* is empty  |
| -11 | *def* is not of type long array or *array* not of type array  |
| -12 | *array* of strings must have > 1 dimension  |
| -13 | *dept* must be positive  |
| -14 | *def* argument not correctly declared  |
| -15 | *def* size exceeds *array* size  |
| -16 | QSS.TYPE not correct |
| -17 | *array* argument not correct  |
| -18 | no definition found in *def* |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Searching and sorting data overview and synopsis](overview_and_synopsis.md)
- [Table searching and sorting sample programs](example.md)
