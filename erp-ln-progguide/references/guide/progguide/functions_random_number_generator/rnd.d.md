# rnd.d()

## Syntax:
`function double rnd.d( )`

## Description
This function uses a system-independent random number generator. On all systems, the generator will generate the same random numbers, provided that the same seed is supplied.
Calls to *rnd.d()* return successive random numbers in the range 0.0 to 1.0. Use [rnd.init()](rnd.init.md) to specify a seed value before starting the random number generator. If you do not do this, the first result of *rnd.d()* is undefined.

## Return values
A random number in the range 0.0 to 1.0.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Random number generators overview and synopsis](overview_and_synopsis.md)
