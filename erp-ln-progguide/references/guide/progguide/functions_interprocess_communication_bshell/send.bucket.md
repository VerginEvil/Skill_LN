# send.bucket()

## Syntax:
`function long send.bucket( long processno, string bucket )`

## Description
This sends a bucket message to a specified process. If the specified process is sleeping, it is automatically started. It can retrieve the message by calling [receive.bucket$()](receive.bucket.md).

## Arguments
| | | |
|---|---|---|
| `long` | `processno` |  The process ID of the process to which the message must be sent, as returned by functions such as [activate()](../functions_processes/activate.md) and [act.and.sleep()](../functions_processes/act.and.sleep.md). In subprocesses, the predefined variable *parent* indicates the process ID of the parent process.  |
| `string` | `bucket` |  The message string.  |

## Return values
> 0: the process ID of the called process
-1: error

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Interprocess communication (OS level) overview](../functions_interprocess_communication_os_level/overview.md)

- [Interprocess communication (bshell) overview](overview.md)

- [Interprocess communication (bshell) synopsis](synopsis.md)
