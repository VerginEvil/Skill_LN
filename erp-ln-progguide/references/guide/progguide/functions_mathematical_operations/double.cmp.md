# double.cmp()

## Syntax:
`function long double.cmp( double double1, double double2, double tolerance )`

## Description

## Arguments
| | | |
|---|---|---|
| `double` | `double1` |  A double value.  |
| `double` | `double2` |  A double value.  |
| `double` | `tolerance` |  Specifies a tolerance value for the function. If the difference between the two doubles is less than this value, the doubles are considered equal. Do not use a tolerance of 0. Also, do not use a negative tolerance.  |

## Return values
0 the difference between the doubles is less than the tolerance.
-1 *double1* is less than *double2* (the difference is greater than the tolerance).
1 *double1* is greater than or equal to *double2* (the difference is greater than the tolerance).

## Context
This function is implemented in the porting set and can be used in all script types.

## Example:
```

double doub1, doub2

if double.cmp( doub1, doub2, 0.0001 ) = 0 then
        | the two doubles are equal
        ...
endif
```

## Related topics
- [Mathematical operations overview](overview.md)

- [Mathematical operations synopsis](synopsis.md)
