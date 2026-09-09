# rnd.i()

## Syntax:
`function long rnd.i( [ long range ] )`

## Description
This function uses a system-independent random number generator. On all systems, the generator will generate the same random numbers, provided that the same seed is supplied.
Calls to *rnd.i()* return successive random numbers in the range 0 to 32767. You can specify a *range* argument if you want to limit the range further. The function then returns numbers in the range 0 to *range-* 1.
Use [rnd.init()](rnd.init.md) to specify a seed value before starting the random number generator. If you do not do this, the first result of *rnd.i()* is undefined.

## Arguments
| | | |
|---|---|---|
| `[ long` | `range ]` |    |

## Return values
A random number in the default or specified range.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Random number generators overview and synopsis](overview_and_synopsis.md)
