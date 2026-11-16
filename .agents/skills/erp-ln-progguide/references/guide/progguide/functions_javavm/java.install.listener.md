# java.install.listener

## Syntax:
`function long java.install.listener( long Queue.id, [ long become.owner ] )`

## Description
Installs a listener at the Infor Enterprise Server side. Whenever a message arrives on the queue specified by queue.id, the 3GL process will be notified by an EVT_CHANNEL_EVENT event. For installation of a listener at the Java side, see the Java IQueueListener interface definition.

## Arguments
| | | |
|---|---|---|
| `long` | `Queue.id` |  id of the queue  |
| `[ long` | `become.owner ]` |  *1* (default) the 3GL process becomes the new owner of the queue itself. This basically means the queue will be removed whenever the 3GL process that called this function exits. *0*: the process will NOT become the new owner of this queue. The queue is removed automatically when the 3GL process that called java.new.queue exits.  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Return codes
| | |
|---|---|
| 0 | upon success |
| -1 | JavaVM not supported on this platform |
| -4 | incorrect queue ID |
| -5 | unable to install the listener on the queue |
Note  The listener will immediately start processing buckets, including the buckets already present within the queue.

## Related topics
- [Java VM integration - Infor Enterprise Server 3GL](overview.md)
