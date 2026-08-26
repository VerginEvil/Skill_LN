# send.wait()

## Syntax:
`function long send.wait( ref long processno, string bucket )`

## Description
This sends a bucket message to a specified process and waits for a reply. The receiving process must send a reply by using [send.bucket()](send.bucket.md) or *send.wait()*. Note that the waiting process cannot receive any message string contained in the reply.

## Arguments
| | | |
|---|---|---|
| `ref long` | `processno` |  The process ID of the process to which the message must be sent, as returned by functions such as [activate()](../functions_processes/activate.md) and [act.and.sleep()](../functions_processes/act.and.sleep.md). In subprocesses, the predefined variable *parent* indicates the process ID of the parent process. Note that the actual process id returning the message will be returned in argument *processno*.  |
| `string` | `bucket` |  The message string.  |

## Return values
> 0: the process ID of the process that sends the reply
-1: error

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  *send.wait()* is used to synchronize two processes. When a reply is sent with *send.bucket()* the processes appear to run simultaneously.
When a process that is waiting for a reply from one process receives a message from another process, it is wakened automatically and the data sent is lost.

## Example
```

Process 1:
long process
process = activate("process2")
send.bucket(process, "")    | This is the reply, data can not be
                                                            |
received in process 2

Process 2:
long parent_process
parent_process = process
| Note: first argument of send.wait is a ref!
send.wait(parent_process, "I am waiting for a reply")
```

## Related topics
- [Interprocess communication (OS level) overview](../functions_interprocess_communication_os_level/overview.md)
- [Interprocess communication (bshell) overview](overview.md)
- [Interprocess communication (bshell) synopsis](synopsis.md)
