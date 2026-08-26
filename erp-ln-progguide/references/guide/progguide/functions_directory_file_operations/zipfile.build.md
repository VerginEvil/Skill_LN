# zipfile.build()

## Syntax:
`function long zipfile.build( long zipinfo )`

## Description
Builds a zip file based on the specified zipinfo object.

## Arguments
| | | |
|---|---|---|
| `long` | `zipinfo` |  a list with entries to add to the zip file; both directories and files are allowed; in case of directories, all sub directories and files are taken into account as well  |

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
long	handle
long	result
string	trgtdir(PATH_MAXLEN)
string	zipfile(PATH_MAXLEN)


	trgtdir = path.combine(getenv$("HOME"), "zip archive")
	zipfile = path.combine(trgtdir, "target.zip")

	| add selection to zipinfo
	handle = zipinfo.new(zipfile)
	if handle = 0 then
		message("Error while creating new zipinfo")
	endif

	zipinfo.add(handle, "dirname1")			| existing directory
	zipinfo.add(handle, "dirname2", TDIR)		| existing directory
	zipinfo.add(handle, "file01")			| existing file01
	zipinfo.add(handle, "file02", TFILE)		| existing file02

	| archive zipinfo to target
	result = zipfile.build(handle)
	if result <> 0 then
		message("Error while building zipfile")
	endif

	| clean up
	zipinfo.delete(handle)
```

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
