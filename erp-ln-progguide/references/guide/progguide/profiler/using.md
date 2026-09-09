# Using the Call Graph Profiler
All variables mentioned in this section can be used as resource variables (in lowercase) and as environment variables (in uppercase). Setting them as environment variables is probably the most frequently used method, as it can be done directly from the BW Config. Setting them as resource variables is possible in various files, with various restrictions regarding scope and overwriting:

- `$BSE/lib/defaults/all` This is for all users.

- `$BSE/lib/defaults/bshell` This is for all users; `bshell` should match with the ipc_info name of the bshell.

- `$BSE/lib/user/u<>` This will be overwritten during 'convert to runtime' of userdata.
| |
|---|
| '0' to disable profiling (default); |
| '1' to profile most sessions (see exclusion list below); |
| '2' to profile everything. |
The following processes are less important for performance analysis and will not be profiled with option 1:
| | |
|---|---|
| Process | Purpose |
| ttstpmsg | popup message |
| ttstpdisplay | print output for device 'D' |
| ttstppollmess | display system message |
| ttstpsplopen | select print device |
| ttstpsplclose | print spooler close |
| ttstpoledaemon | OLE Daemon |
| all ttdsk* programs | menu browser, etc. |
Note:
The Call Graph Profiler records a lot of data about the code that is executed. This incurs some overhead and will slow your program down.
Examples of lines in resource files to configure the profiler:
profile_all:1 prof_dir:/home/bsp/profile prof_client:save:c:\temp
Examples of bshell commands that can be configured in BECS, WebUI and LN UI:
-- -set PROFILE_ALL=1 -set PROF_DIR=/home/bsp/profiles
-- -set PROFILE_ALL=1 -set PROF_CLIENT=save:c:\temp
-- -set PROFILE_ALL=1 -set PROF_CLIENT=start:D:\PROFILES -set PROF_RTIME=1

## Related topics
- [The Call Graph Profile](output.md)

- [Analyzing the Call Graph Profile](analyzing.md)

- [Call Graph Profiler Example](example.md)

- [Call Graph Profiler Glossary](glossary.md)
