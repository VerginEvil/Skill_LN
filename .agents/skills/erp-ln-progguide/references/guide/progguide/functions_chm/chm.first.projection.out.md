# chm.first.projection.out()

## Syntax:
`function long chm.first.projection.out( ref double projection_point, ref long footnote_no )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This retrieves information about the first projection point in the current chart. Use [chm.next.projection.out()](chm.next.projection.out.md) to retrieve information about subsequent projection points in the chart.

## Arguments
| | | |
|---|---|---|
| `ref double` | `projection_point` |  This returns the position on the category axis where the projection point occurs.  |
| `ref long` | `footnote_no` |  This returns the number of the footnote associated with the projection point. It returns 0 if there is no footnote associated with the projection point.  |

## Return values
| | |
|---|---|
| CHM_OK | Success. |
| CHM_ERROR | Error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Chart manager overview](overview.md)

- [Chart manager synopsis](synopsis.md)

- [Creating a chart manager client application](creating_a_chart_manager_client_application.md)

- [Chart manager example](example.md)
