# stop.synchronized.child()

## Syntax:
`function long stop.synchronized.child( long child.id )`

## Description
This ends a child session.

## Arguments
| | | |
|---|---|---|
| `long` | `child.id` |  The unique identifier for the child session to be stopped, as returned by [start.synchronized.child()](start.synchronized.child.md) or [start.synchronized.child.with()](start.synchronized.child.with.md).  |

## Return values
0: success
< 0: error

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related help topics
- [Synchronized sessions overview](overview.md)

- [Synchronized sessions synopsis](synopsis.md)

- [Child synchronization sample program](example.md)
