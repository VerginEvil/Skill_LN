# prcm.bms.is.notification()

## Syntax:
`function boolean prcm.bms.is.notification( [ long bms.command ] )`

## Description
Tests whether the specified bms command is a notification of a subject. If no bms command is passed to this function, the predefined 4GL variable `bms.sender.command` is checked.
If the bms command is a notification of a subject then a [bms.receive$()](../functions_interprocess_communication_bshell/bms.receive.md) is done. The received bms message is decoded into a subject and an aspect. The decoced subject and aspect can be retrieved by calling:

- [prcm.get.subject()](prcm.get.subject.md)

- [prcm.get.aspect()](prcm.get.aspect.md)

## Arguments
| | | |
|---|---|---|
| `[ long` | `bms.command ]` |  Optional bms command that must be checked to see whether it represents a notification of a subject. If not specified the predefined bms.sender.command variable is checked  |

## Return values
This function returns TRUE if the tested bms command represents a PRCM notification. Otherwise FALSE is returned.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Process Change Manager overview](overview.md)

- [Process Change Manager synopsis](synopsis.md)

- [Process Change Manager Code Examples](examples.md)
