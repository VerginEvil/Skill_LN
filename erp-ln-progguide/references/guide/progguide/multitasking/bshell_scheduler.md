# Bshell scheduler
The bshell scheduler is responsible for managing and scheduling processes. It maintains four process queues, as follows:
- running queue
- blocking queue
- sleeping queue
- terminating queue  The scheduler keeps all processes in one or other of the above process queues, depending on their current state.

## Running queue
The scheduler schedules processor time only for those processes in the running queue. It schedules each process in the running queue in turn, in order of priority. Each scheduled process receives a number of ticks, and the execution of each instruction costs the process a certain number of ticks. When the process has used up all its ticks, the bshell schedules another process.
The scheduler always schedules the process with the highest priority.
When a process is started, it gets a default priority (this depends on its nice value). While it is in the running queue, the process's priority is incremented each time that another process is scheduled. In this way, the process's priority increases until it has the highest priority in the running queue. It is then scheduled. When a process has been scheduled, its priority returns to its default value.

## Blocking queue
When a process is waiting for input, the scheduler moves it from the running queue to the blocking queue. So, the running queue contains only processes that can be run. When a blocked process receives an event, it is moved back from the blocking queue to the running queue.

## Sleeping queue
Processes in the sleeping queue are suspended until some external action wakes them again. Processes can be put in a sleeping state (and so in the sleeping queue) only by the functions [sleep()](../functions_processes/sleep.md), [suspend()](../functions_processes/suspend.md), [receive.bucket$()](../functions_interprocess_communication_bshell/receive.bucket.md), and related functions.

## Terminating queue
When a process ends, it is stripped of almost all allocated data and moved to the terminating queue. When the scheduler has scheduled another process to run, it then 'cleans up' the terminating queue. That is, it removes all processes except *zombie* processes. A zombie process is a process that has ended but whose parent process has not yet caught its exit signal.

## Related topics
- [Multitasking and the GUI](multitasking_and_the_gui.md)
