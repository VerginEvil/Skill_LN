# Interprocess communication (bshell) overview
Use these functions to handle communication between different BAAN processes running in the same bshell.

## BMS messages
The BMS mechanism supports broadcast messages, enabling messages to be sent to multiple processes. Messages can be up to 2048 characters long.
The sender process can use process IDs or masks to determine which processes a message is sent to.
- *Masks:* A mask is a character string used to control which messages a process can receive. It can be added to any process by using the [bms.add.mask()](bms.add.mask.md) function. If the sender of a message specifies a mask for that message, the message is sent only to those processes to which the specified mask has been added.
- *Process IDs:* Instead of, or in addition to a mask, the sender of a message can specify the process ID of the process for which the message is intended. The message is then sent only to that process. If a mask is also specified for the message, the process can receive the message only if the mask was previously added to the process. Receiving processes can use masks and levels to control which messages it receives.
- *Masks:* If a particular mask is added to a process, the process can receive all messages sent with that mask.
- *Levels:* The sender of a message can specify a level for that message. Receiving processes can then choose which level of messages they wish to receive. There are four predefined broadcast messages that the system can send to processes. Processes must set the bms.shutdown, bms.exit, bms.exit.child, bms.startup, and bms.startup.child masks to receive these messages.
- *bms.shutdown:* When this mask is set for a process, the message “bms.shutdown” is sent to the process when all processes that do not have this mask set have ended. It indicates that the process must exit because the bshell wants to stop.
- *bms.exit:* When this mask is set for a process, the exit value of an ended process is sent to the process. The received message contains the string “exit<exit.value>”. The process number of the exited process is provided in evt.bms.sender(event).
- *bms.exit.child:* When this mask is set for a process, the exit value of an ended child process is sent to the process. The received message contains the string “ exit.child<exit.value>”.
- *bms.startup:* When this mask is set for a process, the message “startup” is sent to the process when a process is started.
- *bms.startup.child:* When this mask is set for a process, the message “startup.child” is sent to the process when a child process is started.   Note that when one of the above message is sent, evt.bms.command(event) is zero.

## Bucket messages
Bucket messages provide a simple mechanism for two processes to exchange small packets of information (up to 100 characters long). A process uses [send.bucket()](send.bucket.md) or [send.wait()](send.wait.md) to send a data string to another specified process. A process calls [receive.bucket$()](receive.bucket.md) to receive the next bucket message sent to it by any other process.

## Related topics
- [Interprocess communication (OS level) overview](../functions_interprocess_communication_os_level/overview.md)
- [Interprocess communication (bshell) synopsis](synopsis.md)
