# change.progress.delay()

## Syntax:
`function void change.progress.delay( long delay )`

## Description
Changes the delay time of the progress indicator. The delay time is the time in milliseconds after which the progress indicator will appear to the user. This can be used to prevent flashing progress indicators, in case the number of elements to process is low, (i.e. a progress indicator that starts and stops within one or two seconds). By setting the delay time this flashing can be prevented.

## Arguments
| | | |
|---|---|---|
| `long` | `delay` |  The time in milliseconds that must have elapsed before the progress indicator will appear. This time starts counting when [create.progress.indicator()](create.progress.indicator.md) is called.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Progress indicators overview and synopsis](overview_and_synopsis.md)

- [Progress indicators sample program](example.md)
