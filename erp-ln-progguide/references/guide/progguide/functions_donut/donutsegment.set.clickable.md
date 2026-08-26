# donutsegment.set.clickable()

## Syntax:
`function long donutsegment.set.clickable( long i.segmentid, boolean i.is.clickable )`

## Description
Sets the segment to be clickable or not clickable. If a segment is clickable this is shown in the donut display.

## Arguments
| | | |
|---|---|---|
| `long` | `i.segmentid` |  The id returned by the function donut.add.segment.  |
| `boolean` | `i.is.clickable` |  True: segment is clickable, a click will result in a visible action by the script. False: segment is not clickable, no linked action.  |

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
