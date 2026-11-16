# pcm.destroy.object()

## Syntax:
`function void pcm.destroy.object( long plan_id, long object_id )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This deletes the specified object.

## Arguments
| | | |
|---|---|---|
| `long` | `plan_id` |  The ID of the chart to which the object belongs, as returned by [pcm.create()](pcm.create.md).  |
| `long` | `object_id` |  The ID of the object, as returned by [pcm.create.object()](pcm.create.object.md).  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Plan Chart Manager overview](overview.md)

- [Plan Chart Manager synopsis](synopsis.md)

- [Plan Chart Manager: example](example.md)
