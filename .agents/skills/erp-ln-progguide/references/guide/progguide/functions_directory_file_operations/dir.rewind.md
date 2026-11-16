# dir.rewind()

## Syntax:
`function long dir.rewind( long dfd )`

## Description
This resets the read pointer of the specified directory to the beginning of the directory entry list. The *dfd* argument is the pointer to the directory returned by [dir.open()](dir.open.md) or [dir.open.tree()](dir.open.tree.md) when the directory was opened.

## Arguments
| | | |
|---|---|---|
| `long` | `dfd` |  Pointer to the directory returned by dir.open() or dir.open.tree() when the directory was opened.  |

## Return values
| | |
|---|---|
| > 0 | Success; A pointer to the directory data. |
| -1 | Error. Bad directory descriptor. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
