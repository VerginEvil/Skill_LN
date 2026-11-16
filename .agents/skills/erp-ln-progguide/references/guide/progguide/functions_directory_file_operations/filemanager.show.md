# FileManager.show()

## Syntax:
`function void FileManager.show( [ string i.root.path ], string i.start.path, string i.mime.filter )`

## Description
This starts the File Manager workbench running in modeless mode.

## Arguments
| | | |
|---|---|---|
| `[ string` | `i.root.path ]` |  when specified, the root directory for the File Manager workbench. A user can navigate to child directories but not to the parent of the root directory. Also, the start directory, i.start.path, must be located within the root directory otherwise the error message "Directory X is not a directory within Y" where X is the i.start.path and Y is the i.root.path.  |
| `string` | `i.start.path` |  The startup directory for the File Manager workbench. If i.start.path specifies a file instead of a directory, the directory part of i.start.path is used as startup directory. Note that if i.root.path is not specified or is empty, this startup directory becomes the root directory of the File Manager workbench. In case of an empty string the startup directory will be the directory where the Baan Software Environment is installed (see [bse.dir$](../functions_system_and_user_information/bse.dir.md)).  |
| `string` | `i.mime.filter` |  The list of mime types, separated by commas, of the files shown by the File Manager. If the list is an empty string all files are shown.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2310.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
