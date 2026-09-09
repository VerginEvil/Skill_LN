# chart.series.set.color()

## Syntax:
`#include <bic_dialog>`
`function long chart.series.set.color( long series, const string color, [ long tint ] )`

## Description
With this function a color is set for the series. As a default a color will be selected by LN UI.

## Arguments
| | | |
|---|---|---|
| `long` | `series` |  The id returned by the function chart.add.series or function chart.add.line.series.  |
| `const string` | `color` |  The color of the segment, one of the available colors in the color palette: COLOR.PALETTE.RUBY COLOR.PALETTE.AMBER COLOR.PALETTE.EMERALD COLOR.PALETTE.TURQUOISE COLOR.PALETTE.AZURE COLOR.PALETTE.SLATE Or one of the available status colors: COLOR.PALETTE.ERROR COLOR.PALETTE.WARNING COLOR.PALETTE.GOOD COLOR.PALETTE.INFO  |
| `[ long` | `tint ]` |  The tint of the color for the segment. Value 2,4,6,8,10 can be used in case of a not status color (RUBY, AMBER, EMERALD, TURQUOISE, AZURE, AMETHYST, SLATE). For the status colors (ERROR, WARNING, CAUTION, GOOD, INFO) no tint should be set. When for tint any value other than 0 is used, then a color will be selected by LN UI.  |

## Return values
Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Failure, probably series identification is not correct. |
| -2 | Failure, color-tint combination not supported, invalid values. |
| -3 | Failure, invalid tint value. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2521.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Programmable dialogs synopsis](synopsis.md)
