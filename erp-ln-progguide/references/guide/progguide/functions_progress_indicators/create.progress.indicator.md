# create.progress.indicator()

## Syntax:
`function long create.progress.indicator( string title, [ long mode ] )`

## Description
This creates a progress indicator with the specified title displayed in its title bar. The progress indicator is activated after the first update (using [change.progress.indicator()](change.progress.indicator.md)). It is removed again using [destroy.progress.indicator()](destroy.progress.indicator.md), or automatically if PROGRESS.NOAUTODESTROY is not specified.
Only one progress indicator can be active at the same time. If this function is not successful, then it is not allowed to change or destroy the progress indicator.

## Arguments
| | |
|---|---|
| PROGRESS.BAR | Create a progress bar. |
| PROGRESS.STOP | Add a Stop button to the progress bar window. The user can click on this button to stop the operation; changes already made are not canceled. |
| PROGRESS.CANCEL | Add a Cancel button to the progress bar window. The user can click on this button to stop the operation; any changes already made are canceled. |
| PROGRESS.NOAUTODESTROY | The progress bar window is not automatically destroyed when the progress bar value changes to 100%, or when the user clicks Stop or Cancel, or closes the indicator. |

## Return values
| | |
|---|---|
| 0 | Success |
| -1 | Error |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Progress indicators overview and synopsis](overview_and_synopsis.md)

- [Progress indicators sample program](example.md)
