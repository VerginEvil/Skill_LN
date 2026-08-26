# start.synchronized.child()

## Syntax:
`function long start.synchronized.child( string sess_code, [ string parent.var child.var, long start.mode ] )`

## Description
Use this to synchronize two sessions that act on different main tables. The function starts the specified child session when the user chooses a particular form command in the multioccurrence parent session. The primary key of the parent's main table must be a subset of the primary key of the child's main table.
Although you normally use this function to synchronize sessions that act on different main tables, it is also possible to use it to synchronize sessions that act on the same main table.

## Arguments
| | | |
|---|---|---|
| `string` | `sess_code` |  The session code of the child session.  |
| `[ string` | `parent.var child.var ]` |  These are optional arguments. You use them to synchronize particular variables in the parent and child sessions. For example, to display in the child session only order lines for the order currently selected in the parent session. For each variable to be synchronized, specify the name of the relevant field in the parent's main table, followed by the name of the corresponding field in the child’s main table. For each synchronization event ( *start.synchronized.child()*, [start.synchronized.child.with()](start.synchronized.child.with.md), or [synchronize.with.child()](synchronize.with.child.md)), the child session is refreshed, and the specified variables derive their values from the parent session.  |
| `[ long` | `start.mode ]` |  When SINGLE_OCC is specified behind the pairs of fields, the specified session will be started in, details mode. Default the session will be started in MULTI_OCC.  |

## Return values
> 0 a unique identifier for the child process
0 cannot start child
-1 argument error

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2120 and Value of argument sess_code starts with "tx" or "otx" and no optional argumens are used

## Related help topics
- [Synchronized sessions overview](overview.md)
- [Synchronized sessions synopsis](synopsis.md)
- [Child synchronization sample program](example.md)
