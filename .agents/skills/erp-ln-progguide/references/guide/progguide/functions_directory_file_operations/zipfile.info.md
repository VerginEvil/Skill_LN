# zipfile.info()

## Syntax:
`function long zipfile.info( const string zipfile )`

## Description
Retrieves a zipinfo object providing information regarding all entries in a zipfile.

## Arguments
| | | |
|---|---|---|
| `const string` | `zipfile` |  the full name of the zip file to retrieve the info from  |

## Return values
| | |
|---|---|
| <> 0 | a handle to a zipinfo object |
| 0 | in case of failure. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  This function is available from [TIV](../tiv/tiv_overview.md) [1900](../tiv/tiv_1900.md).

## Example
```

string	trgtdir(PATH_MAXLEN)
string	zipfile(PATH_MAXLEN)
string	entry(PATH_MAXLEN)

long	info
	trgtdir = path.combine(getenv$("HOME"), "zip archive")
	zipfile = path.combine(trgtdir, "target.zip")

	info = zipfile.info(zipfile)

	if zipinfo.first(info, entry, type) then
		repeat
			if type = TFILE then
				|... process compressed file
			endif
			if type = TDIR then
				|... process compressed directory
			endif
		until result < 0 or not zipinfo.next(info, entry, type)
	endif

	zipinfo.delete(info)
```

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
