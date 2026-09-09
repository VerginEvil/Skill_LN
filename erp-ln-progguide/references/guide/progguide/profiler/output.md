# The Call Graph Profile

## Header, summary, and hyperlinks
The summary shows the total CPU time of the profile, the total run time of the profile and the amount of time that was spent waiting on UI events (waiting for the user to interact with the user interface). In the example in picture 1 the total run time is 38.3 seconds, of which 8 seconds was spent waiting on UI events.

- *UI wait time* This is the run time a process waits for user interaction. It is called Evitable Wait Time because the run time is dependent on user interaction

- *Interprocessing wait times* This includes 3GL process communication like BMS messaging

- *Interprocess run time* This is the run a process waits for other 3GL/4GL (zoom sessions etc.) It is called Inevitable wait time because the other processes execute on the behalf of this process. Also included are all Java related execution times and programs that are stated via run.prog or run.baan.prog

- *Other waiting or processing times* This includes all other processing time not included in the categories mentioned above

The header contains some details about the profile and about the system and a summary of the Call Graph Profile. One important feature is the "system info" file which contains system settings which affect the environment.

## The System information header

## Summary of various wait times
The items that are in blue can be selected and the Call Graph Profile where available will be shown. Note that for example the Call Graph Profile of "ottstpstdlib" will be available after a bshell exits. Additionally, sessions like "ttstpclose" never contain any relevant profile information.

## Profile output
The hyperlinks lead to the various sections of the Call Graph Profile (Query Summary, Call Graph, Flat Profile). Normally there is only one occurrence of each of these sections, sorted by CPU time. When the PROF_RTIME=1 variable is set, there is another occurrence of these sections, sorted by run time.

## Query Summary
For SQL statements some work is done in the bshell, some work is done in the database driver and some work is done in the database. The run time of SQL statements covers all of these processes and operating system overhead. Therefore run time (rtime) is often the first indicator for the performance of SQL statements. Note that run time also includes wait time for other events that may not be related to the SQL statement itself (e.g. when the system is just too busy with other processes).

## Object Summary

## Breakdown per Function
The breakdown per function (picture 4) shows how functions that are called in a nested way (recursively) are represented in the call graph. The statistics of each depth on which the function is called are kept separately, in case of recursion as might happen with functions like dal.select(). (Not shown in example.)
In this example breakdown per function (fld.ondisplay) was used 115 times.

## Call Graph
Each entry (or node) on the Call Graph is about one specific function which is printed in bold in the middle of the entry. The parent functions (callers) are above it, and the child functions (callees) are below it. Before the function names there are a couple of columns:

- *index*: a sequence number that indicates the position of the entry in the list. This index is also printed after the parent and child functions. The number is an indication of the relative importance of a function and its descendents in the profile (high number = relatively important, low number = relatively unimportant).

- *%time*: this is the percentage of the total CPU time taken by this function with its descendents.

- *utime + stime*: the user time + system time for the function itself and for the descendents. For these numbers are the part of the user time and system time of the function that this node is about, when called from this particular parent function. For these numbers are the part of the user time and system time of the child function when called from the function that this entry is about. The utime + stime is printed separately for 'self' and for 'descendents'.

- *rtime*: the run time for the function itself and for its descendents. For these numbers are the part of the run time of the function that this node is about, when called from this particular parent function. For these numbers are the part of the run time of the child function when called from the function that this entry is about. The rtime is printed separately for 'self' and for 'descendents'.

- *called*: the number of calls to the function. For this field contains the number of calls that this parent makes to this function and after the slash the total number of calls to this function. For this field contains the number of calls that this function makes to this child and after the slash the total number of calls to this child function in this profile.

## Self and descendents times relationships

## SQL Statements
SQL statements are included in the Call Graph because a large portion of the time consumption on the server (both CPU time and run time) is related to SQL statements. In the Call Graph this is best indicated by the run time on SQL statements. The SQL statements are printed in the call graph after the sql.parse() call for the statement.

## Flushing of pending updates/inserts/deletes
*Next comment applies when BDB_ALWAYS_FLUSH has been set to '0'.* Buffered updates/inserts/deletes are flushed to the database at the next commit.transaction(), abort.transaction() or at the next SQL statement (whichever comes first). The time (both CPU time and run time) that is spent during execution of that statement will include the time that was required for the flush of buffered updates/inserts/deletes. The Call Graph Profiler is recording the time that is taken for flushing buffered updates separately. It is shown as descendents time on the database-related bshell functions (db.*, commit.transaction, abort.transaction, sql.fetch, etc)

## Flat Profile
Note that the Flat Profile does not contain lines about internal bshell functions (like db.*, sql.fetch, commit.transaction, etc)
The time consumption for these functions has been added to the time consumption for the 3GL function in which these bshell functions are called.
Descriptions of columns in the Flat Profile:

- *count*: number of times the function is called

- *utime*: user time in the function

- *stime*: system time in the function

- *rtime*: run time int the function

- *call*: time (user/system/run) per call

- *perc %*: percentage of the time (user/system/run) in the function

- *alloc*: number of bytes allocated in the function

- *free*: number of bytes freed in the function

- *ticks*: number of bshell ticks in the function

- *function*: the name of the function

## Related topics
- [Using the Call Graph Profiler](using.md)

- [Analyzing the Call Graph Profile](analyzing.md)

- [Call Graph Profiler Example](example.md)

- [Call Graph Profiler Glossary](glossary.md)
