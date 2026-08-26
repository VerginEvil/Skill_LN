# PCM_OT_ACTIVITY – activity object

## Overview
An activity is an event or series of events with a start and end time. There are parent activities and subactivities. A parent activity can be an independent activity within a project or it can have one or more subactivities. Subactivities are always linked to a parent activity. Activities can be repeated in the plan chart.
An activity consists of the following parts:
- part reported completed
- part still to be executed
- lower margin – that is, the number of time units the activity may start earlier that the defined start time
- upper margin – that is, the number of time units by which the end time of the activity may be exceeded  You must create a PCM_OT_ACTIVITY object for each activity you want to include in the chart.

## Attributes
| | |
|---|---|
|  PcmActivityParent (long)  | The object ID of the activity's parent activity. The parent ID of a parent activity is 0.  |
|  PcmActivityBrother (long)  | An activity can occur several times in one project (repeated activity). The activity is placed several times on the same line, each time shifted in time. In this flag, specify the object ID of the activity that is to be repeated.  |
|  PcmActivityGroup (long)  | By grouping activities, you can assign different colors to different groups of activities. You can define up to nine activity groups. Use this attribute to specify the group number for the activity.  |
|  PcmActivityStart (double)  | The starting point of the activity on the time scale.  |
|  PcmActivityFinish (double)  | The end point of the activity on the time scale.  |
|  PcmActivityProgress (double)  | The part of the activity reported completed (as a percentage).  |
|  PcmActivityFreeStart (double)  | The starting point of the free float of this activity as a value on the time scale. This value should be less than or equal to PcmActivityStart. The free float is the degree to which an activity can be moved in time without influencing the start or end time of other activities.  |
|  PcmActivityFreeFinish (double)  | The end point of the free float of this activity as a value on the time scale. This value should be less than or equal to PcmActivityFinish.  |
|  PcmActivityTotalStart (double)  | The starting point of the total float of this activity as a value on the time scale. This value should be less than or equal to PcmActivityStart. The total float is the degree to which an activity may be moved in time without influencing the start or end time of the entire project.  |
|  PcmActivityTotalFinish (double)  | The end point of the total float of this activity as a value on the time scale. This value should be less than or equal to PcmActivityFinish.  |
|  PcmActivityText1 PcmActivityText9 (string)  | An explanatory text for the activity. This is displayed in the specified column. You can create as many texts (per activity) as there are columns. See also [PCM_OT_COLUMN – column object](column_object.md).  |
|  PcmActivitySort (string)  | Activities can be sorted (for example, by start time). Use this to specify the string by which they must be sorted.  |
|  PcmActivityCritical (long)  |  This flag indicates if the activity is part of the critical path. The critical path is the longest route between the start and end of the project. Any change in one of the activities or relations that are part of the critical path directly influences the project's end time. The possible values are: true the activity is part of the critical path false the activity is not part of the critical path  |
|  PcmActivityExpand (long)  |  This flag determines if subactivities are shown on the plan chart. The possible values are: PCM_EM_EXPAND show subactivities PCM_EM_NOEXPAND do not show subactivities PCM_EM_TOGGLE toggle between EXPAND and NOEXPAND  |
|  PcmActivityEdit (long)  |  This flag determines whether or not users are authorized to modify or move the activity. The possible values are: PCM_ED_NOEDIT The user is not authorized to change or shift the activity in time. PCM_ED_START The user is authorized to shift the entire activity in time. This is done by dragging the start point of the activity with the mouse. PCM_ED_FINISHThe user is authorized to shorten or lengthen the activity. This is done by dragging the end point of the activity with the mouse. You can combine PCM_ED_START + PCM_ED_FINISH in order to authorize users to both shift and change activities.  |

## Related topics
- [Plan Chart Manager overview](overview.md)
- [Plan Chart Manager synopsis](synopsis.md)
- [Plan Chart Manager: example](example.md)
