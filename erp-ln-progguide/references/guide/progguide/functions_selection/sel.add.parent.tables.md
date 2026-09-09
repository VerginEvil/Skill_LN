# sel.add.parent.tables()

## Syntax:
`function boolean sel.add.parent.tables( long group_id, string parent_table )`

## Description
In the Dynamic Form Editor you can already indicate the main table of the parent session for which a session can handle the selection. You should specify that table at the "selection range group" in which the user can specify the range if the selection of the parent session is not used. Because you can only specify one table per group, you need to use this function if you want to add one or more extra tables to a group.

## Arguments
| | | |
|---|---|---|
| `long` | `group_id` |  The number of the group for which you want to add a table. The number can be found in the Dynamic Form Editor  |
| `string` | `parent_table` |  The table code (e.g. tccom100) of which you need to process records.  |

## Return values
true Tables are added for the group with the specified number.
false The supplied arguments are not of the right type, or the group with the specified number doesn't exist.

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1075.
Note  This function is avialable from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 1075](../tiv/tiv_1075.md).

## Related topics
- [Record selection Overview](overview.md)

- [Record selection Synopsis](synopsis.md)

- [Improved Record selection Cookbook](cookbook.md)
