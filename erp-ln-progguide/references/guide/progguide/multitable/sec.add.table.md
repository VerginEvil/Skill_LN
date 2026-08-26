# sec.add.table()

## Syntax:
`function long sec.add.table( const string tablename(), ... )`

## Description
Add the passed table as a secondary table to the current session. This function call is only allowed from the `before.program` section.

## Arguments
| | | |
|---|---|---|
| `const string` | `tablename()` |  The table name to be added.  |
| `` | `...` |  (optional) pairs of parameters of type string which defines the mapping of maintable fields on secondary table keyfields. First string of pair: maintable field Second string of pair: secondary table field  |

## Return values
The `id` of the secondary table. This id must be used in subsequent calls to the functions [sec.add.set()](sec.add.set.md), [sec.get.update.status()](sec.get.update.status.md), [sec.mark.delete()](sec.mark.delete.md) and [sec.record.exists()](sec.record.exists.md).

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1075.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
We have two situations:
1. In program script all tables can be used as secondary table.
2. In extension-script only 'tx' tables can be used.
Note:  This function does not add table-fields to the session.
As extension, use option Secondary Table of the Extension Modeler for non 'tx' sessions.

## Related topics
- [Multi Table Overview](overview.md)
- [Multi Table synopsis](synopsis.md)
