# java.new.queue

## Syntax:
`function long java.new.queue( )`

## Description
Creates a new queue for buckets. Upon return, the new queue.id is returned, or an error code is presented. NOTE: queues are removed automatically if the process that created it (or the process that called java.install.listener(…) on that queue) is finished !! See also the 3GL function java.install.listener.

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Return codes
| | |
|---|---|
| > 0 | id for the newly created Java queue |
| -1 | :JavaVM not supported on this platform |
| -2 | Java virtual machine could not be started (resource problems). |
| -4 | failed to create the Java queue. |

## Example
```

long queue.id

queue.id = java.new.queue()
if queue.id > 0 then
	| do something useful
	java.destroy.queue( queue.id )
endif
```

## Related topics
- [Java VM integration - Infor Enterprise Server 3GL](overview.md)
