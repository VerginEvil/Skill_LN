# pstat()

## Syntax:
`function long pstat( long pid, ref string progname, ref long info(PSMAXSIZE) )`

## Description
This returns status information about a specified process.

## Arguments
| | | |
|---|---|---|
| `long` | `pid` |  The ID of the process for which you want to retrieve information. Specify a negative value here to retrieve information about the init process.  |
| `ref string` | `progname` |  This returns the process code.  |
| `ref long` | `info(PSMAXSIZE)` |  This returns status information that you can retrieve with the following macros, each of which returns a long: *ps.state(info)* returns PSRUNNING, PSBLOCKING, PSSLEEPING, or PSTERMINATING. *ps.group(info)* returns the identifier of the process group to which the process belongs. *ps.parent(info)* returns the identifier of the parent process of the process group. *ps.flags(info)* returns flags. *ps.nice(info)* returns the [nice value](../multitasking/bshell_scheduler.md) of the process. *ps.cpu.use(info)* returns the number of ticks used by the process. *ps.mwin(info)* returns the object id of the [main window](../functions_user_interface_objects/dscmwindow.md) of the process. *ps.pri(info)* returns the [priority](../multitasking/bshell_scheduler.md) of the process. *ps.size(info)* returns the amount of memory allocated by the process (in bytes). *ps.cwin(info)* returns the object id of the current [window](../functions_user_interface_objects/dscmwindow.md) of the process. *ps.menu(info)* returns the object id of the [menubar](../functions_user_interface_objects/dscbarmenu.md) of the current window of the process. *ps.bar(info)* returns the object id of the [toolbar](../functions_user_interface_objects/dsctoolbar.md) of the current window of the process.  |

## Return values
| | |
|---|---|
| < 0 | Could not retrieve info: process does not exist.  |
| >= 0 | The process ID of the next process in the internal process list, or 0 if this is the last process in that list.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related help topics
- [Processes overview and synopsis](overview_and_synopsis.md)

## Example
```

long     info(PSMAXSIZE)
string   progname(512)
long     procid

procid = -1
procid = pstat( procid, progname, info )
while procid > 0
        | process info
        procid = pstat( procid, progname, info )
endwhile
```
