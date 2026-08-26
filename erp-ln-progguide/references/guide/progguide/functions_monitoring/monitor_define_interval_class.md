# monitor_define_interval_class()

## Syntax:
`function long monitor_define_interval_class( const string interval_class_name )`

## Description
Creates a monitor interval class.
A monitor interval class is a special monitor event class, which has 1 additional metric (‘duration’), the value for this metric is automatically determined, being the time (in seconds, with millisecond granularity) between the start of a timer and the actual occurrence of the event.

## Arguments
| | | |
|---|---|---|
| `const string` | `interval_class_name` |  The name of the measurement that will be used for this interval class. It must consist of printable 7-bit ascii characters.  |

## Return values
| | |
|---|---|
| On success | Returns a number > 0, which identifies the monitor interval class which has been created. |
| On failure | No monitor interval class is created, and the function returns a number < 0, possible values are: monitor_not_enabled monitor_error_invalid_class_name  |
-
-

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Monitoring overview and synopsis](overview_and_synopsis.md)
- [Monitoring errors.](errors.md)
