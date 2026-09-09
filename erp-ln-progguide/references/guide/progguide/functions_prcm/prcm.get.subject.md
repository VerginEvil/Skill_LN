# prcm.get.subject()

## Syntax:
`function string prcm.get.subject( )`

## Description
Returns the last decoded subject that did a notification.

## Return values
The last decoded subject as string.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Preconditions
- The bms message that was sent to the observer process is expected to be a PRCM notification. This can be tested by calling function [prcm.bms.is.notification()](prcm.bms.is.notification.md). In other words, [prcm.bms.is.notification()](prcm.bms.is.notification.md) must have been called before calling prcm.get.subject() and it should have returned TRUE.

## Related topics
- [Process Change Manager overview](overview.md)

- [Process Change Manager synopsis](synopsis.md)

- [Process Change Manager Code Examples](examples.md)
