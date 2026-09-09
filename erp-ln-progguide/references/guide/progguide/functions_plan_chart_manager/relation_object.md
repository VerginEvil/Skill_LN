# PCM_OT_RELATION – relation object

## Overview
On the planning board you can record relations between different activities and/or markers. These relations define the mutual relationships between such objects. You can record, for instance, that certain activities must be completed before another activity can start. Also, two related activities can be separated by a mandatory interval (for example, if a coat of paint must dry for two days before the next activity can take place) or they can overlap.
You must create a PCM_OT_RELATION object for each relation you want to include in the chart.
The Plan Chart manager supports the following relation types:
| | |
|---|---|
| start-start | Activity 1 can start as soon as activity 2 has started. |
| start-end | Activity 1 can start only when activity 2 is completed. |
| end-start | Activity 2 can start when activity 1 is completed. |
| end-end | Activity 2 can end only when activity 1 is completed. |

## Attributes
| | |
|---|---|
| PcmRelationObject1 (long) | This specifies the object ID of object 1. |
| PcmRelationObject2 (long) | This specifies the object ID of object 2. |
| PcmRelationGroup (long) | By grouping relations, you can assign different colors to different groups of relations. You can define up to nine relation groups. Use this attribute to specify the group number for this relation. |
| PcmRelationType (long) | The relation type. The possible values are: PCM_RT_STARTSTART PCM_RT_STARTEND PCM_RT_ENDSTART PCM_RT_ENDEND |
| PcmRelationDelay (double) | The time span between the two related activities. This number is placed alongside the line that indicates the relationship (this can also be a negative value). |
| PcmRelationCritical (long) | This flag indicates if the relation is part of the critical path. The critical path is the longest route between the start and end of the project. Any change in one of the activities or relations that are part of the critical path directly influences the project's end time. The possible values are: true the activity is part of the critical path false the activity is not part of the critical path |

## Related topics
- [Plan Chart Manager overview](overview.md)

- [Plan Chart Manager synopsis](synopsis.md)

- [Plan Chart Manager: example](example.md)
