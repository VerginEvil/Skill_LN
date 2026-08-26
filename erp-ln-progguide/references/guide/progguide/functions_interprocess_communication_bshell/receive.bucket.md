# receive.bucket$()

## Syntax:
`function string receive.bucket$( long processno )`

## Description
This waits for a bucket message to be sent to the calling process by another process. It then returns that message. The *processno* argument returns the process ID of the sending process.

## Arguments
| | | |
|---|---|---|
| `long` | `processno` |  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Interprocess communication (OS level) overview](../functions_interprocess_communication_os_level/overview.md)
- [Interprocess communication (bshell) overview](overview.md)
- [Interprocess communication (bshell) synopsis](synopsis.md)
