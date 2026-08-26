# plcm.create.legend.entry

## Syntax:
`function long plcm.create.legend.entry( string legend.id, long color, string description )`

## Description
Defines a legend entry. This function must be called before the plcm.start() is called. The legend will be visualized in the underneath the plan chart.

## Arguments
| | | |
|---|---|---|
| `string` | `legend.id` |  ID of the activity.  |
| `long` | `color` |  One of the following constants: PLCM_RED, PLCM_LIGHTRED, PLCM_BLUE, PLCM_DARKBLUE, PLCM_GREEN, PLCM_LIGHTGREEN, PLCM_ORANGE, PLCM_YELLOW, PLCM_PURPLE, PLCM_BACKGROUND PLCM_BACKGROUND is avialable from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 2140](../tiv/tiv_2140.md)  |
| `string` | `description` |  The description (meaning) of the legend  |

## Return values
| | |
|---|---|
| 0 | Success |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Synopsis](synopsis.md)
- [Example](example.md)
