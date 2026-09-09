# bms.send()

## Syntax:
`function long bms.send( string broadcast, long level_or_evt, string mask, long processno, [ long no.bytes ] )`

## Description
Use this to send a broadcast message to one or more processes.

## Arguments
| | | |
|---|---|---|
| `string` | `broadcast` |  The message that must be sent.  |
| `long` | `level_or_evt` |  Use this either to specify a level for the message (1 or 2, for example) or to specify an event array with the following information: evt.type( event ) this is always EVTBUCKETMESSAGE evt.bms.sender( event ) sender ID (this is filled automatically) evt.bms.command( event ) command ID evt.bms.argument( event ) some argument The specified event is sent to each process to which the broadcast message is sent.  |
| `string` | `mask` |  If you specify a mask in this argument, the message is sent to all processes to which that mask has been added. If you also specify a process ID in the *processno* argument, the process is sent only to the specified process.  |
| `long` | `processno` |  If you specify a process ID in this argument, the broadcast message is sent only to that process. If you specify 0 for this argument, the *mask* argument is used to determine the processes to which the message is sent.  |
| `[ long` | `no.bytes ]` |  The size of the broadcast message, in bytes.  |

## Return values
0: error
> 0: the process ID of the last process to which the broadcast message was sent

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  If *bms.send()* specifies a mask and no processes have that mask set, the file ‘$BSE/lib/bms_mask’ is searched for a line beginning with the mask name. Lines in this file have the following syntax:
`<mask>:<process>:<y/n>:[boot]`
When a line is found that begins with the specified mask, the process specified in that line is started. If the line contains ‘y’, the mask is automatically added to the process. The broadcast message and event are then sent to the process. If the line contains ‘n’, the mask is not added to the process and so the process does not receive the message and event. If the line ends with the word ‘boot’, the specified process is always started automatically before any other process when the bshell starts. For example:
```

| suppose the file '$BSE/lib/bms_mask' contains the following line:

| calculator:ottstpcalc:y

long event(EVTMAXSIZE), bms_id

bms_id = bms.send( "", event, "calculator", 0 )
```

## Related topics
- [Events overview](../events/overview.md)

- [Interprocess communication (OS level) overview](../functions_interprocess_communication_os_level/overview.md)

- [Interprocess communication (bshell) overview](overview.md)

- [Interprocess communication (bshell) synopsis](synopsis.md)
