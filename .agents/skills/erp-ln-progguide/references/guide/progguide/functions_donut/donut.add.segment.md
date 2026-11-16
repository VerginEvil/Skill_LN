# donut.add.segment()

## Syntax:
`function long donut.add.segment( long i.donutid, const string i.segmentname, const string i.title, long | double i.value, Color The color of the segment, one of the available colors in the color, long i.tint )`

## Description
This function adds a segment to the donut.

## Arguments
| | | |
|---|---|---|
| `long` | `i.donutid` |  The id returned by the function donut.new.  |
| `const string` | `i.segmentname` |  Name of the segment, will be used in the callback of the function donut.'fieldname'.clicked.  |
| `const string` | `i.title` |  The title of the segment. The title will be displayed in the legend of the donut.  |
| `long | double` | `i.value` |  The value (y) of the segment.  |
| `Color` | `The color of the segment, one of the available colors in the color` |  The value (y) of the segment. Options: COLOR.PALETTE.RUBY COLOR.PALETTE.AMBER COLOR.PALETTE.EMERALD COLOR.PALETTE.TURQUOISE COLOR.PALETTE.AZURE COLOR.PALETTE.AMETHYST COLOR.PALETTE.SLATE COLOR.PALETTE.ERROR COLOR.PALETTE.WARNING COLOR.PALETTE.CAUTION COLOR.PALETTE.GOOD COLOR.PALETTE.INFO  |
| `long` | `i.tint` |  The tint of the color for the segment. Value 2,4,6,8,10 can be used in case of a not status color RUBY, AMBER, EMERALD, TURQUOISE, AZURE, AMETHYST, SLATE). Another value will result in a color being selected by LN UI. For the status colors (ERROR, WARNING, CAUTION, GOOD, INFO) no tint should be set.If a tint or another value than 0 is used, then a color will be selected by LN UI.  |

## Return values
| | |
|---|---|
| not 0 | Success, the id of the created segment xml document is returned. |
| 0 | Failure, creation of the xml-document failed. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2492.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Donut overview and synopsis](overview_and_synopsis.md)
