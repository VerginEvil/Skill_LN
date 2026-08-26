# Bshell command line options
The following (incomplete) list shows some of the bshell command line options.
| | | |
|---|---|---|
| Command line option | Synopsis | Explanation |
| v, V |   | Print bshell version information to standard output. |
| ?, u |   |  Print bshell usage information to standard output. Use this option to find many other bshell command line options.  |
| logfile | `-logfile <file>` | Redirect stdout and stderr output to file <file>. In the supplied file name, the pattern %h will be substituted with the current hostname, the pattern %p will be substituted with the OS process ID of the bshell, and the pattern %u will be substituted with the current (short) baan user name. Default value for the supplied file name is bshell.%h.%p in some directory, typically ${BSE_TMP} or ${BSE}/log.  |
| keeplog | `-keeplog` | Do not remove the logfile after ending the bshell. |
| appendlog | `-appendlog` | Append to logfile instead of overwriting it (only useful with -logfile option).  |
| logtag | `-logtag <tag>` | The <tag> is used in the messages logged into the logfile and is especially useful when logging from multiple bshells to the same file (only useful with -logfile and -appendlog option).  |
| nolog | `-nolog` | Do not redirect stdout and stderr to a log file; they will go to the controlling terminal (if possible - on remote connection no output will appear).  |
| dbgams | `-dbgams` | Set the DEBUG_AMS flag in the [debug_level resource](bshell_resources.md).  |
| dbgarray | `-dbgarray` | Set the SHOW_FLOW_ARRAY flag in the [debug_level resource](bshell_resources.md).  |
| dbgbdbact | `-dbgbdbact` | Set the BDB_ACTIONS flag in the [debug_level resource](bshell_resources.md).  |
| dbgcolor | `-dbgcolor` | Set the DEBUG_MEM flag in the [debug_level resource](bshell_resources.md).  |
| dbgcpu | `-dbgcpu` | Set the BCPU_DEBUG flag in the [debug_level resource](bshell_resources.md).  |
| dbgdata | `-dbgdata` | Set the DATA_AKTIE flag in the [debug_level resource](bshell_resources.md).  |
| dbgdbcm | `-dbgdbcm` | Set the DEBUG_DBCM flag in the [debug_level resource](bshell_resources.md). This command line option is available as of [porting set TIV](../tiv/tiv_overview.md) [level 2550](../tiv/tiv_2550.md).  |
| dbgenums | `-dbgenums` | Set the PRINT_ENUMS flag in the [debug_level resource](bshell_resources.md).  |
| dbgfdev | `-dbgfdev` | Set the DEBUG_FILEDEV flag in the [debug_level resource](bshell_resources.md).  |
| dbgfile | `-dbgfile` | Set the DEBUG_FILE flag in the [debug_level resource](bshell_resources.md).  |
| dbgflow | `-dbgflow` | Set the SHOW_FLOW flag in the [debug_level resource](bshell_resources.md).  |
| dbgfun | `-dbgfun` | Set the FUN_DEBUG flag in the [debug_level resource](bshell_resources.md).  |
| dbggpvar | `-dbggpvar` | Set the GET_PUT_VAR flag in the [debug_level resource](bshell_resources.md).  |
| dbggraphs | `-dbggraphs` | Set the DEBUG_GRAPHS flag in the [debug_level resource](bshell_resources.md).  |
| dbginstr | `-dbginstr` | Set the INSTR_DEBUG flag in the [debug_level resource](bshell_resources.md).  |
| dbgjvmi | `-dbgjvmi` | Set the DEBUG_JVMI flag in the [debug_level resource](bshell_resources.md).  |
| dbglck | `-dbglck` | Set the BDB_DELAY_LOCK flag in the [debug_level resource](bshell_resources.md).  |
| dbglts | `-dbglts` | Set the DEBUG_LTS flag in the [debug_level resource](bshell_resources.md).  |
| dbgmesg | `-dbgmesg` | Set the DEBUG_MESG flag in the [debug_level resource](bshell_resources.md).  |
| dbgmulact | `-dbgmulact` | Set the MUL_ACTION flag in the [debug_level resource](bshell_resources.md).  |
| dbgobj | `-dbgobj` | Set the OBJ_SIZE flag in the [debug_level resource](bshell_resources.md).  |
| dbgpty | `-dbgpty` | Set the PTY_DEBUG flag in the [debug_level resource](bshell_resources.md).  |
| dbgrefer | `-dbgrefer` | Set the BDB_REFER flag in the [debug_level resource](bshell_resources.md).  |
| dbgres | `-dbgres` | Set the RESOURCE_DBG flag in the [debug_level resource](bshell_resources.md).  |
| dbgs3 | `-dbgs3` | Set the DEBUG_S3 flag in the [debug_level resource](bshell_resources.md).  |
| dbgsched | `-dbgsched` | Set the SCHED_DEBUG flag in the [debug_level resource](bshell_resources.md).  |
| dbgsock | `-dbgsock` | Set the SOCK_DEBUG flag in the [debug_level resource](bshell_resources.md).  |
| dbgsrdduse | `-dbgsrdduse` | Set the SRDD_USAGE flag in the [debug_level resource](bshell_resources.md).  |
| dbgsrv | `-dbgsrv` | Set the BDB_SERVER_TYPE flag in the [debug_level resource](bshell_resources.md).  |
| dbgstack | `-dbgstack` | Set the SHOW_TRACE flag in the [debug_level resource](bshell_resources.md).  |
| dbgsym | `-dbgsym` | Set the SYM_DEBUG flag in the [debug_level resource](bshell_resources.md).  |
| dbgtss | `-dbgtss` | Set the DEBUG_TSS flag in the [debug_level resource](bshell_resources.md).  |
| dbgyy | `-dbgyy` | Set the DEBUG_YY flag in the [debug_level resource](bshell_resources.md).  |
| nodebug | `-nodebug` | Prevent the debug window to be displayed on the monitor. |
| set | `-set var=val` |  Set environment variable 'var' to value 'val'. See this [list of bshell environment variables](bshell_environment_variables.md). Notice that it is possible to set the value of a [resource](bshell_resources.md) via its corresponding environment variable.  |

## Related topics
- [Bshell environment variables](bshell_environment_variables.md)
- [Bshell resources](bshell_resources.md)
