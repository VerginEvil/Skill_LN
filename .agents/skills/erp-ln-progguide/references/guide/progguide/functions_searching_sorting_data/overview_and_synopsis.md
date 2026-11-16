# Searching and sorting data overview and synopsis

## Overview
Use these functions for searching and sorting data. Use *qss.search()* to search the data for a particular value. Use *qss.sort()* to sort the data. The data can be a string or an array of type string, long, or double.
The *qss.search()* function can perform either a linear or a binary search. A binary search is faster than a linear search, but the data must first be sorted by *qss.sort()*. In practice, therefore, a binary search is efficient only when the data does not often change and so does not require repeated sorting. If the data is frequently modified, use a linear search on unsorted data instead; this avoids frequent calls to *qss.sort()*.

## Synopsis
```

long
```
```

long
```
| | | |
|---|---|---|
|  | [qss.search](qss.search.md) | `( long flag, void search, const void array, const long def(,) [, long dept] )` |
|  | [qss.sort](qss.sort.md) | `( ref void array, const long def(,) [, long dept] )` |

## Related topics
- [Table searching and sorting sample programs](example.md)
