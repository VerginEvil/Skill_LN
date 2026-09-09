# monitor_add_tag()

## Syntax:
`function long monitor_add_tag( long event_class_id, const string tag_name, const string tag_value )`

## Description
Adds or replaces a tag to an existing monitor event/interval class.

## Arguments
| | | |
|---|---|---|
| `long` | `event_class_id` |  The id of the event or interval the tag must be added to.  |
| `const string` | `tag_name` |  The name of the tag. It must consist of printable 7-bit ascii characters.  |
| `const string` | `tag_value` |  The value of the tag. It must not contain a newline character.  |

## Return values
| | |
|---|---|
| On success | Returns 0. |
| On failure | Returns an error code (value < 0), possible values are: monitor_not_enabled monitor_error_unknown_class monitor_error_invalid_tag_name monitor_error_invalid_tag_value |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Monitoring overview and synopsis](overview_and_synopsis.md)

- [Monitoring errors.](errors.md)
