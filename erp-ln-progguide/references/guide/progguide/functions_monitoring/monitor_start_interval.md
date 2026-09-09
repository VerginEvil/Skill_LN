# monitor_start_interval()

## Syntax:
`function long monitor_start_interval( long interval_class_id )`

## Description
Start a timer for an interval of the indicated class.

## Arguments
| | | |
|---|---|---|
| `long` | `interval_class_id` |  The id of the interval class the timer must be started for.  |

## Return values
| | |
|---|---|
| On success | The interval will be remembered, and the function returns the interval id (value > 0). |
| On failure | No timer will be started, nor will an interval be remembered. The function will return an error code (value < 0), possible values are: monitor_not_enabled monitor_error_unknown_class |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Monitoring overview and synopsis](overview_and_synopsis.md)

- [Monitoring errors.](errors.md)
