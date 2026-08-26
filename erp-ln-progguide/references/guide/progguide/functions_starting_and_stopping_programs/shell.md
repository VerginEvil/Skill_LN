# shell()

## Syntax:
`function long shell( string command, long mode )`

## Description
*Deprecated.* This function is supported for backward compatibility only. In new applications, use [run.prog()](run.prog.md) and [run.baan.prog()](run.baan.prog.md) instead.
This starts the vt200 compatible terminal emulator to execute the command specified in the *command* argument. The shell (UNIX only) process is connected with the bshell by means of a pseudo tty. Running a shell does not block the bshell. You can switch to another window and perform other tasks.

## Arguments
| | | |
|---|---|---|
| `string` | `command` |  The command to be executed.  |
| `long` | `mode` |  This can be a combination of the following options:  |

## Return values
> 0 return code of *command*
0 success
-1 maximum number of pty's is reached; general error code
-2 cannot open the master pty
-3 pipe command failed
-4 fork of reader process or shell process failed
-6 cannot start terminal emulator

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  The function is available only for programs running under UNIX, and not for programs running under Windows NT.

## Example 1
Run a shell command that creates no main window. Output can appear on the current main window. The bshell process waits for the shell command to end.
```

ret = shell("rm $BSE/tmp/file", 0)
```

## Example 2
Similar to example 1. The terminal emulator displays "Press <RETURN>" and waits for confirmation after the shell process has ended.
```

ret = shell("ls -l", SHELL_CONFIRM)
```

## Example 3
Run a shell command in the background. Output is displayed in a separate main window. The main window is stretched to its maximum possible size on the terminal display.
```

ret = shell("vi helloworld.c", SHELL_NO_WAIT + SHELL_MAXWINSIZE)
```

## Example 4
Run a shell command that produces no output. Errors can be caught by checking the return value of the shell function.
```

ret = shell("cp /tmp/a /tmp/b", SHELL_NO_OUTPUT)
```

## Related topics
- [Starting and stopping programs: overview and synopsis](overview_and_synopsis.md)
