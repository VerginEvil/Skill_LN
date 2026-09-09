# pcm.activate.session()

## Syntax:
`function long pcm.activate.session( ref string session, string title )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This starts a specified 4GL session. It generates a new window for the session and ensures that it is handled correctly. You can use this function in combination with [pcm.send.bms.event()](pcm.send.bms.event.md), which sends changed values back to the application as events.

## Arguments
| | | |
|---|---|---|
| `ref string` | `session` |  The session code.  |
| `string` | `title` |  The title for the session window.  |

## Return values
The function returns the process ID of the activated session.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
See [pcm.send.bms.event()](pcm.send.bms.event.md)

## Related topics
- [Plan Chart Manager overview](overview.md)

- [Plan Chart Manager synopsis](synopsis.md)
