# change.progress.indicator()

## Syntax:
`function long change.progress.indicator( long perc, [ string message, ... ] )`

## Description
This changes the value of the progress indicator.

## Arguments
| | | |
|---|---|---|
| `long` | `perc` |  A value in the range 0 – 100. This indicates the percentage of completion of the operation.  |
| `[ string` | `message, ... ]` |  This optional argument displays a string that provides information about the progress of the operation. For example, if the process involves multiple stages, you could add a short description of each stage to the progress indicator. If you include more than one message argument, each successive message is displayed below the previous one. A subsequent call to change.progress.indicator() may not give less messages than the first one.  |

## Return values
| | |
|---|---|
| 0 | No signal sent. |
| PROGRESS.STOP | Stop button pressed. Function must stop. |
| PROGRESS.CANCEL | Cancel button pressed. Function must stop and cancel any changes made. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Progress indicators overview and synopsis](overview_and_synopsis.md)
- [Progress indicators sample program](example.md)
