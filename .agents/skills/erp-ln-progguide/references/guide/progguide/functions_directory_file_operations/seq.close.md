# seq.close()

## Syntax:
`function long seq.close( long fp )`

## Description
This flushes the buffers associated with the specified file and closes the file. *fp* is the file pointer returned by [seq.open()](seq.open.md) when the file was opened. Buffers allocated by the standard i/o system are also flushed and closed. These actions are performed automatically when the process exits.

## Arguments
| | | |
|---|---|---|
| `long` | `fp` |  fp is the file pointer returned by seq.open() when the file was opened..  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error. Probably *fp* not connected. (the last system error is available in the e variable - for example, for file system full, e will be ENOSPC (that is, 28) - for a list of error codes, see [Infor ES errors and messages](../errors/overview.md)) |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
