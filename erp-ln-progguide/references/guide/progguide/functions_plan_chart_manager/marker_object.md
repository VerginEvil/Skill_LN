# PCM_OT_MARKER – marker object

## Overview
You can place markers on the planning board to indicate when certain standard actions must take place – for example, "Principal's Approval". Markers are defined at a specific point in time. You must create a PCM_OT_MARKER object for each marker you want to include in the chart.

## Attributes
| | |
|---|---|
| PcmMarkerActivity (long) | The object ID of the activity that must be marked. |
| PcmMarkerType (long) | The marker type. The possible values are: PCM_MT_RECTANGLE PCM_MT_TRIANGLE PCM_MT_DIAMOND PCM_MT_STAR PCM_MT_ARROW |
| PcmMarkerStart (double) | The time where the marker is to be placed. |
| PcmMarkerText (string) | A text explaining the marker. |
| PcmMarkerEdit (long) | This flag determines whether or not users can move the marker. The possible values are: PCM_ED_NOEDIT The user is not authorized to shift this marker in time. PCM_ED_START The user is authorized to shift this marker in time. This is done by dragging the starting point with the mouse. |
| PcmMarkerGroup (long) | By grouping markers, you can assign different colors to different groups of markers. You can define up to three marker groups. Use this attribute to specify the group number for this marker. |

## Related topics
- [Plan Chart Manager overview](overview.md)

- [Plan Chart Manager synopsis](synopsis.md)

- [Plan Chart Manager: example](example.md)
