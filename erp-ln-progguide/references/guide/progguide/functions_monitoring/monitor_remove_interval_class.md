# monitor_remove_interval_class()

## Syntax:
`function long monitor_remove_interval_class( long interval_class_id )`

## Description
Removes an interval class.
In addition to the interval class itself, all associated intervals are removed as well.
When this function succeeds, subsequent use of this interval class id will result in a monitor_error_unknown_class error.

## Arguments
| | | |
|---|---|---|
| `long` | `interval_class_id` |  The id of the interval class that must be removed.  |

## Return values
| | |
|---|---|
| On success | Returns 0. |
| On failure | Returns an error code (value < 0), possible values are: monitor_not_enabled monitor_error_unknown_class  |
-
-

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Monitoring overview and synopsis](overview_and_synopsis.md)
- [Monitoring errors.](errors.md)
