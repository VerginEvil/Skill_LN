# monitor_remove_interval()

## Syntax:
`function long monitor_remove_interval( long interval_id )`

## Description
Removes an interval.
When this function succeeds, subsequent use of this interval id will result in a monitor_error_unknown_interval error.

## Arguments
| | | |
|---|---|---|
| `long` | `interval_id` |  The id of the interval that must be removed.  |

## Return values
| | |
|---|---|
| On success | Returns 0. |
| On failure | Returns an error code (value < 0), possible values are: monitor_not_enabled monitor_error_unknown_interval |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Monitoring overview and synopsis](overview_and_synopsis.md)

- [Monitoring errors.](errors.md)
