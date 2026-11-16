# progressbar.add.segment()

## Syntax:
`function long progressbar.add.segment( long i.percentage, const string i.color )`

## Description
This function adds a segment (state) to the Progress bar.
There can be a maximum of 3 segments for the Progress bar.

## Arguments
| | | |
|---|---|---|
| `long` | `i.percentage` |  The percentage of the segement. The totalof the percentages should be 100 or less. If the total percentage is less than 100, the remaining part of the progress bar will get the remaining part color by LN UI.  |
| `const string` | `i.color` |  The color (state) of the segment, one of the available colors (states) in the color palette: COLOR.PROGRESS.ERROR COLOR.PROGRESS.CAUTION COLOR.PROGRESS.COMPLETE COLOR.PROGRESS.DEFAULT COLOR.PROGRESS.ERROR.SECONDARY COLOR.PROGRESS.CAUTION.SECONDARY COLOR.PROGRESS.COMPLETE.SECONDARY COLOR.PROGRESS.DEFAULT.SECONDARY If another value is set, the default color will be used. If a segment is created with a secondary color, the same color (state) should be used as for the segment with the primary color. Default: COLOR.PROGRESS.DEFAULT  |

## Return values
| | |
|---|---|
| 0 | Success |
| -1 | Failure, Field is not a Progress bar. |
| -2 | Failure, Color value is not correct. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2610.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "before.display" section for the field that is set as a Progress bar by calling the function progressbar.set.field.

## Related topics
- Overview and synopsis
