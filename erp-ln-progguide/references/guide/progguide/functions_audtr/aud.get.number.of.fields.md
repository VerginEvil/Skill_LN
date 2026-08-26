# aud.get.number.of.fields()

## Syntax:
`function long aud.get.number.of.fields( long selection.id, long table.id, ref long number.of.fields )`

## Description
Use this function to determine the number of fields, read from the data dictionary, that are stored in the sequence files. This function is especially useful if the user is not aware or interested in the table fields but simply needs to pick up the value of all fields. In this situation the user uses this function together with the [aud.get.field.list()](aud.get.field.list.md) to read all the information of all fields.

## Arguments
| | | |
|---|---|---|
| `long` | `selection.id` |  Id of the selection, as provided by [aud.select.transactions()](aud.select.transactions.md)  |
| `long` | `table.id` |  Id of the table on which the action occurred as provided by the [aud.get.next.action()](aud.get.next.action.md). The *table.id* is used to retrieve the detailed action data using function [aud.get.field.status()](aud.get.field.status.md), [aud.put.old.field.value()](aud.put.old.field.value.md), and [aud.put.new.field.value()](aud.put.old.field.value.md). This id is also used to get the meta data information, in case it has been changed.  |
| `ref long` | `number.of.fields` |  The number of fields logged in the audit trail for the specified table. This can be used to run the function [aud.get.field.list()](aud.get.field.list.md).  |

## Return values
| | |
|---|---|
| AUD_INCORRECT_SELECTION_ID | is invalid. |
| AUD_INCORRECT_TABLE_ID | is invalid. |
| AUD_OK | The number of fields can be retrieved. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Restrictions
The function [aud.get.next.action()](aud.get.next.action.md) has to be called prior to this function so that the fields list contains the dictionary information stored in the audit file.

## Related topics
- [Audit management overview](audit_management_overview.md)
- [Audit management synopsis](audit_management_synopsis.md)
- [Audit management examples](audit_management_examples.md)
