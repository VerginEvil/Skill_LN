# random()

## Syntax:
`function long random( )`

## Description
This function uses a system-independent random number generator. On all systems, the generator will generate the same random numbers, provided that the same seed is supplied.
Calls to this function return successive random numbers in the range 0 to 32767. The function uses a multiplicative congruential random number generator, with period 2^32. The default seed is 1. To use a different seed, call [srand()](srand.md) before starting the generator.

## Return values
A random number.

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long r_number
   srand( 200 )
   r_number = random()
```

## Related topics
- [Random number generators overview and synopsis](overview_and_synopsis.md)
