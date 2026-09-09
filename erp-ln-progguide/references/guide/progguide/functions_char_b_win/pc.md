# pc$()

## Syntax:
`function string pc$( long num_expr )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
Use this to set certain printer codes. The following printer codes are available:
| | |
|---|---|
| 1 | paper bin 1 |
| 2 | paper bin 2 |
| 3 | paper bin 3 |
| 4 | paper bin 4 |
| 5 | landscape |
| 6 | portrait |
| 7 | usr1 |
| 8 | usr2 |
| ... | ... |
| 22 | usr16 |
You define codes 9 to 22 in the printer information file for the particular printer (for example, $BSE/lib/printinf/m/m290).

## Arguments
| | | |
|---|---|---|
| `long` | `num_expr` |    |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
