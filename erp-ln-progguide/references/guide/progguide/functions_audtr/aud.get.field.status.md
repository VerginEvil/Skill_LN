# aud.get.field.status()

## Syntax:
`function string aud.get.field.status( long selection.id, long table.id, long field.id )`

## Description
Retrieves the status of a field in a database action (insert, update or delete).
The status can be one of the following values:
| | |
|---|---|
| X |  Not available (insert, update or delete) This either means the field does not exist, or it was not logged because this was specified in the data model, or (in case of an update) it was not logged because it has not changed  |
| Y (changed) | Depending on Action Type: old value available (delete), new value available (insert), both old and new value available, value has changed (update)  |
| N (not changed) | Value has not changed, yet both old and new values are available (update).  |
The following table shows the status in all cases that might occur:
| | | | | |
|---|---|---|---|---|
| Action Type | Field in Audit DD | Field Changed | Field Logged | Status |
| I | Yes | Yes | Yes | Y |
| I | No | - | - | X |
| D | Yes | Yes | Yes | Y |
| D | No | - | - | X |
| U | Yes | Yes | Yes | Y |
| U | Yes | No | Yes | N |
| U | Yes | No | No | X |
| U | No | - | - | X |

## Arguments
| | | |
|---|---|---|
| `long` | `selection.id` |  Id of the selection, as provided by aud.select.transactions  |
| `long` | `table.id` |  Id of the table on which the action occurred, which is used to retrieve the detailed action data using function [aud.get.field.status()](aud.get.field.status.md), [aud.put.old.field.value()](aud.put.old.field.value.md), and [aud.put.new.field.value()](aud.put.old.field.value.md). This id is also used to get the meta data information, in case it has been changed.  |
| `long` | `field.id` |  Identifier for a field, as retrieved using the functions aud.get.field.ids() or aud.get.field.list(). Note: if field.id = 0 (the field does not exist) status "X" is returned.  |

## Return values
See description.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Restrictions
This function will not check the input, because of performance reasons. Instead the combination of *selection.id*, *table.id*, *field.id* is assumed to refer to an existing field, as returned by [aud.get.field.ids()](aud.get.field.ids.md). This means that if the arguments are not valid, an error message will be presented to the end user.
During the last aud.get.next.action for this selection, an *action.type* must have been returned that is 'I', 'U' or 'D'. If the action is a table operation ('C', 'L' or 'R') the status of a field has no meaning and therefore this function cannot be used.

## Related topics
- [Audit management overview](audit_management_overview.md)
- [Audit management synopsis](audit_management_synopsis.md)
- [Audit management examples](audit_management_examples.md)
