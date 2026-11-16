# monitor_add_metric()

## Syntax:
`function long monitor_add_metric( long event_class_id, const string metric_name, long metric_type )`

## Description
Adds or replaces a metric to an existing monitor event/interval class.

## Arguments
| | | |
|---|---|---|
| `long` | `event_class_id` |  The id of the event or interval the metric must be added to.  |
| `const string` | `metric_name` |  The name of the metric. It must consist of printable 7-bit ascii characters.  |
| `long` | `metric_type` |  The type of the metric. This must be one of the following: VAR.TYPE.LONG VAR.TYPE.BOOLEAN VAR.TYPE.STRING VAR.TYPE.DOUBLE  |

## Return values
| | |
|---|---|
| On success | Returns 0. |
| On failure | Returns an error code (value < 0), possible values are: monitor_not_enabled monitor_error_unknown_class monitor_error_invalid_field_name monitor_error_invalid_field_type |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Monitoring overview and synopsis](overview_and_synopsis.md)

- [Monitoring errors.](errors.md)
