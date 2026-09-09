# prcm.unregister()

## Syntax:
`function void prcm.unregister( const string subject, [ string aspect(32) ] )`

## Description
Is called by an Observer process (i.e. the current process) to unregister/unsubscribe itself for a certain Subject (and optionally Aspect). Afterwards, this process will no longer be notified by the Process Change Manager if the subject tries to notify its observers.

## Arguments
| | | |
|---|---|---|
| `const string` | `subject` |  The subject in which the current process is interested.  |
| `[ string` | `aspect(32) ]` |  Optional aspect in which the current process is interested.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Process Change Manager overview](overview.md)

- [Process Change Manager synopsis](synopsis.md)

- [Process Change Manager Code Examples](examples.md)
