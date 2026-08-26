# Using the Call Graph Profiler
All variables mentioned in this section can be used as resource variables (in lowercase) and as environment variables (in uppercase). Setting them as environment variables is probably the most frequently used method, as it can be done directly from the BW Config. Setting them as resource variables is possible in various files, with various restrictions regarding scope and overwriting:
- `$BSE/lib/defaults/all` This is for all users.
- `$BSE/lib/defaults/bshell` This is for all users; `bshell` should match with the ipc_info name of the bshell.
- `$BSE/lib/user/u<>` This will be overwritten during 'convert to runtime' of userdata.
| | | |
|---|---|---|
|  |  |  |
| Variable | Synopsis | Explanation |
| PROFILE_ALL | `PROFILE_ALL=[0|1|2]` |  Set this variable to:  |
| PROF_DIR | `PROF_DIR=<>` |  Specify the directory for the Call Graph Profile files. The default value is $BSE_TMP (usually $BSE/tmp). If this variable is set with a relative path $HOME will be prepended. The Call Graph Profiles are written to files with the following name: profile.<bshell pid>.<session name>.<pid>.html  |
| PROF_RTIME | `PROF_RTIME=[0|1]` | Set this variable to add information to the Call Graph Profile that is sorted by run time. The default value is '1'.  |
| PROF_CLIENT | `PROF_CLIENT= <>` |  Set this variable to move the Call Graph Profiles to a directory on the client. The Call Graph Profile will be deleted from the ERP server after copying it to the client. When startstart is specified the Call Graph Profile is opened in the default browser (this *startstart* option does not work in WebUI and LN UI). Examples: PROF_CLIENT=save:c:\temp save on c:\temp PROF_CLIENT=start:c:\temp save on c:\temp and start browser  |
| BDB_ALWAYS_FLUSH | BDB_ALWAYS_FLUSH=[0|1] |  This controls the flushing of the data to the database. With the Call Graph Profiler enabled this setting is enabled by default.  |
| PROFFILES | PROFFILES=<file1;file2> |  This parameter allows to include file1 and file2 to be added to the System Information File that gets generated. When the filename is relative it is relative to $BSE.  |
| PROFILE_TRAMPOLINE | PROFILE_TRAMPOLINE=bshell.fun1[,bshell.fun2[,another.*]] |  This parameter allows the inclusion of bshell functions into to the Call Graph Profiler output. For example setting this variable to xml* will include all xml* functions into the Call Graph Profiler output. Use only when a bshell function is suspect of being a performance problem.  |
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
