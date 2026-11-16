# change.object()

## Syntax:
`function void change.object( long object_id, long attribute, void value, [ long size ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This changes the attribute values of the specified object.

## Arguments
| | | |
|---|---|---|
| `long` | `object_id` |  The object ID, as returned by [create.object()](create.object.md) when the object was created.  |
| `long` | `attribute` |  Use these arguments to set new values for the object's attributes. For each attribute you specify, you must include the attribute type (for example, DsNmaximum or DsNminimum), and the attribute value. For attributes of type void data or long array, you must also include the size of the data or array.  |
| `void` | `value` |    |
| `[ long` | `size ]` |    |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
