# qss.search()

## Syntax:
`function long qss.search( long flag, void search, const void array, const long def(,), [ long dept ] )`

## Description
This searches a specified array for a particular value, which is referred to as the search key. By default, it reads the array sequentially until it finds the specified value (that is, it performs a linear search). To perform a binary search instead, you must first sort the data, for example with [qss.sort()](qss.sort.md) and then call *qss.search()* with the *flag* argument set to QSS.SRC.IS.SORTED. If the same search key occurs more than once, then you should also specify the QSS.SRC.DUPL.ALLOWED option, or else it is not predictable which one of the duplicate records is found.

## Arguments
| | |
|---|---|
| QSS.FIRST | Find the first record in the array; the *search* argument is ignored. |
| QSS.LAST | Find the last record in the array; the *search* argument is ignored. |
| QSS.GT | Find the first record greater than the search key. |
| QSS.GTEQ | Find the first record greater than or equal to the search key. |
| QSS.LESS | Find the first record less than the search key. |
| QSS.EQLE | Find the first record less than or equal to the search key. |
| QSS.EQUAL | Find the first record equal to the search key. |
| QSS.NE | Find the first record not equal to the search key. |
You can combine each of these options with one or more of the following options:
| | |
|---|---|
| QSS.SRC.IS.SORTED | Specifies that the array is sorted according to the specifications in the *def* argument, for example by using the [qss.sort()](qss.sort.md) function. The search will be performed using a binary search. |
| QSS.LOOKUP.FOR.STRUCT | When this flag is set, the function searches the array for a specified record pattern – that is, it searches for an array element that matches both the structure and value of the search key. The search argument must have the same layout and length as the elements in array. When this flag is not set, the search argument is constructed as the concatenation of the key fields defined by the def argument (see Example 2). |
| QSS.SRC.DUPL.ALLOWED | Specifies that the search key can occur more than once in the source array. Note that when multiple records match the search key, then the index of the *first* matching record (in effect the one with the *lowest* index) is returned. |
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
| | |
|---|---|
|  | This indicates the search field's start position in the array element. For example, this allows you to search a string array for a character combination starting at the fourth character of the array element. |
|  | This defines how this search field is compared. See the corresponding sort field comparison values for [qss.sort()](qss.sort.md) |
|  | This specifies the search field's type. See the corresponding sort field type values for [qss.sort()](qss.sort.md) |
|  | This specifies the length of the search field. This option is valid only when the search field type is a string type. |
If you define fewer search fields than you have declared, you must close the *def* argument by calling *qss.start()* with a start position of zero. For example, if you have declared three search fields, as follows: def(3,4) but then create only two search fields, you must close the definition with the following call:qss.start(def,3,0)

## Return values
| | |
|---|---|
| > 0 | index in the array where the search key was found |
| -1 | error; *search* argument not found |
| -11 | *search* argument must be of same type as array; *def* is not of type long array or *array* not of type array |
| -12 | *search* argument not correct; string not expected |
| -13 | *dept* must be positive |
| -14 | *def* argument not correctly declared |
| -15 | *search* argument does not fit in declared array |
| -16 | QSS.TYPE not correct |
| -17 | *array* argument not correct |
| -18 | no definition found in *def* |
| -21 | flag LOOKUP.FOR.STRUCT is used; *search* argument must be a string |
| -22 | *search* argument not correct; probably a size problem - size of search must match size of an element in array if LOOKUP.FOR.STRUCT is set or (if LOOKUP.FOR.STRUCT is not set) must be at least the sum of lengths of the key fields (set by qss.length()) |
| -23 | *search* argument not correct; probably a type problem |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Searching and sorting data overview and synopsis](overview_and_synopsis.md)

- [Table searching and sorting sample programs](example.md)
