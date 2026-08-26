# qss.search()

## Syntax:
`function long qss.search( long flag, void search, const void array, const long def(,), [ long dept ] )`

## Description
This searches a specified array for a particular value, which is referred to as the search key. By default, it reads the array sequentially until it finds the specified value (that is, it performs a linear search). To perform a binary search instead, you must first sort the data, for example with [qss.sort()](qss.sort.md) and then call *qss.search()* with the *flag* argument set to QSS.SRC.IS.SORTED. If the same search key occurs more than once, then you should also specify the QSS.SRC.DUPL.ALLOWED option, or else it is not predictable which one of the duplicate records is found.

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
| `long` | `flag` |  This specifies which array element is to be retrieved and the type of search to be performed. You can set the argument to one of the following possible values:  |
| `void` | `search` |  The value that you want to search for in the specified array. This is the search key.  |
| `const void` | `array` |  This specifies the array that must be searched. It can be a string or an array of type string, long, or double, but it is usually an array of strings.  |
| `const long` | `def(,)` |  This indicates how the system is to search the array and against what conditions it must test the elements of the array. The argument must be declared as follows: long def(x,4) | x is the number of search fields You can define several search fields (1 to *x*). For each search field, you define the four search properties by using the following functions. In each case, the *field_number* argument specifies the sequence number (1 to *x*) of the search field.  |
| `[ long` | `dept ]` |  This indicates the number of array elements (starting with the first element) that must be searched if the function is not intended to search the entire array. By default, the function searches the entire array until it finds the required value. In that case, if the QSS.SRC.IS.SORTED option is specified then the *entire* array must previously have been sorted.  |

## Return values
| | |
|---|---|
| > 0 | index in the array where the search key was found |
| -1 | error; *search* argument not found  |
| -11 | *search* argument must be of same type as array; *def* is not of type long array or *array* not of type array  |
| -12 | *search* argument not correct; string not expected  |
| -13 | *dept* must be positive  |
| -14 | *def* argument not correctly declared  |
| -15 | *search* argument does not fit in declared array  |
| -16 | QSS.TYPE not correct |
| -17 | *array* argument not correct  |
| -18 | no definition found in *def* |
| -21 | flag LOOKUP.FOR.STRUCT is used; *search* argument must be a string  |
| -22 | *search* argument not correct; probably a size problem - size of search must match size of an element in array if LOOKUP.FOR.STRUCT is set or (if LOOKUP.FOR.STRUCT is not set) must be at least the sum of lengths of the key fields (set by qss.length())  |
| -23 | *search* argument not correct; probably a type problem  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Searching and sorting data overview and synopsis](overview_and_synopsis.md)
- [Table searching and sorting sample programs](example.md)
