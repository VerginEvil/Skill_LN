# ltoe()

## Syntax:
`function domain ltoe( long long_value )`

## Description
This returns the named constant corresponding to a specified numeric code. The numeric code represents one of the values in an enumerated domain.

## Arguments
| | | |
|---|---|---|
| `long` | `long_value` |  The numeric code represents one of the values in an enumerated domain.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
This example assumes an enumerated domain 'tcyesno' with two possible constants: 'tcyesno.yes’ (=1) and 'tcyesno.no’ (=2).
```

domain    tcyesno active
long      enum_long

active = tcyesno.no
enum_long = etol( active )    | enum_long now contains 2
active = ltoe( 1 )            | active now equals tcyesno.yes
```

## Related topics
- [Enumerates overview and synopsis](overview_and_synopsis.md)

- [Enumerate and set constants](../3gl_features/enumerate_and_set_constants.md)
