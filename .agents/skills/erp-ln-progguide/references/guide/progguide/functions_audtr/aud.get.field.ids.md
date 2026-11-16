# aud.get.field.ids()

## Syntax:
`function long aud.get.field.ids( long selection.id, long table.id, long number.of.fields, const string field.names(,), ref long field.ids() )`

## Description
[aud.get.next.action()](aud.get.next.action.md) stores the contents of the action row internally: old value, new value and status of each field. To retrieve this information, the application needs to have a reference for each field. These references are called field ids. Only when the meta data is changed do the field ids change, so only in such a case does this function have to be used. This function also enables the user to filter only those fields that are relevant to the application by means of a *field.names* array. This array contains the field names for which an id has to be retrieved.

## Arguments
| | | |
|---|---|---|
| `long` | `selection.id` |  Id of the selection, as provided by [aud.select.transactions()](aud.select.transactions.md)  |
| `long` | `table.id` |  Id of the table on which the action occurred, which is used to retrieve the detailed action data using function [aud.get.field.status()](aud.get.field.status.md), [aud.put.old.field.value()](aud.put.old.field.value.md), and [aud.put.new.field.value()](aud.put.old.field.value.md). This id is also used to get the meta data information, in case it has been changed.  |
| `long` | `number.of.fields` |  The number of fields specified in the field.names array.  |
| `const string` | `field.names(,)` |  An array that contains one or more fields of the table.  |
| `ref long` | `field.ids()` |  An array that contains an index for each field in the *field.names* array. If the field is not in the audit trail data, the index is 0. These ids can be used in function [aud.get.field.info()](aud.get.field.info.md), aud.get.field.status(), aud.put.old.field.value() and aud.put.new.field.value().  |

## Return values
| | |
|---|---|
| AUD_INCORRECT_SELECTION_ID | *Selection.id* is invalid. |
| AUD_INCORRECT_TABLE_ID | *Table.Id* is invalid. |
| AUD_OK | The meta data information was retrieved successfully. Note: if one or more *field.ids* are 0, this function will still return. |
| AUD_FAIL | The meta data information could not be found. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Restrictions
The [aud.get.next.action()](aud.get.next.action.md) must be run before this function. This function returns the *table.id* for which the new meta data needs to be retrieved. Note that it is not necessary (although not forbidden) to run [aud.get.field.ids()](aud.get.field.ids.md) if the aud.get.next.action did not indicate that the meta data has changed.

## Related topics
- [Audit management overview](audit_management_overview.md)

- [Audit management synopsis](audit_management_synopsis.md)

- [Audit management examples](audit_management_examples.md)
