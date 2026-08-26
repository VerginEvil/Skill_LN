# prcm.get.data()

## Syntax:
`function long prcm.get.data( )`

## Description
Returns the last data passed by the subject that did a notification.

## Return values
| | |
|---|---|
| <> 0 | The id of the passed data |
| 0 | When no data was passed with the last PRCM notification |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Preconditions
- The bms message that was sent to the observer process is expected to be a PRCM notification. This can be tested by calling function [prcm.bms.is.notification()](prcm.bms.is.notification.md). In other words, [prcm.bms.is.notification()](prcm.bms.is.notification.md) must have been called before calling prcm.get.data() and it should have returned TRUE.

## Related topics
- [Process Change Manager overview](overview.md)
- [Process Change Manager synopsis](synopsis.md)
- [Process Change Manager Code Examples](examples.md)
