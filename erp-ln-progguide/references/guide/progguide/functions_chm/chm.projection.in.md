# chm.projection.in()

## Syntax:
`function long chm.projection.in( double projection_point, long footnote_no )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This defines a projection point for the current chart.

## Arguments
| | | |
|---|---|---|
| `double` | `projection_point` |  This specifies the position on the category axis where the projection point occurs.  |
| `long` | `footnote_no` |  This specifies the number of the footnote (if any) associated with the projection point. Specify 0 here, if you do not want to associate a footnote with the point. You use [chm.footnote.in()](chm.footnote.in.md) to create footnotes.  |

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
