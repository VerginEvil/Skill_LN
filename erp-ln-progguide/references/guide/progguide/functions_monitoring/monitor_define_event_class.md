# monitor_define_event_class()

## Syntax:
`function long monitor_define_event_class( const string event_class_name )`

## Description
Creates a monitor event class. The class will contain the tags as defined in the BSE.
In addition, the monitoring system may afterwards add some tags to each event, such as account, region or host.

## Arguments
| | | |
|---|---|---|
| `const string` | `event_class_name` |  The name of the measurement that will be used. It must consist of printable 7-bit ascii characters.  |

## Return values
| | |
|---|---|
| On success | Returns a number > 0, which identifies the monitor event class which has been created. |
| On failure | No monitor event class is created, and the function returns a number < 0, possible values are: monitor_not_enabled monitor_error_invalid_class_name  |
-
-

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Monitoring overview and synopsis](overview_and_synopsis.md)
- [Monitoring errors.](errors.md)
