# Synchronizing processes with the wait() function
The [wait()](../functions_processes/wait.md) function enables synchronization of parent and child processes. It causes the parent process to wait for one or all of its children to exit before continuing. Each child process sends an exit signal to the parent process when it ends.
The parent can choose to ignore child signals or not. If it wants to ignore child signals, the parent process calls:
```

signal(SIGCHLD, SIGIGN)
```
If it does not want to ignore child signals, it calls:
```

signal(SIGCHLD, SIGNOIGN)
```
When a parent process issues a [wait()](../functions_processes/wait.md) call but is ignoring child signals, child processes exit without any action by the parent. They exit, send an exit signal to the parent, and are removed. The parent process blocks until it receives an exit signal from the last process. The exit value and process ID of the last child are returned in the return value and *prodess_id* argument respectively of the *wait()* function. The following diagram illustrates this situation.
When a parent process issues a [wait()](../functions_processes/wait.md) call and is not ignoring child signals, the exit signal of every child process is caught by the *wait()* function (including exit signals from children in other process groups). So, each child waits after exiting until its parent process calls the *wait()* function. While it is waiting for the parent process to catch its exit value, the child process becomes a zombie process. It is placed in the terminating process queue, but is not removed until the parent catches its exit signal. The following diagram illustrates this situation.
Note that if a parent ends while some of its children are zombie process, those children are removed automatically.

## Related topics
- [Multitasking and the GUI](multitasking_and_the_gui.md)
