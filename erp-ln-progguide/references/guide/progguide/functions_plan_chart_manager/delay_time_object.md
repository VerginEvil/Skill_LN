# PCM_OT_DELAY – delay time object

## Overview
Delay time is a span of time characterized as non-working time – for example, weekends and holidays. It can be indicated in a chart by hatched lines. You must create a PCM_OT_DELAY object for each delay time period you want to include in the chart. The same delay time object can be repeated at regular intervals – to indicate weekends, for example.

## Attributes
| | |
|---|---|
|  PcmDelayStart (double)  | The starting point of the delay time on the time scale.  |
|  PcmDelayFinish (double)  | The end point of the delay time on the time scale.  |
|  PcmDelayRepeat (long)  |  This indicates whether or not the delay time is repeated. The possible values are: true delay time is repeated false delay time occurs only once  |
|  PcmDelayInterval (double)  | If PcmDelayRepeat = true, use this flag to specify the interval at which the delay time must be repeated. The format depends on the division of the time scale.  |

## Related topics
- [Plan Chart Manager overview](overview.md)
- [Plan Chart Manager synopsis](synopsis.md)
- [Plan Chart Manager: example](example.md)
