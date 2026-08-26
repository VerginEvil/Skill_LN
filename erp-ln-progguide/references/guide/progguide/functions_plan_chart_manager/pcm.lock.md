# pcm.lock()

## Syntax:
`function void pcm.lock( long plan_id, long lock )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
Use this function to lock and unlock the Plan Chart Manager (for example, when data is changed in a session).

## Arguments
| | | |
|---|---|---|
| `long` | `plan_id` |  The ID of the planning chart that you want to lock.  |
| `long` | `lock` |  This indicates whether the planning chart must be locked or unlocked. The possible values are: true The planning board is locked. The user cannot interact with it until it is unlocked again. false The planning board is unlocked. This is the default value.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Plan Chart Manager overview](overview.md)
- [Plan Chart Manager synopsis](synopsis.md)
- [Plan Chart Manager: example](example.md)
