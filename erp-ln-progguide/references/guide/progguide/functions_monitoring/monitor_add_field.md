# monitor_add_field()

## Syntax:
`function long monitor_add_field( long event_class_id, const string field_name, void field_value )`

## Description
Adds or replaces a field to an existing monitor event/interval class.
A field is like a metric, but all events of a class have the same value for this field. A field differs from a tag in that it doesn’t identify the event, it just provides supplementary information. Furthermore, a field is not restricted to string for its type.

## Arguments
| | | |
|---|---|---|
| `long` | `event_class_id` |  The id of the event or interval the field must be added to.  |
| `const string` | `field_name` |  The name of the field. It must consist of printable 7-bit ascii characters.  |
| `void` | `field_value` |  The value of the field. The type of the actual argument determines the type of the value, its type is restricted to: long boolean string The string must not contain a newline character. double  |
-
-
-
-

## Return values
| | |
|---|---|
| On success | Returns 0. |
| On failure | Returns an error code (value < 0), possible values are: monitor_not_enabled monitor_error_unknown_class monitor_error_invalid_field_name monitor_error_invalid_field_type  |
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
