# start.application.local()

## Syntax:
`#include <bic_desktop>`
`function boolean start.application.local( string commandline, boolean waitFlag, ref long exitCode, [ const string verb ] )`

## Description
*Deprecated.* This starts the client application specified in the *commandline* argument.

## Arguments
| | | |
|---|---|---|
| `string` | `commandline` |  This specifies the command that starts the application. If *commandline* does not include a directory path, Windows searches for the executable file in the following directories, in the order shown below: The Windows system directory. The Windows directory. The directories listed in the PATH environment variable. This argument may also contain the full pathname of a local document. In this case the application associated with this document extension will be started. The *commandline* parameter may one or more times include the string ${BSE_TMP} which indicates the ${BSE}\tmp directory in case of Baan Windows or Windows temp directory in case of WebUI.  |
| `boolean` | `waitFlag` |  Indicates whether the application must wait for the local application to exit.  |
| `ref long` | `exitCode` |  Exit code of local application. Only contains a valid exit code when the *waitFlag* attribute was true  |
| `[ const string` | `verb ]` |  When the *commandline* argument contains a document pathname, the optional *verb* argument may contain the action to be performed on this document. The default action is *"open"*. Another useful verb is: *"print"*. In case this argument is supplied, the *waitFlag* argument will be ignored and the execution will always by asynchronous.  |

## Return values
| | |
|---|---|
| true | Application started successfully. |
| false | Application failed to start. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function is not supported in LN UI. See the [Implementing LN UI support](../webtop/htmlui_adoption.md) for more information.

## Related topics
- [Client file access overview](overview.md)

- [Client file access synopsis](synopsis.md)
