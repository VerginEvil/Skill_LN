# dir.close()

## Syntax:
`function long dir.close( long dfd )`

## Description
This closes a specified directory and frees all memory allocated to it. The *dfd* argument is the pointer to the directory returned by [dir.open()](dir.open.md) or [dir.open.tree()](dir.open.tree.md) when the directory was opened.

## Arguments
| | | |
|---|---|---|
| `long` | `dfd` |  The pointer to the required directory, as returned when the directory was opened by [dir.open()](dir.open.md) or [dir.open.tree()](dir.open.tree.md).  |

## Return values
| | |
|---|---|
| >= 0 | Success. |
| -1 | Error; The system dependent error value is put in the e variable. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
