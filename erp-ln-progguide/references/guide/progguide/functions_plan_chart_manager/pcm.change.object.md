# pcm.change.object()

## Syntax:
`function void pcm.change.object( long plan_id, long object_id, [ long flag, long value, ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
Use this function to change the attributes of an object that was created by [pcm.create.object()](pcm.create.object.md).

## Arguments
| | | |
|---|---|---|
| `long` | `plan_id` |  The ID of the chart to which the object belongs, as returned by [pcm.create()](pcm.create.md).  |
| `long` | `object_id` |  The ID of the object, as returned by [pcm.create.object()](pcm.create.object.md).  |
| `[ long` | `flag ]` |  Use these arguments to set new values for the object's attributes. For each attribute you specify, you must include the attribute type (for example, PcmMenuName or PcmTimescaleVisible), and the attribute value. For a list of the object attributes, see [pcm.create.object()](pcm.create.object.md).  |
| `[ long` | `value, ]` |  Use these arguments to set new values for the object's attributes. For each attribute you specify, you must include the attribute type (for example, PcmMenuName or PcmTimescaleVisible), and the attribute value. For a list of the object attributes, see [pcm.create.object()](pcm.create.object.md).  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Plan Chart Manager overview](overview.md)
- [Plan Chart Manager synopsis](synopsis.md)
