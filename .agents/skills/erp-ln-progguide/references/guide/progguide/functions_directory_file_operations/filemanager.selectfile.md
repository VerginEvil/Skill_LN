# FileManager.selectFile()

## Syntax:
`function long FileManager.selectFile( [ string i.root.path ], string i.start.path, string i.mime.filter, ref string o.file )`

## Description
This shows the File Manager workbench running in file selection mode to allow a user to select a file on the server.

## Arguments
| | | |
|---|---|---|
| `[ string` | `i.root.path ]` |  when specified, the root directory for the File Manager workbench. A user can navigate to child directories but not to the parent of the root directory. Also, the start directory, i.start.path, must be located within the root directory otherwise the error message "Directory X is not a directory within Y" where X is the i.start.path and Y is the i.root.path.  |
| `string` | `i.start.path` |  The startup directory for the File Manager workbench. If i.start.path specifies a file instead of a directory, the directory part of i.start.path is used as startup directory. Note that if i.root.path is not specified or is empty, this startup directory becomes the root directory of the File Manager workbench. In case of an empty string the startup directory will be the directory where the Baan Software Environment is installed (see [bse.dir$](../functions_system_and_user_information/bse.dir.md)).  |
| `string` | `i.mime.filter` |  The list of mime types, separated by commas, of the files shown by the File Manager. If the list is an empty string all files are shown.  |
| `ref string` | `o.file` |  Output argument which will contain the full path of the file selected by the user.  |

## Return values
| | |
|---|---|
| 1 | The user has selected a file. |
| 0 | The user has cancelled. |
| -1 | Error occurred |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2200.

## Examples
```

| Selecting a file at a specific location:
function string select.file()
{
|* This function returns the full path of a file selected by a user.
|* The FileManager starts in the directory ${BSE}/appdata/import/companies with companies as its root entry.
|* The user cannot move to a parent directory of companies.

string	start.path(500) mb
string	selected.file(500) mb
string	mime.filter(100)

	start.path = "${BSE}/appdata/import/companies"
	mime.filter = ""
	if FileManager.selectFile(start.path, mime.filter, selected.file) <> 1 then
		selected.file = ""
	endif
	return(selected.file)
}

| Selecting a file at a specific location but allowing the user to change to the parent or to sibling directories:
function string select.file.with.root.dir()
{
|* This function returns the full path of a file selected by a user.
|* The FileManager starts in the directory ${BSE}/appdata/import/companies with ${BSE} as its root entry.
|* The user can move to a parent or higher directory of companies but cannot move beyond ${BSE}.

string	root.path(500) mb
string	start.path(500) mb
string	mime.filter(100)
string	selected.file(500) mb

	root.path = "${BSE}"
	start.path = "${BSE}/appdata/import/companies"
	mime.filter = ""
	if FileManager.selectFile(root.path, start.path, mime.filter, selected.file) <> 1 then
		selected.file = ""
	endif
	return(selected.file)
}

| Selecting a file of a specific type in a specific directory and allowing the user to move to parent/sibling directories:
#include <bic_desktop>
function string select.file.with.root.dir.and.filter()
{
|* This function returns the full path of a zip file selected by a user.
|* The FileManager starts in the directry ${BSE}/appdata/import/companies with ${BSE} as its root entry.
|* The user can move to a parent or higher directory of companies but cannot move beyond ${BSE}.
|* The FileManager only shows zip files.

string	root.path(500) mb
string	start.path(500) mb
string	mime.filter(100)
string	selected.file(500) mb

	root.path = "${BSE}"
	start.path = "${BSE}/appdata/import/companies/"
	mime.filter = client.get.media.type(".zip")
	if FileManager.selectFile(root.path, start.path, mime.filter, selected.file) <> 1 then
		selected.file = ""
	endif
	return(selected.file)
}
```

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
