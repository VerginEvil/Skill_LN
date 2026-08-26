# edit$()

## Syntax:
`function string edit$( void expression, string format )`

## Description
This formats an expression according to a specified format.
Typical usage of this function is (but is not restricted to) the computation of a formatted decimal representation of an integer or floating point input value.

## Arguments
| | | |
|---|---|---|
| `void` | `expression` |  The expression that must be formatted. Implicit conversion of the input value from its original type to type string is performed. The resulting string value is formatted according to the format argument.  |
| `string` | `format` |  A string that defines the required format. The following formatting characters are available:  |

## Return values
The function returns the formatted expression. If the specified expression does not fit in the format string, the result is filled with the overflow characters defined in the data dictionary.

## Context
This function is implemented in the porting set and can be used in all script types.
Note  To include currency symbols or to use formats defined in the data dictionary, use [sprintf$()](sprintf.md).

## Examples
These examples assume that the decimal sign, thousand sign, and overflow character are defined in the data dictionary as a period [.], comma [,] and hash sign [#] respectively
| | | | |
|---|---|---|---|
| Expression | Format | Result | Remarks |
| 5286.45 | 9999VD99 | 5286.45 |  |
| 463.897 | 9999VD99 | 0463.89 |  |
| 34.65 | 9999VD99 | 0034.65 |  |
| -3.1 | 9999VD99 | ####### | overflow |
| 5286.45 | ZZZZVD99 | 5286.45 |  |
| 463.897 | ZZZZVD99 | 463.89 |  |
| 34.65 | ZZZZVD99 | 34.65 |  |
| -3.1 | ZZZZVD99 | -3.10 |  |
| 5286.45 | ----VD99 | 5286.45 | no space for - |
| 463.897 | ----VD99 | 463.89 |  |
| 34.65 | ----VD99 | 34.65 |  |
| -3.1 | ----VD99 | -3.10 |  |
| 5286.45 | ++++VD99 | 5286.45 | no space for + |
| 463.897 | ++++VD99 | +463.89 |  |
| 34.65 | ++++VD99 | +34.65 |  |
| -3.1 | ++++VD99 | -3.10 |  |
| 34.65 | +ZZZVD99 | +34.65 |  |
| -3.1 | +ZZZVD99 | -3.10 |  |
| 5286.45 | ZZZZVD99- | 5286.45 |  |
| -3.1 | ZZZZVD99- | 3.10- |  |
| 5286.45 | ZZZZVD99+ | 5286.45+ |  |
| -3.1 | ZZZZVD99+ | 3.10- |  |
| 5286.45 | *ZZZVD99 | ###### | overflow |
| 463.897 | *ZZZVD99 | 463.89 |  |
| 34.65 | *ZZZVD99 | *34.65 |  |
| -3.1 | *ZZZVD99 | *-3.10 |  |
| 5286.45 | ZTZZZVD99 | 5,286.45 |  |
| 463.897 | ZTZZZVD99 | 463.89 |  |
| 5286.45 | ZDZZZVD99 | 5.286.45 |  |
| 463.8970 | ZZZVD99ZZ | 463.897 |  |
| -3.1 | (ZZZVD99) | (3.10) |  |
| 3.1 | (ZZZVD99) | 3.10 |  |

## Related topics
- [Formatting input and output - overview and synopsis](overview_and_synopsis.md)
