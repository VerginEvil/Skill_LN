# pathname()

## Syntax:
`function long pathname( string file_basename, string file_type, ref string file_path, [ long log.options ] )`

## Description
This searches for and returns the location of a specified file.
The function uses the file $BSE/lib/fd *ver.pack_combination* to find the file. *ver* refers to a particular release of the software; *pack_combination* refers to a particular package combination.
It is not necessary to use this function within functions such as db.bind(). These also use the file $BSE/lib/fd *ver.pack_combination* to search for a path name.

## Arguments
| | | |
|---|---|---|
| `string` | `file_basename` |  The name of the file that must be found. The file name must begin with *xppmmm* where *pp* is a package code, *mmm* is a module code, and *x* is a single character that corresponds to the file type, as shown in column one of the following table:  |
| `string` | `file_type` |  The file type. Use the values shown in column three of the above table.  |
| `ref string` | `file_path` |  This returns the full path to the specified file. If the file is not found, it returns the full path (including filename) where the file should be created. If the *file_type* is unknown, or *file_basename* starts with an invalid character, this argument returns the value of *file_basename*.  |
| `[ long` | `log.options ]` |  PATHNAME.NOLOG: Do not log errors in $BSE/log PATHNAME.LOG: Do log errors in $BSE/log (default)  |

## Return values
| | |
|---|---|
| 0 | Success. |
| ENOENT | File not found. |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  Language codes are relevant to reports, forms, and menus. You can specify the language code for a report, form, or menu file by appending it to the file name (that is, adding it as the 16 character). If you do not include this, the current language is assumed.

## Example
```

string file_path(256)
if pathname( "rpctst121200010", "O", file_path ) <> 0 then
                message( "File not found, must be created in %s",
                         file_path )
endif
```

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
