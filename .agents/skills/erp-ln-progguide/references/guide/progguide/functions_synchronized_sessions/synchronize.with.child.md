# synchronize.with.child()

## Syntax:
`function long synchronize.with.child( ref long child.id )`

## Description
This refreshes (that is, resynchronizes) a child session. If the specified child session does not exist, the child.id argument is set to 0 on return.

## Arguments
| | | |
|---|---|---|
| `ref long` | `child.id` |  The unique identifier for the child session to be refreshed, as returned by [start.synchronized.child()](start.synchronized.child.md) or [start.synchronized.child.with()](start.synchronized.child.with.md).  |

## Return values
0: success
< 0: error

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related help topics
- [Synchronized sessions overview](overview.md)

- [Synchronized sessions synopsis](synopsis.md)

- [Child synchronization sample program](example.md)
