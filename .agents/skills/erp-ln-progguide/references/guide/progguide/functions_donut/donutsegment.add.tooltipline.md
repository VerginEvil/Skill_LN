# donutsegment.add.tooltipline()

## Syntax:
`function long donutsegment.add.tooltipline( long i.segmentid, const string i.tooltip )`

## Description
This function adds a tooltip line to the segment. LN UI will display each line as a separate line below each other.

## Arguments
| | | |
|---|---|---|
| `long` | `i.segmentid` |  The id returned by the function donut.add.segment.  |
| `const string` | `i.tooltip` |  A tooltip description. Multiple added lines are displayed as separate lines by LN UI.  |

## Return values
| | |
|---|---|
| 0 | Success |
| -1 | Failure, probably the i.segmentid was not correct. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2492.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Donut overview and synopsis](overview_and_synopsis.md)
