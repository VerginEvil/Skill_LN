# Context switches
Each running process receives a number of ticks when it is scheduled. This is the equivalent of a UNIX time slice. The execution of each instruction costs the process a number of ticks. When the process has used up all its ticks, the bshell schedules another process. The switch to another process is referred to as a context switch.

## Forcing a context switch
Normally, the bshell executes context switches automatically. Functions such as [bms.send()](../functions_interprocess_communication_bshell/bms.send.md), [appl.set()](../functions_appl/appl.set.md), and [start.session()](../functions_starting_and_stopping_programs/start.session.md) also cause a context switch. And programmers can force a context switch by calling suspend(0).This is useful when the immediate response of another process is required.

## Allocating bonus ticks
The database locking mechanism prevents two or more processes from updating or deleting the same record or table simultaneously. When a process is modifying the database, the relevant record or table is locked. Other processes cannot modify that record or table until the lock is released.
Some database management systems use a page locking mechanism instead of a record locking mechanism. That is, they lock a predefined block size that can include several records. This can result in a deadlock when two processes within the same bshell attempt to lock records that are positioned very close to each other in the database. To prevent this happening, you can boost the number of ticks assigned to a process by using the bonus tick mechanism. When this mechanism is enabled, the bshell assigns bonus ticks to a process when it locks a database record (note that a lock is applied when the first update, insert, or delete is performed by a database transaction). This means that the process is not scheduled out before the lock is released (the lock is released when the transaction is committed or aborted).
You can configure the bonus tick mechanism by means of environment variables or user resources.
| | |
|---|---|
| 0 | Warning mechanism off. |
| 1 | Warning mechanism on. A warning message is displayed when a process is about to loose its time slice. The message is also displayed when a context switch is forced. |
| 2 | This is similar to 1, except that when the object is in debug mode, the process stops and the debugger points to the next instruction. |
| 3 | This is similar to 2, except that the process is aborted. |

## Related topics
- [Multitasking and the GUI](multitasking_and_the_gui.md)
