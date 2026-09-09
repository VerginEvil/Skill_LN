# PCM_OT_TIMESCALE – time scale object

## Overview
A plan chart represents a projection of activities on a time scale. An efficient time scale is essential in order to make the chart as clear as possible. To divide the time scale, you require a base unit. In the Plan Chart Manager, any time unit, from seconds to years, can be used as the base unit. In practice, the base unit is usually one day.
You can define several time scales for each plan chart. You must create a PCM_OT_TIMESCALE object for each of the time scales included in the chart. You specify start and end dates for the time scale with the function [pcm.create()](pcm.create.md). These can, for example, be specified as the number of days since 01-01-0001.
The following predefined variables are available for PCM_OT_TIMESCALE objects.
| | |
|---|---|
| PCM_DAYNO | The number of days since 01-01-0001. |
| PCM_WEEKDAYNO | The day number in the week (1 to 7). |
| PCM_WEEKNO | The week number in the year (0 to 53). |
| PCM_MONTHDAYNO | The day number in the month (1 to 31). |
| PCM_MONTHNO | The month number in the year (1 to 12). |
| PCM_YEARNO | The day number in the year (1 to 366). |

## Attributes
| | |
|---|---|
| PcmTimescaleVisible (long) | This flag indicates if the time scale must be visible on the planning board. The possible values are true and false. |
| PcmTimescaleDesc (string) | The format of the description on the time scale – for example, month numbers, day numbers, and so on. See [sprintf$()](../functions_formatting_io/sprintf.md). |
| PcmTimescaleExprV (string) | This expression determines how the time scale must be divided and where the ticks indicating the divisions must be placed. |
| PcmTimescaleExprD (string) | This expression determines the value by which the substitution symbol specified in PcmTimescaleDesc must be replaced – for example, a day number. |
| PcmTimescaleInterval (double) | The interval for the time scale division. |

## Example
```

Base Unit: Day
Time Scale Division: Week Numbers

pcm.create.object ( plan_id, PCM_OT_TIMESCALE,
    PcmTimescaleVisible, TRUE,
    PcmTimescaleDesc, "Week %D(%w)",
          PcmTimescaleExprV, "PCM_WEEKDAYNO = 1",
    PcmTimescaleExprD, "PCM_DAYNO",
    PcmTimescaleInterval, 1 )
```
In this example, the starting point of the time scale is a number representing the number of days since 01-01-0001. At each division, the Plan Chart Manager increments this value (ExprD) by 1 (Interval) and checks if this day coincides with the start date of a week (ExprV). If the latter expression is true, a mark is placed on the time scale containing a week number. In fact, if ExprV is true, the following statement is executed:
```

sprintf$(PcmTimescaleDesc, PcmTimescaleExprD)
```
that is,
```

sprintf$("Week %D(%wer)", PCM_DAYNO)
```

## Related topics
- [Plan Chart Manager overview](overview.md)

- [Plan Chart Manager synopsis](synopsis.md)

- [Plan Chart Manager: example](example.md)
