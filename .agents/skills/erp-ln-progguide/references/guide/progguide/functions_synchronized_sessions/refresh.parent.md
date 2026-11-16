# refresh.parent()

## Syntax:
`function long refresh.parent( long occurrence )`

## Description
This refreshes the parent session of the current session. The occurrence parameter determines which ocurrence of the child session must be refreshed in the parent session.
If -1 is passed to this function, the parent session will refresh all its occurrences.

## Arguments
| | | |
|---|---|---|
| `long` | `occurrence` |  The occurrence that must be refreshed in the parent session. If the child session is a details session, this is occurrence 1. In case the child session is an overview session, then any number between 1 and the number of occurrences displayed (filled.occ) can be given. If you specify -1, then the parent session will refresh all its occurrences.  |

## Return values
0 The parent is refreshed
-1 No parent process
-2 Invalid occurrence specified

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related help topics
- [Synchronized sessions overview](overview.md)

- [Synchronized sessions synopsis](synopsis.md)
