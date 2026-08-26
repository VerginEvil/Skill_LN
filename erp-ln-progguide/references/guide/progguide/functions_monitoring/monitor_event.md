# monitor_event()

## Syntax:
`function long monitor_event( long event_class_id, void ... )`

## Description
An event will be reported to the monitoring system.
The event will be off the class identified and contains all tags and fields as defined for this class. In addition, the metrics which are given in this call will be added to the reported event.

## Arguments
| | | |
|---|---|---|
| `long` | `event_class_id` |  The id of the event class the event must be reported for.  |
| `void` | `...` |  One or more pairs of arguments:  |

## Return values
| | |
|---|---|
| On success | The event will be reported, and the function returns 0. |
| On failure | No event will be reported and the function returns an error code (value < 0), possible values are: monitor_not_enabled monitor_error_unknown_class monitor_error_unknown_field monitor_error_missing_field_value monitor_error_field_value_of_wrong_type monitor_error_invalid_field_value  |
-
-
-
-
-
-

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Monitoring overview and synopsis](overview_and_synopsis.md)
- [Monitoring errors.](errors.md)
