# mb.type()

## Syntax:
`function long mb.type( void value )`

## Description
This function tests whether the runtime type of the supplied value is ['multibyte string'](../3gl_features/multibyte_strings.md) or 'multibyte string array'. It only tests the runtime type of the supplied value, not its contents.

## Arguments
| | | |
|---|---|---|
| `void` | `value` |  The function determines whether the runtime type of *value* is 'multibyte string' or 'multibyte string array'. Before [porting set TIV](../tiv/tiv_overview.md) [level 2340](../tiv/tiv_2340.md), *value* had to be of type string. As of [porting set TIV](../tiv/tiv_overview.md) [level 2340](../tiv/tiv_2340.md), this argument can be of any type, allowing to use this function also for a string array. See also the example section.  |

## Return values
| | |
|---|---|
| 0 | the supplied value is neither of type multibyte string nor of type multibyte string array. |
| 1 | the supplied value is of type multibyte string or of type multibyte string array. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

STRING	my_string( 3 )
STRING	string_array( 3, 4 )

STRING	string_mb( 3 ) mb
STRING	string_mb_matrix( 3, 4, 5 ) mb

| Before porting set TIV level 2340, only string type arguments are allowed.
| To determine whether a string array is multibyte or single-byte,
| apply mb.type to the first string in the array.

mb.type( my_string )                      | result is 0
mb.type( my_string( 1 ) )                 | result is 0
mb.type( string_array( 1, 1 ) )           | result is 0

mb.type( string_mb )                      | result is 1
mb.type( string_mb( 1 ) )                 | result is 1
mb.type( string_mb_matrix( 1, 1, 1 ) )    | result is 1

STRING	string_based( 1 ) based
STRING	string_based_array( 1, 1 ) based

STRING	string_mb_based( 1 ) mb based
STRING	string_mb_based_cube( 1, 1, 1, 1 ) mb based

| Array access to an unallocated based string (or string array)
| will cause a 'Use of NULL pointer' runtime error
| mb.type( string_based_array( 1, 1 ) )

| As of porting set TIV level 2340, any type arguments are allowed.

#if ES_TIV_LEVEL >= 2340

mb.type( string_based )                   | result is 0
mb.type( string_based_array )             | result is 0

mb.type( string_mb_based )                | result is 1
mb.type( string_mb_based_cube )           | result is 1

mb.type( string_array )                   | result is 0
mb.type( string_mb_matrix )               | result is 1

LONG	my_long
LONG	long_array( 2 )

DOUBLE	my_double
DOUBLE	double_array( 2 )

mb.type( my_long )                        | result is 0
mb.type( long_array )                     | result is 0

mb.type( my_double )                      | result is 0
mb.type( double_array )                   | result is 0

#endif	| ES_TIV_LEVEL >= 2340
```

## Related topics
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
