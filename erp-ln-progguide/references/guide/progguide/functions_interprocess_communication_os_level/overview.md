# Interprocess communication (OS level) overview
These functions enable BAAN processes in different bshells to communicate with each other. On UNIX platforms you can use both the message queue and pipe mechanisms. On Windows NT platforms you can currently use only message queues.

## Message queues
With the **.message* functions, BAAN processes in different bshells can communicate with each other by means of UNIX message queues or NT mailslots (referred to here as mailboxes). A process can create new mailboxes, connect to existing mailboxes, and read from and write to those mailboxes.
Processes use the [open.message()](open.message.md) function both to create a new mailbox and to connect to an existing mailbox. The arguments of the *open.message()* function include a project number and the name of a file that is readable by all processes that want to use the mailbox. The project number and some attribute of the specified file are used internally to generate a numeric key that uniquely identifies the mailbox. All processes that want to use the same mailbox must generate the same key, so they must call *open.message()* with the same project number and file name arguments.
Once a process has connected to a particular mailbox, it can write to it and read from it by using the [send.message()](send.message.md) and [recv.message()](recv.message.md) functions. When there is no further use for a particular message queue, you must explicitly destroy it by calling [close.message()](close.message.md).
On UNIX platforms, the mailbox functions can use the UNIX message queue ID instead of the mailbox key to address a particular mailbox. To do this, *all* functions must specify 1 in the optional *fast* argument. Using the UNIX message queue ID has both advantages and disadvantages. For example:
- The UNIX system call to convert the mailbox key to a message queue ID ( *msgget()*) is called only once – that is, during *open.message()*. It is not called during *send.message()*, *recv.message()*, or *close.message()*. So, the load on the UNIX system is reduced.
- You cannot use a message queue key that was not returned by *open.message()*.
- Some errors, such as a removed message queue, can be difficult to detect.   On Windows NT, only the bshell that created a certain queue can read from this queue . So, multiple readers reading messages from the same message queue does not work on Windows NT, nor the situation where one process creates a queue and tells another process to read from this queue.
There is no such restriction on the write-side (any process can write to any queue).
Please use mailboxes in such a way that it works on both UNIX and Windows NT!

## Pipes
On UNIX platforms, the bshell can use unnamed pipes to communicate with an external UNIX process started by the same bshell.
On Windows NT, this has not been implemented in the bshell.

## Related topics
- [Interprocess communication (OS level) synopsis](synopsis.md)
