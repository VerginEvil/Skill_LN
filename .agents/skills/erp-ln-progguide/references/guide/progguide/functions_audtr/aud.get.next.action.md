# aud.get.next.action()

## Syntax:
`function long aud.get.next.action( long selection.id, ref long table.id, ref long company, ref string table.code, ref bool meta.data.changed, ref long current.action.number, ref string action.type )`

## Description
Determines and reads the next action from the list of tables that was constructed by the [aud.get.next.transaction()](aud.get.next.transaction.md) function.
The action header is returned, which consists of the *current.action.number* and the *action.type*. Furthermore, an indication is given on whether the meta data is changed. If this is the case, the number of fields, the type, or the length of one or more fields has changed, which means the meta data functions [aud.get.field.ids()](aud.get.field.ids.md) and [aud.get.field.info()](aud.get.field.info.md) must be used to handle the meta data.
The other information on the action (for each field the status, the old value and the new value) is kept internally and can be retrieved using function [aud.get.field.status()](aud.get.field.status.md), [aud.put.old.field.value()](aud.put.old.field.value.md), and [aud.put.new.field.value()](aud.put.old.field.value.md).
The *action.type* specifies if the action is a table operation (create table, clear table and drop table) or a row operation (insert row, delete row and update row).
If the maximum number of opened files has been reached, the function uses the action numbers to determine the last action in the list. The sequence file of this action is closed before opening a new sequence file.

## Arguments
| | | |
|---|---|---|
| `long` | `selection.id` |  Id of the selection, as provided by [aud.select.transactions()](aud.select.transactions.md)  |
| `ref long` | `table.id` |  Id of the table on which the action occurred that is used to retrieve the detailed action data using functions [aud.get.field.status()](aud.get.field.status.md), [aud.put.old.field.value()](aud.put.old.field.value.md), and [aud.put.new.field.value()](aud.put.old.field.value.md). This id is also used to get the meta data information, in case it has been changed.  |
| `ref long` | `company` |  Infor Enterprise Server company that contains the table on which the database action was done.  |
| `ref string` | `table.code` |  The code of the updated database table  |
| `ref bool` | `meta.data.changed` |    |
| `ref long` | `current.action.number` |  Sequence number of the action within the transaction.  |
| `ref string` | `action.type` |  A character that specifies the type of action retrieved. The string contains an 'I' for inserting a row, 'U' for updating a row and a 'D' for deleting a row. For table operations the string contains a 'C' for creating a table, 'L' for clearing a table and 'R' for dropping a table.  |

## Return values
| | |
|---|---|
| AUD_OK | Next transaction in the selection is determined and transaction header data is retrieved |
| AUD_FAIL | The transaction data could not be retrieved |
| AUD_NO_MORE_ACTIONS | There are no more transactions in the selection |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Restrictions
The function [aud.get.next.transaction()](aud.get.next.transaction.md) has to be called successfully prior to this function.

## State
If *meta.data.changed* is true, the internal meta data information on the fields have been refreshed. This information must be retrieved using functions [aud.get.field.ids()](aud.get.field.ids.md) and [aud.get.field.info()](aud.get.field.info.md).
If *action.type* is 'I', 'U' or 'D' then the row information on the action is available for retrieval using functions [aud.get.field.status()](aud.get.field.status.md), [aud.put.old.field.value()](aud.put.old.field.value.md) and [aud.put.new.field.value()](aud.put.old.field.value.md). See the following table:
| | | | |
|---|---|---|---|
| Action type | aud.get.field.status | aud.get.old.field.value | aud.get.new.field.value |
| 'C' (Create table) | no | no | no |
| 'L' (Clear table) | no | no | no |
| 'R' (Drop table) | no | no | no |
| 'I' (Insert row) | yes | no | yes |
| 'D' (Delete row) | yes | yes | no |
| 'U' (Update row) | yes | yes | yes |
Note: The old and new field value is not available if the status shows the field is not logged in the audit trail. See [aud.get.field.status()](aud.get.field.status.md).

## Related topics
- [Audit management overview](audit_management_overview.md)

- [Audit management synopsis](audit_management_synopsis.md)

- [Audit management examples](audit_management_examples.md)
