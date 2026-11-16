# Bshell resources
Resources are specified in the u<user> file in the '$BSE/lib/user' directory, but also in the files '$BSE/lib/defaults/<logical_name_of_bshell>' and '$BSE/lib/defaults/all'. The logical name of the bshell is the name you specify for the Bshell in BW.
A bshell resource often has a corresponding [environment variable](bshell_environment_variables.md) via which it is possible to set the value of the resource.
Resource values may be retrieved by means of the bshell function [get.resource$()](../functions_system_and_user_information/get.resource.md).
The following (incomplete) list shows some of the bshell resources.
| | | | |
|---|---|---|---|
| Flag name | Value | Command line option | Meaning |
| DATA_AKTIE | 1 | dbgdata | Show data input options (not for fields!). |
| OBJ_SIZE | 2 | dbgobj | Show object information. |
| SHOW_FLOW_ARRAY | 4 | dbgarray | When showing 3GL program flow, also show the complete array arguments. |
| DEBUG_YY | 010 | dbgyy | Debug expressions. |
| FUN_DEBUG | 020 | dbgfun | Debug functions. |
| BDB_SERVER_TYPE | 040 | dbgsrv | Show bdb server type. |
| BDB_DELAY_LOCK | 0100 | dbglck | Show locking errors. |
| MUL_ACTION | 0200 | dbgmulact | Show process actions (activate, sleep, kill etc.). |
| BDB_REFER | 0400 | dbgrefer | Show references. |
| BDB_ACTIONS | 01000 | dbgbdbact | Show bdb actions. |
| DEBUG_FILEDEV | 02000 | dbgfdev | Debug file access. |
| RESOURCE_DBG | 04000 | dbgres | Show loaded resources. |
| PRINT_ENUMS | 010000 | dbgenums | Show loading of enums. |
| INSTR_DEBUG | 020000 | dbginstr | Show bshell cpu instructions. |
| BCPU_DEBUG | 040000 | dbgcpu | Use debug version of the bshell cpu. |
| SRDD_USAGE | 0100000 | dbgsrdduse | Show srdd usage. |
| GET_PUT_VAR | 0200000 | dbggpvar | Debug getvar and putvar. |
| SCHED_DEBUG | 0400000 | dbgsched | Debug scheduler. |
| PTY_DEBUG | 01000000 | dbgpty | Debug PTYs. |
| DEBUG_FILE | 02000000 | dbgfile | Show successfully opened sequential files. |
| DEBUG_TSS | 04000000 | dbgtss | Debug TSS functions. |
| SYM_DEBUG | 010000000 | dbgsym | Show assignments. |
| DC_DEBUG | 020000000 |  | Debug distributed computing functions. Unused. |
| SHOW_TRACE | 040000000 | dbgstack | Show stack traces. |
| DEBUG_MESG | 0100000000 | dbgmesg | Stop in the debugger when a warning message is sent to the display server. |
| SHOW_FLOW | 0200000000 | dbgflow | Debug 3gl, 4gl program flow. |
| SOCK_DEBUG | 0400000000 | dbgsock | Debug network socket actions. |
| DEBUG_JVMI | 01000000000 | dbgjvmi | Debug JVMI interactions within bshell. |
| DEBUG_LTS | 02000000000 | dbglts | Debug Language Translation Support (LTS). In order to see whether label lookup was successful, all labels get a fixed first letter: X - the label was looked up and found in the dumped and indeXed label files; B - the label was looked up and found in the dataBase; F - the Fallback label value is used. For example you see the "Create Runtime Help" session displayed as "Xreate Runtime Help". And in the menu as "Freate Runtime Help". |
| DEBUG_AMS | 04000000000 | dbgams | Debug ams. |
| DEBUG_GRAPHS | 010000000000 | dbggraphs | Debug graphs/iterators. |
| DEBUG_MEM | 020000000000 | dbgcolor | Debug memory: dump m_help at strategic places. |
| DEBUG_S3 | 040000000000 | dbgs3 | Debug S3 3GL functions. |
| DEBUG_DBCM | 0100000000000 | dbgdbcm | Debug DBCM functionality. This flag is available as of [porting set TIV](../tiv/tiv_overview.md) [level 2540](../tiv/tiv_2540.md). |
| | | |
|---|---|---|
| Flag name | Value | Meaning |
| LoadLong | 1 | Log runtime loading of any [compile time constant integer expression](../3gl_features/arithmetic_operators.md#compile_time_constants). |
| LoadLongOverflow | 2 | Log runtime loading of any [compile time constant integer expression](../3gl_features/arithmetic_operators.md#compile_time_constants) of which the exact *unsigned* 32-bit result is outside the signed 32-bit value range, so it is in the range [2^31 … 2^32 - 1]. |
| ArithmeticOverflow | 4 | Log execution of operations where a runtime overflow occurs of the signed [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-bit value range. Also operations will be logged where an integer value outside the signed 32-bit value range is serialized to a four-byte sequence. Examples of such operations are [db.eq()](../functions_db_operations/db.eq.md), [store.long()](../functions_string_operations/store.long.md), [store.utc()](../functions_string_operations/store.utc.md), [ims.w.long()](../functions_ims/ims.w.long.md), [ims.w.utc()](../functions_ims/ims.w.utc.md), [seq.w.long()](../functions_directory_file_operations/seq.w.long.md), and [seq.w.utc()](../functions_directory_file_operations/seq.w.utc.md). Also operations will be logged where an integer value outside the signed 40-bit value range is serialized to a five-byte sequence. Examples of such operations are [db.eq()](../functions_db_operations/db.eq.md), [store.utc()](../functions_string_operations/store.utc.md), [ims.w.utc()](../functions_ims/ims.w.utc.md), and [seq.w.utc()](../functions_directory_file_operations/seq.w.utc.md). This option covers many, but not all, operations where integer values are involved. Whenever an operation is covered, it is fully covered, i.e. any overflow during that operation is detected and reported. |
| Long64Usage | 8 | Log execution of operations where a value outside the signed 32-bit value range is used. When the concerned value is outside the signed [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-bit value range, then its usage will be reported as an arithmetic overflow. Operations where an integer value outside the signed 32-bit value range is serialized to a four-byte sequence will be logged as an overflow Operations where an integer value outside the signed 40-bit value range is serialized to a five-byte sequence will be logged as an overflow This option covers many, but not all, operations where integer values are involved. Whenever an operation is covered, it is fully covered, i.e. any usage of a value outside the signed 32-bit value range during that operation is detected and reported. |

## Related topics
- [get.resource$()](../functions_system_and_user_information/get.resource.md)

- [Bshell command line option -set](bshell_command_line_options.md)

- [Bshell environment variables](bshell_environment_variables.md)
