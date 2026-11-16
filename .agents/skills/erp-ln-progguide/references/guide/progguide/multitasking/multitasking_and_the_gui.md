# Multitasking and the GUI
The BAAN bshell provides the execution environment for BAAN applications. Whenever a user logs on to the BAAN system, a separate bshell process is activated for that user. So, when multiple users log on to the same BAAN system, or when the same user logs on multiple times, multiple bshell processes are activated on the execution platform.
The BAAN bshell provides a multitasking execution environment for BAAN applications. Each bshell can execute and schedule multiple parallel processes. So, it blocks individual processes only while they are waiting for user input, and not while other processes are waiting for user input.
This section provides an overview of how processes and user interface interaction are managed by the bshell.

- [Bshell scheduler](bshell_scheduler.md)

- [Context switches](context_switches.md)

- [Events](events.md)

- [Requests, inquiries, and replies](requests_inquiries_and_replies.md)

- [Processes, process groups, and main windows](processes_process_groups_and_main_windows.md)

- [Synchronizing processes with the wait() function](synchronizing_processes_with_the_waitfunction.md)

The following diagram provides a schematic overview of the relationships between the scheduler, process queues, and the display server.
Note  The bshell is a single-threaded process. The complete bshell blocks when a database action is performed by the database driver.
