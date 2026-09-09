# run.baan.prog()

## Syntax:
`function long run.baan.prog( const string progname, const string arguments, long mode, [ string stdin, string stdout, string stderr, ref long os.pid ] )`

## Description
The function *run.baan.prog()* runs a program from $BSE/bin.

## Arguments
| | |
|---|---|
| RP_WAIT | wait for the program to finish |
| RP_NOWAIT | run as a background program. In this case there is no standard way to determine whether the program has finished or what the exit code of the program was. Other means must be used to synchronize with such a background process. |
| RP_INTERACTIVE_WINDOWS_LOGON_FLAG | perform an interactive logon on the Windows host specified in the *progname* argument. Without this flag, the logon will not be an interactive logon, but a network logon. This flag is available as of [porting set TIV](../tiv/tiv_overview.md) [level 2361](../tiv/tiv_2361.md). For further details, see the notes and examples below. |

## Return values
0: program executed successfully. When *mode* RP_NOWAIT was used, it means the program was started successfully.
< 0: program could not be started.
> 0: program did not execute successfully.
Note that the return value cannot be retrieved when the *mode* argument is set to RP_NOWAIT.

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  Input for the program cannot be entered interactively, but it can be read from a file. There are two ways to do this:

- Use the *stdin* argument described above.

- If the program has a command line argument for input redirection, pass this in the *arguments* argument to let the program read from a file.

Output or error messages from the program cannot be displayed, but they can be stored in a file. There are two ways to do this:

- Use the *stdout* and *stderr* arguments described above. (Please note that the previous contents of these files is lost.)

- If the program has a command line argument for output/error redirection, pass this in the *arguments* argument to let the program send results to a file. (For example, several Baan programs accept -q, -qo, and/or -qe arguments.)

Note  When the *progname* argument does not contain a host name, then the bshell user will run the specified program, without logging on again. On Windows, the bshell user is normally logged on via a network logon.
When the *progname* argument contains a host name, then a new logon is done on the specified host and the newly logged on user will run the specified program. On Windows, the new logon is normally a network logon.
The logon parameters are taken from the *host name* entry in the $BSE/lib/user/r<user> file of the current user.
As of [porting set TIV](../tiv/tiv_overview.md) [level 2361](../tiv/tiv_2361.md) the *mode* flag RP_INTERACTIVE_WINDOWS_LOGON_FLAG is available. When it is used, the new logon is an interactive logon.
Internally, the logon is done with the Windows API function [LogonUser](https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-logonusera). For the normal network logon, the Win32 API flag LOGON32_LOGON_NETWORK_CLEARTEXT is used. For the interactive logon, the Win32 API flag LOGON32_LOGON_INTERACTIVE is used.
Once logged on, the difference between a network logon and an interactive logon is in most cases irrelevant. In both cases the user has access to network resources, like shared files. However, an interactive logon also allows access to UNC path network printers, whereas a network logon does not do so.

## Example
```

string	hostname(100)
string	command(100)
string	arguments(100)

...

| The bshell user runs the command.
run.baan.prog( command, arguments, RP_WAIT )

| A new network logon is done on host 'hostname' to run the command.
run.baan.prog( hostname & "!" & command, arguments, RP_WAIT )

| A new interactive logon is done on host 'hostname' to run the command.
run.baan.prog( hostname & "!" & command, arguments, RP_WAIT+RP_INTERACTIVE_WINDOWS_LOGON_FLAG )

| A new network logon is done on the local host to run the command.
run.baan.prog( "localhost!" & command, arguments, RP_WAIT )

| A new interactive logon is done on the local host to run the command.
run.baan.prog( "localhost!" & command, arguments, RP_WAIT+RP_INTERACTIVE_WINDOWS_LOGON_FLAG )
```

## Related topics
- [Starting and stopping programs: overview and synopsis](overview_and_synopsis.md)
