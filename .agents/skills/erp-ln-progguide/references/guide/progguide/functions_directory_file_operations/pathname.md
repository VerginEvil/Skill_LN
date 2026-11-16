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
| Character | Description | file_type argument |
| d | data/domain definition | "D" |
| r | report | "O" |
| o | object | "O" |
| f | form | "S" |
| m | menu | "M" |
| p | program script | "P" |
| i | include file | "P" |
| b | additional files | "B" |
For example, when searching for a report, the file name specified must begin with 'r'. The name of the report object located begins with 'o'.

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
