# create.object()

## Syntax:
`function long create.object( long type, long parent_object, [ long attribute, value [, size] ], ... )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This creates a new object of the specified type.

## Arguments
| | | |
|---|---|---|
| `long` | `type` |  The type of object to be created. For example, DsCbarMenu or DsCcheckBox.  |
| `long` | `parent_object` |  The ID of the parent object. You must create an object within a parent object. The parent object can be a main window, another object, or the [current.display()](../functions_system_and_user_information/current.display.md).  |
| `[ long` | `attribute, value [, size] ]` |  Use these optional arguments to set the object's attributes. For each attribute you specify, you must include the attribute type (for example, DsNmaximum or DsNminimum), and the attribute value. For attributes of type void data or long array, you must also include the size of the data or array.  |
| `` | `...` |  |

## Return values
The ID for the new object, or 0 if an error occurs. You can subsequently use the returned ID as the *object_id*, *parent_object*, or *object* argument in other functions.

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
