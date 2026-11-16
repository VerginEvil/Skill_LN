# pcm.get.data()

## Syntax:
`function void pcm.get.data( long evt_type, ref string arglist,... )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
When the client application receives an event from the Plan Chart Manager, use this function to read the event.

## Arguments
| | | |
|---|---|---|
| `long` | `evt_type` |  This specifies the type of the event you want to read.  |
| `ref string` | `arglist,...` |  This returns the argument list.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Plan Chart Manager overview](overview.md)

- [Plan Chart Manager synopsis](synopsis.md)

- [Plan Chart Manager: example](example.md)
