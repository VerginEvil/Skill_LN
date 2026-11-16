# pcm.create()

## Syntax:
`function long pcm.create( [ long flag, long value,... ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This starts the Plan Chart Manager and creates a new chart with the specified attributes. It returns the variable *plan_id*, which is a unique identifier for the chart. You use *plan_id* in the other functions in order to identify the chart you want to work with.

## Arguments
| | |
|---|---|
| PcmPlanName(50) (string) | The title of the chart. |
| PcmPlanFontHeight (long) | The size of the font used in the chart. |
| PcmPlanLineHeight (double) | The distance between the lines/activities. |
| PcmPlanBackgroundColor (long) | The background color for the chart. |
| PcmPlanForegroundColor (long) | The foreground color for the chart. |
| PcmPlanProgressColor (long) | The color for the part of an activity that has been reported as completed. |
| PcmPlanActivityColor1 - PcmPlanActivityColor9 (long) | Use these to define the colors for activity groups. You can define up to nine activity groups, and assign a different color to each. |
| PcmPlanRelationColor1 - PcmPlanRelationColor9 (long) | Use these to define the colors for relation groups. You can define up to nine relation groups, and assign a different color to each. |
| PcmPlanMarkerColor1 -PcmPlanMarkerColor3 (long) | Use these to define the colors for marker groups. You can define up to three marker groups, and assign a different color to each. |
| PcmPlanCriticalColor (long) | The color for an activity or relation that is part of the critical path. |
| PcmPlanTimescaleStart (double) | The starting point of the time scale. Specify a number that you translate into a date or time value when dividing the time scale. |
| PcmPlanTimescaleFinish (double) | The end point of the time scale. |
| PcmPlanTimescaleWidth (double) | The width (number of characters) of each time unit on the time scale. |
| PcmPlanFreeTimeVisible (long) | This indicates if the float must be displayed in the chart. The possible values are true or false. |
| PcmPlanCriticalVisible (long) | Activities and relations that are part of the critical path can be shown in a particular color. This flag indicates if the critical path must be displayed in the chart. The possible values are true or false. |
| PcmPlanDelaysVisible (long) | You can define lay-offs, holidays, and weekends as non-workdays and the Plan Chart Manager then takes this into account. This flag indicates if non-workdays must be shown hatched or not. The possible values are true or false. |
| PcmPlanCriticalVisible (long) | You can define relations between different objects by means of lines on the planning board. This flag indicates if the relations must be visible. The possible values are true or false. |
| PcmPlanRelationsStraight (long) | true a relation is represented by a straight line between two objects. false a relation is represented by lines at right angles or parallel to the objects |
| PcmPlanMarkersVisible (long) | You can add a marker to an activity in order to plan certain standard actions – for example, "Principal's Approval". This flag indicates if such markers must be visible in the planning board. The possible values are true or false. |

## Return values
The function returns a unique ID for the new chart.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Plan Chart Manager overview](overview.md)

- [Plan Chart Manager synopsis](synopsis.md)

- [Plan Chart Manager: example](example.md)
