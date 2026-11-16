# PCM_OT_COLUMN – column object

## Overview
You can define up to nine columns for each chart plan. These columns contain the activity descriptions. The first column you define becomes the leftmost column on the planning board. You must create a PCM_OT_COLUMN object for each column you want to include in the chart.

## Attributes
| | |
|---|---|
| PcmColumnVisible (long) | This indicates whether or not the column is to be visible in the chart plan. The possible values are true and false. |
| PcmColumnName (string) | The title of the column. This is placed over the column. |
| PcmColumnWidth (double) | The column width, expressed in characters (up to 50). |
| PcmColumnIndent (long) | This indicates whether or not the texts relating to subactivities are indented. The possible values are: true texts relating to subactivities are indented false all texts start at the left margin of the column |

## Related topics
- [Plan Chart Manager overview](overview.md)

- [Plan Chart Manager synopsis](synopsis.md)

- [Plan Chart Manager: example](example.md)
