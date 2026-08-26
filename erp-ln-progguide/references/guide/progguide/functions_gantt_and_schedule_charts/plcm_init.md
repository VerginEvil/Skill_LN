# plcm.init

## Syntax:
`function long plcm.init( string title, string initial.types, [ long options ] )`

## Description
This function must be the first to be called, it initializes the global data structures of the plan chart.

## Arguments
| | | |
|---|---|---|
| `string` | `title` |  The title for the Plan Chart.  |
| `string` | `initial.types` |  Initial type of the chart. Supported types: CHART_TYPE_GANTT, CHART_TYPE_SCHEDULE. Or you can display both by passing CHART_TYPE_GANTT +CHART_TYPE_SCHEDULE.  |
| `[ long` | `options ]` |  When passing both types to the initial.types argument, the default.type argument determines which type will be default shown: STARTUP_CHART_TYPE_GANTT or STARTUP_CHART_TYPE_SCHEDULE,SHOW_COMPLETION_PERCENTAGES,EXPAND_ALL_ROWS,DELETE_NOT_ALLOWED  |

## Return values
| | |
|---|---|
| 0 | Success |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Synopsis](synopsis.md)
- [Example](example.md)
