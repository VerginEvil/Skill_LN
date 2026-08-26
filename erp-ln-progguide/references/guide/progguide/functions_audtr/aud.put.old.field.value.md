# aud.put.old.field.value()

## Syntax:
`function void aud.put.old.field.value( long pid, string variable.name, long selection.id, long table.id, long field.id, long element, [ bool endian ] )`

## Description
Use aud.put.old.field.value to retrieve the value of a field from the old (new) value string. The retrieved value is put into the variable supplied by the application.
If the action is a table operation the old value has no meaning and therefore this function cannot be used in that case. Depending on the status of a field the old value and/or new value can be retrieved.
| | |
|---|---|
| Insert row | The value part of the action row contains all the field values of the inserted row. This part is copied to the new.value string.  |
| Delete row | The value part of the action row contains all the field values of the deleted row. This part is copied to the new.value string.  |
| Update row |  The value part of the action row contains both old and new values but not for all fields. Only those fields that have been changed or are part of the key or specified in the audit_set file are stored in the action row. Unchanged field entries in the action row consist of only two parts: the status that is 'N', meaning unchanged, and the old value. Changed field entries in the action row consist of three parts: the status which is 'Y', meaning that the field has changed, and both old value and new value. The function reads each field entry in the action row and, depending on the status, copies the values to the old.value or the new.value string. If the field is unchanged, the status string will have an 'N' for this field entry otherwise an 'Y'.  |
The following table shows whether the functions can be used, depending on action type and status:
| | | | |
|---|---|---|---|
| Action Type | Status | Field in OldValues | Field in NewValues |
| I | Y | No | Yes |
| I | X | No | No |
| D | Y | Yes | No |
| D | X | No | No |
| U | Y | Yes | Yes |
| U | N | Yes | Yes |
| U | X | No | No |
| U | X | No | No |

## Arguments
| | | |
|---|---|---|
| `long` | `pid` |  Id of the current process. This must be filled in the same manner as the Infor Enterprise Server function put.var().  |
| `string` | `variable.name` |  The name of the variable that will contain the extracted field value.  |
| `long` | `selection.id` |  Id of the selection, as provided by aud.select.transactions  |
| `long` | `table.id` |  Id of the table on which the action occurred, which is used to retrieve the detailed action data using function aud.get.field.status, aud.put.old.field.value and aud.put.new.field.value. This id is also used to get the meta data information, in case it has been changed.company: the company that holds the updated table.  |
| `long` | `field.id` |  Identification of the field as retrieved using function aud.get.field.ids. Precondition: *field.id* must not be 0: for not existing fields no field information can be retrieved. ( *action.type* = 'D' and FieldStatus = 'A') or ( *action.type* = 'U' and FieldStatus = ('Y' or 'N')).  |
| `long` | `element` |  Identification of the array element within a field.  |
| `[ bool` | `endian ]` |  Defines how the data in *element* must be interpreted. It is assumed that data is stored in big endian order (highest byte first) . If little endian order is required set this optional argument to 1.  |

## Return values
None

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Restrictions
This function will not check the input, because of performance reasons. Instead the combination *selection.id*, *table.id*, *field.id* is assumed to refer to an existing field, as returned by aud.get.field.ids. This means that if the input parameters are not valid, an error message will be presented to the end user.
During the last aud.get.next.action for this selection, an *action.type* must have been returned that is 'I', 'U' or 'D'. The last execution of aud.get.field.status for this action must have indicated a status <> "X".
The combination of *action.type* and status for the field must be one of the following:
Status <> "X" and ( *action.type* = "U" or *action.type* = "D")
In all other cases the value of a field has no meaning and therefore this function cannot be used in those cases.

## Related topics
- [Audit management overview](audit_management_overview.md)
- [Audit management synopsis](audit_management_synopsis.md)
- [Audit management examples](audit_management_examples.md)
