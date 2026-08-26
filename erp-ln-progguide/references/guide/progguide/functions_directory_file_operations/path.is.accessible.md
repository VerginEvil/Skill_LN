# path.is.accessible()

## Syntax:
`function boolean path.is.accessible( string path_name )`

## Description
This checks if *path_name* exists and is available for writing.

## Arguments
| | | |
|---|---|---|
| `string` | `path_name` |  Path name.  |

## Return values
| | |
|---|---|
| false | *path_name* does not exist or is not available for writing.  |
| true | *path_name* exists and is available for writing.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2410.

## Example
```

field.path:
check.input:
      if not path.is.accessible(path) then
           set.input.error("ttadvd0005")
           |* Path is not allowed
      endif
before.zoom:
      if Filemanager.selectFile("", path, "", path) then
           display("path")
      endif
      choice.again()
```

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
