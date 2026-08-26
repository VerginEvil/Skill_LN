# app_start()

## Syntax:
`#include <bic_desktop>`
`function long app_start( string commandline, string directory, string stdin, string stdout, string stderr )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated. Instead you should use function: [start.application.local()](start.application.local.md).
This starts the application specified in the *commandline* argument. It returns an ID for the started application. You can subsequently use this ID as the *app.id* argument in the [app_status()](app_status.md) function.

## Arguments
1.
1.
1.
1.
| | | |
|---|---|---|
| `string` | `commandline` |  This specifies the command that starts the application. If *commandline* does not include a directory path, Windows searches for the executable file in the following directories, in the order shown below: The directory where BW is loaded. The Windows system directory. The Windows directory. The directories listed in the PATH environment variable.  |
| `string` | `directory` |  The default working directory for the application. Some applications handle the default working directory themselves and are therefore not influenced by the setting of this argument.  |
| `string` | `stdin` |  The standard input file name.  |
| `string` | `stdout` |  The standard output file name.  |
| `string` | `stderr` |  The standard error file name.  |

## Return values
| | |
|---|---|
| >= 0 | Identification number of the started application is returned.  |
| < 0 | Error. The negative value of the system error |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  If *commandline* specifies the name of a nonexecutable file, Windows starts the application with which the file name extension is associated. For example, if *commandline* is c:\temp\file.txt, and .txt is associated with the Notepad application, Windows will start Notepad. Because users can change the association of a file name extension, you cannot predict which application will start.
This functionality is not available when you specify standard input, output, and error files.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
