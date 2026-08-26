# FileManager.selectFolder()

## Syntax:
`function long FileManager.selectFolder( [ string i.root.path ], string i.start.path, ref string o.folder )`

## Description
This shows the File Manager workbench running in folder selection mode to allow a user to select one folder on the server.

## Arguments
| | | |
|---|---|---|
| `[ string` | `i.root.path ]` |  when specified, the root directory for the File Manager workbench. A user can navigate to child directories but not to the parent of the root directory. Also, the start directory, i.start.path, must be located within the root directory otherwise the error message "Directory X is not a directory within Y" where X is the i.start.path and Y is the i.root.path. By default ${BSE} should be used a root directory.  |
| `string` | `i.start.path` |  The startup directory for the File Manager workbench. If i.start.path specifies a file instead of a directory, the directory part of i.start.path is used as startup directory. Note that if i.root.path is not specified or is empty, this startup directory becomes the root directory of the File Manager workbench. In case of an empty string the startup directory will be the directory where the Baan Software Environment is installed (see [bse.dir$](../functions_system_and_user_information/bse.dir.md)).  |
| `ref string` | `o.folder` |  Output argument which will contain the full path of the folder selected by the user.  |

## Return values
| | |
|---|---|
| 1 | The user has selected a folder. |
| 0 | The user has cancelled. |
| -1 | Error occurred |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2200.

## Examples
```

| Selecting a folder at a specific location:
function string select.folder()
{
|* This function returns the full path of a folder selected by a user.
|* The FileManager starts in the directory ${BSE}/appdata/import/companies with companies as its root entry.
|* The user cannot move to a parent directory of companies.

string	start.path(500) mb
string	selected.folder(500) mb

	start.path = "${BSE}/appdata/import/companies"
	if FileManager.selectFolder(start.path, selected.folder) <> 1 then
		selected.folder = ""
	endif
	return(selected.folder)
}

| Selecting a folder at a specific location but allowing the user to change to the parent or to sibling directories:
function string select.folder.with.root.dir()
{
|* This function returns the full path of a folder selected by a user.
|* The FileManager starts in the directory ${BSE}/appdata/import/companies with ${BSE} as its root entry.
|* The user can move to a parent or higher directory of companies but cannot move beyond ${BSE}.

string	root.path(500) mb
string	start.path(500) mb
string	selected.folder(500) mb

	root.path = "${BSE}"
	start.path = "${BSE}/appdata/import/companies"
	if FileManager.selectFolder(root.path, start.path, selected.folder) <> 1 then
		selected.folder = ""
	endif
	return(selected.folder)
}
```

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
