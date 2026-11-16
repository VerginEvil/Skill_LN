# substitute.session()

## Syntax:
`function long substitute.session( long old.pid, string new.session, long new.pid, [ void... ] )`

## Description
This function overlays (substitutes) one session with another. The old session will be no longer visible and the new session will be placed on the same position with exactly the same dimensions.

## Arguments
| | | |
|---|---|---|
| `long` | `old.pid` |  The process id of the process that should be substituted.  |
| `string` | `new.session` |  The session code of the new session that should be started or reactivated.  |
| `long` | `new.pid` |  The process id of the session that should be reactivated. If the value is not a valid process id or if the session code of the process doesn't match with *new.session*, the session with session code *new.session* is started.  |
| `[ void` | `... ]` |  Arguments that should be passed to the new session.  |

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Return Value
The process id of the new started process.

## Related topics
- [Substitute session overview](overview.md)

- [Synchronized sessions synopsis](synopsis.md)

- [Substitute session sample program](example.md)
