# pcm.create()

## Syntax:
`function long pcm.create( [ long flag, long value,... ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This starts the Plan Chart Manager and creates a new chart with the specified attributes. It returns the variable *plan_id*, which is a unique identifier for the chart. You use *plan_id* in the other functions in order to identify the chart you want to work with.

## Arguments
| | | |
|---|---|---|
| `[ long` | `flag ]` |  Use this optional argument to specify the read mode for seq.gets(). Possible values are:  |
| `[ long` | `value,... ]` |  |

## Return values
The function returns a unique ID for the new chart.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Plan Chart Manager overview](overview.md)
- [Plan Chart Manager synopsis](synopsis.md)
- [Plan Chart Manager: example](example.md)
