# rnd.init()

## Syntax:
`function void rnd.init( long seed )`

## Description
[rnd.d()](rnd.d.md) and [rnd.i()](rnd.i.md) use a system-independent random number generator to generate random numbers. On all systems, the generator will generate the same random numbers, provided that the same seed is supplied.
*rnd.init()* resets the random number generator to the starting point specified by the *seed* argument (the seed can be any long value). If *rnd.init()* is not called before starting the generator, then the first results of *rnd.d()* and *rnd.i()* are undefined.

## Arguments
| | | |
|---|---|---|
| `long` | `seed` |    |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Random number generators overview and synopsis](overview_and_synopsis.md)
