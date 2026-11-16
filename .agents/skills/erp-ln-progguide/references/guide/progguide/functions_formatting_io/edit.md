# edit$()

## Syntax:
`function string edit$( void expression, string format )`

## Description
This formats an expression according to a specified format.
Typical usage of this function is (but is not restricted to) the computation of a formatted decimal representation of an integer or floating point input value.

## Arguments
| | |
|---|---|
| 9 | Use to reserve a position for a digit. Inserts a 0 if there is no significant digit in that position. |
| Z | Use to reserve a position for a digit. Inserts a space if there is no significant digit in that position. You can use this both before and after the decimal sign. |
| V | Use to indicate the position of the decimal sign. No decimal sign is displayed. To display a decimal sign, you must enter ‘D’, a period [.], or a comma [,] immediately after this character, depending on which decimal sign you wish to use. |
| D | Use to display the decimal sign as defined in the data dictionary. |
| T | Displays a thousand sign. The representation of the thousand sign is defined in the data dictionary. |
| - | If this is the first or last character in a format string, a negative value is prefixed or suffixed by a minus sign [-] and a positive value is prefixed or suffixed by a space. Minus signs in other positions have the same meaning as ‘Z’. |
| + | If this is the first or last character in a format string, a negative value is prefixed or suffixed by a minus sign [-] and a positive value is prefixed or suffixed by a plus sign [+]. Plus signs in other positions have the same meaning as ‘Z’. |
| * | If this is the first character in a format string, all spaces to the left of the most significant digit are filled with asterisks [*]. |
All characters other than those described above are copied directly to the output string. Periods [.] and commas [,] are exceptions. These are reserved for use as decimal signs and thousand signs.
If the format expression is enclosed by parentheses, these are displayed only if the result is negative.
Starting with TIV level 1640 the thousend separator and decimal sign can be overruled with the function set.numformat.symbols( string decimal(1), string grouping(1) ). The function reset.numformat.symbols() reverts to the normal behavior.

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
