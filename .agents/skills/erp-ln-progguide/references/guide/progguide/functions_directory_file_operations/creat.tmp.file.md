# creat.tmp.file$()

## Syntax:
`function string creat.tmp.file$( [ string pathname ] )`

## Description
This creates a temporary file. The optional *pathname* argument may be used to specify the full path to the directory where the file is to be placed.
When *pathname* is omitted or left empty, the file is created in the current directory.
In UNIX environments, a unique temporary file is created with UNIX-privilege mode 0664.

## Arguments
| | | |
|---|---|---|
| `[ string` | `pathname ]` |    |

## Return values
The name of the temporary file.

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  It is recommended that you use this function in conjunction with the BSE_TMP environment variable. You can use the function [bse.tmp.dir$()](../functions_system_and_user_information/bse.tmp.dir.md) to retrieve the name of the directory defined by this variable. For example:
`creat.tmp.file$( bse.tmp.dir$() )`

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
