# zipfile.extract()

## Syntax:
`function long zipfile.extract( const string zipfile, const string dir )`

## Description
Extracts all files from a zip file to the specified directory. Any files in the zip file that already exist in the specified directory, will be overwritten. In case the extracted files are to be removed after processing them, it is advised to extract the files to a just created temporary directory, which can be removed when no longer needed. See rmdir() for more information regarding removing a directory structure.

## Arguments
| | | |
|---|---|---|
| `const string` | `zipfile` |  the full name of the zip file to extract from  |
| `const string` | `dir` |  the directory to extract the contents to  |

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


	srcedir = path.combine(getenv$("HOME"), "sources")
	trgtdir = path.combine(getenv$("HOME"), "zip archive")
	zipfile = path.combine(trgtdir, "target.zip")

	result = zipfile.extract(zipfile, srcedir)
	if result <> 0 then
		message("Error while extracting zipfile")
	endif
```

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
