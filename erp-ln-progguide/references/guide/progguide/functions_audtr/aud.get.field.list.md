# aud.get.field.list()

## Syntax:
`function long aud.get.field.list( long selection.id, long table.id, ref string field.names(,) )`

## Description
Use this function to get the field names of all fields logged for a database table in the audit trail. This function is especially useful if the user is not aware or interested in the table fields but simply needs the names of all fields. In this case the user uses the [aud.get.number.of.fields()](aud.get.number.of.fields.md) to determine how many fields are available and also uses [aud.get.field.list()](aud.get.field.list.md) to obtain the field ids for each field. The information of these two function can be used to further retrieve field info as well as the value of the field using the functions: [aud.get.field.info()](aud.get.field.info.md), [aud.get.field.status()](aud.get.field.status.md) and [aud.put.old.field.value()](aud.put.old.field.value.md) and [aud.put.new.field.value()](aud.put.old.field.value.md).

## Arguments
| | | |
|---|---|---|
| `long` | `selection.id` |  Id of the selection, as provided by [aud.select.transactions()](aud.select.transactions.md).  |
| `long` | `table.id` |  Id of the table on which the action occurred, as provided by the aud.get.next.action function. The *table.id* is used to retrieve the detailed action data using function [aud.get.field.status()](aud.get.field.status.md), [aud.put.old.field.value()](aud.put.old.field.value.md), and [aud.put.new.field.value()](aud.put.old.field.value.md). This id is also used to get the meta data information, in case it has been changed.  |
| `ref string` | `field.names(,)` |  An array that contains the fields of the table. Note: the number of elements in this array is equal to the number.of.fields returned by function aud.get.number.of.fields()  |

## Return values
| | |
|---|---|
| AUD_INCORRECT_SELECTION_ID | *Selection.id* is invalid.  |
| AUD_INCORRECT_TABLE_ID | *Table.Id* is invalid.  |
| AUD_OK | Names of all fields can be determined |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Restrictions
The function [aud.get.next.action()](aud.get.next.action.md) has to be called prior to this function so that the fields list contains the dictionary information stored in the audit file.

## Related topics
- [Audit management overview](audit_management_overview.md)
- [Audit management synopsis](audit_management_synopsis.md)
- [Audit management examples](audit_management_examples.md)
