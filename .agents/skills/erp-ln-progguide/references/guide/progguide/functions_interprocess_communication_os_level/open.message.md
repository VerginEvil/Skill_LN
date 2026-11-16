# open.message()

## Syntax:
`function long open.message( long project, string name$, long action, [ long fast ] )`

## Description
Use this to create a new mailbox or to connect to an existing mailbox. You must call this function before you can read from or write to the mailbox.

## Arguments
| | | |
|---|---|---|
| `long` | `project` |  A number in the range 1 to 255 that indicates the project to which the mailbox belongs.  |
| `string` | `name$` |  This identifies a particular mailbox within the specified project. The argument must contain the name of a file that can be read by all processes that want to use the mailbox. The function uses the specified project number and some attribute of the specified file to generate a mailbox key that uniquely identifies the mailbox. The contents of the file are not used or changed by the function. Note that within a project, the specified file must be clearly associated with a particular mailbox.  |
| `long` | `action` |  This argument can have one of the following values: 0 If the mailbox does not already exist, a new one is created. 1 This is similar to 0, except that instead of using a file name specified in *name$*, the system creates a unique file name ("$BSE/TMP/PostB<pid>"). When specifying this option, specify *name$* as an empty string (""). 2 If the mailbox does not already exist, a new one is not created.  |
| `[ long` | `fast ]` |  Set this optional argument to 1 if you are using the UNIX message queue ID instead of the mailbox key to identify the mailbox.  |

## Return values
This returns a unique key for the opened mailbox. It returns -1 if an error occurs (the predefined variable *e* contains the error number).

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Interprocess communication (OS level) overview](overview.md)

- [Interprocess communication (OS level) synopsis](synopsis.md)
