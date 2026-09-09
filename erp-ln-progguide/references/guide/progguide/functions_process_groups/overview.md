# Process groups overview
Use these functions to handle process groups.
A process group is a group of related, interdependent processes. One process is the group leader. Child processes are started by the leader or by one of its children. All processes belong to a process group.
Process groups have the following characteristics:

- Each process group has its own event queue. Events are sent to the process group, not to individual processes.

- When one process within a group starts another process, that process is automatically placed in the same process group.

- For the group leader, the predefined variable *background* is set to zero, For child processes, this variable is set to 1.

- When a process is killed or ended, its parent is automatically awakened, unless the parent and child are in different groups.

- You use the *grab.mwindow()* function to set the process group to which a main window sends its events. After calling this function, all events that occur in the main window are sent to the process group.

See [Processes overview and synopsis](../functions_processes/overview_and_synopsis.md) for details of the functions available for handling processes.

## Related topics
- [Process groups synopsis](synopsis.md)
