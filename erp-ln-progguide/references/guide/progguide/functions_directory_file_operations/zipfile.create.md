# zipfile.create()

## Syntax:
`function long zipfile.create( const string zipfile, const string entry )`

## Description
Creates a zip file for the specified entry. This may be a file or a directory. In case of a directory, all files and subdirectories in that directory are added to the zip file. In case the zip file already exists, it is overwritten.

## Arguments
| | | |
|---|---|---|
| `const string` | `zipfile` |  the full name of the zip file to create  |
| `const string` | `entry` |  the file or directory create the zip file for; in case of directories, all sub directories and files are taken into account as well  |

## Return values
| | |
|---|---|
| 0 | OK, success. |
| <> 0 | When an error occurred. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  Java methodes in domain com.infor.ln.dom.zip are used for the implementation.
This function is available from [TIV](../tiv/tiv_overview.md) [1900](../tiv/tiv_1900.md).

## Example
```

#define PATH_MAXLEN 	1024
long	result
string	srcedir(PATH_MAXLEN)
string	trgtdir(PATH_MAXLEN)
string	zipfile(PATH_MAXLEN)

	srcedir = path.combine(getenv$("HOME"), "source")
	trgtdir = path.combine(getenv$("HOME"), "zip archive")
	zipfile = path.combine(trgtdir, "target.zip")

	| archive directory source to target
	result = zipfile.create(zipfile, srcedir)
	if result <> 0 then
		message("Error while creating zipfile")
	endif
```

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
