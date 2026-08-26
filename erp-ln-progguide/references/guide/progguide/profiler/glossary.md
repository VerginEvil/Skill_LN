# Call Graph Profiler Glossary
| | |
|---|---|
| Term | Explanation |
| CPU time |  The amount of time a bshell process *actually* uses the CPU. This does not include time waiting for e.g. on database, the disk and user input. Note: The cpu time includes the time spent in the database driver when the bshell runs in the so called 'combo mode' (that is: when the database driver runs as a DLL or shared library).  |
| run time | The amount of *elapsed time* (sometimes also referred to as "wallclock time" or "rtime") that was spent with execution of code in the bshell process and time spent waiting on database, disk, network and user input.  |
| utime / stime |  utime is "user time", the actual time spent in the code itself. stime is "system time", the actual time spent in system functions on behalf of the bshell. utime + stime = CPU time  |
| children / parents |  The term *children* (or descendants) is used for the functions that are callee of a particular function.  |
