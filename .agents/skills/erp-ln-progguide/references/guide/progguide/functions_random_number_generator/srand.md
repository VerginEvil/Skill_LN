# srand()

## Syntax:
`function void srand( long seed )`

## Description
[random()](random.md) generates random numbers using a multiplicative congruential random number generator. The default seed is 1. *srand()* resets the random number generator to the starting point specified by the *seed* argument (the seed can be any long value).

## Arguments
| | | |
|---|---|---|
| `long` | `seed` |    |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long r_number
   srand( 175 )
   r_number = random()
```

## Related topics
- [Random number generators overview and synopsis](overview_and_synopsis.md)
