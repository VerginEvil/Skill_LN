# string.to.bounded.long()

## Syntax:
`function long string.to.bounded.long( string string$, long lowerbound, long upperbound, [ ref long appliedbounds ] )`

## Description
This function performs explicit string to long type conversion. If the resulting value is within the specified bounds, that value is returned. Otherwise, the concerned bound is returned.

## Arguments
| | | |
|---|---|---|
| `string` | `string$` |  String value to be converted to a long value.  |
| `long` | `lowerbound` |  Lower bound to be applied to the exact long value resulting from the conversion. If the exact result is less than this lower bound, then the lower bound is returned rather than the exact result.  |
| `long` | `upperbound` |  Upper bound to be applied to the exact long value resulting from the conversion. If the exact result is greater than this upper bound, then the upper bound is returned rather than the exact result.  |
| `[ ref long` | `appliedbounds ]` |  Optional argument into which information will be written about the success of the conversion.  |

## Return values
| | | | |
|---|---|---|---|
| Condition on exact conversion result | Description | Value returned by string.to.bounded.long | Value returned in appliedbounds |
| >= lowerbound and <= upperbound  | success | exact conversion result | 0 |
| < lowerbound and lowerbound <= upperbound  | lower bound is applied | lowerbound | STRING.TO.BOUNDED.LONG.APPLIED.LOWERBOUND |
| > upperbound and upperbound >= lowerbound  | upper bound is applied | upperbound | STRING.TO.BOUNDED.LONG.APPLIED.UPPERBOUND |
| upperbound < lowerbound | inconsistent bounds | upperbound | STRING.TO.BOUNDED.LONG.APPLIED.LOWERBOUND + STRING.TO.BOUNDED.LONG.APPLIED.UPPERBOUND |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2020.

## Related topics
- A similar function, but with implicit bounds: [lval()](lval.md)
- Inverse operation: [str$()](str.md)
- Conversion to floating point type: [val()](val.md)
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
