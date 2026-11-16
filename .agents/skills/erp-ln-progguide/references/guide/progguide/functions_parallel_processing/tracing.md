# Parallel Application Processing Tracing
Error reporting and tracing is an important aspect of a product which is usually run without any user interface. Therefore two mechanisms are used: error logging and tracing. Below the characteristics of these two mechanisms are described. The characteristics of the error logging mechanism are:

- Serious errors are logged unconditionally

- A single error log file is used in which all serious errors related to parallel processing are logged.

- The name of this file is: ${BSE}/log/log.parbshell

- The maximum file size of this file is: 512 Kb

- When this size is reached, the current log file is named "olg.parbshell" and a new empty "log.parbshell" file is created.

The characteristics of the trace mechanism are:

- A single trace file will be generated per parallel session run

- All bshells started for this run will send errors and trace output to the same file.

- The name of this file is: ${BSE}/log/trace.parbshell.<pid> in which <pid> is the process id of the client Bshell

- 0 - no tracing

- 1 - trace API calls

- 2 - trace communication

- 3 - trace API calls and communication

Each trace line is constructed as follows:
[date time] <user>:<session>(pid), <component> (bshellpid): <message>
In which <component> is one of:

- ClientAPI

- ServerAPI

- SupportAPI

- ServerCOM

- ClientCOM

## Related topics
- [Parallel Application Processing Overview](overview.md)

- [Parallel Application Processing synopsis](synopsis.md)
