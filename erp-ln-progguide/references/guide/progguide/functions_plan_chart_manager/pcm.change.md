# pcm.change()

## Syntax:
`function void pcm.change( long plan_id, ..., long flag, long value )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
Use this function to change the attributes of a specified chart.

## Arguments
| | | |
|---|---|---|
| `long` | `plan_id, ...` |  The ID of the chart whose attributes you want to change, as returned by [pcm.create()](pcm.create.md).  |
| `long` | `flag` |  Use these arguments to set new values for the chart attributes. For each attribute you specify, you must include the attribute type (for example, PcmPlanName or PcmPlanBackgroundColor), and the attribute value. For a list of the plan attributes, see [pcm.create()](pcm.create.md).  |
| `long` | `value` |  Use these arguments to set new values for the chart attributes. For each attribute you specify, you must include the attribute type (for example, PcmPlanName or PcmPlanBackgroundColor), and the attribute value. For a list of the plan attributes, see [pcm.create()](pcm.create.md).  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Plan Chart Manager overview](overview.md)
- [Plan Chart Manager synopsis](synopsis.md)
