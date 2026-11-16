# chm.new()

## Syntax:
`function long chm.new( string chart_name(16), ref string chart_type() )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This creates a new chart. The chart is not saved until the user executes the Save command.

## Arguments
| | | |
|---|---|---|
| `string` | `chart_name(16)` |  The name of the new chart.  |
| `ref string` | `chart_type()` |  The chart type. If you do not specify an existing chart type, the Chart Manager selects the default chart type, as defined in the Chart Manager Application session (ttchm1500m000).  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Chart manager overview](overview.md)

- [Chart manager synopsis](synopsis.md)

- [Creating a chart manager client application](creating_a_chart_manager_client_application.md)

- [Chart manager example](example.md)
