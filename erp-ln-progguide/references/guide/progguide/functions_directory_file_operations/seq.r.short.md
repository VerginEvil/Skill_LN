# seq.r.short()

## Syntax:
`function long seq.r.short( long fp )`

## Description
Reads a 16-bit value from the file. The 2 bytes read from the file are interpreted as the 16-bit binary representation of an unsigned integer value.

## Arguments
| | | |
|---|---|---|
| `long` | `fp` |  The file pointer returned by [seq.open()](seq.open.md) when the particular file was opened. This function reads 2 bytes from the file.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *fp* is not a valid file pointer. The last system error is available in [predefined variable](../misc/predefined_variables.md) *e*.  |
| >= 0 | The numerical value of the 2 bytes read from the supplied file. This is a value in the *unsigned* 16-bit range [0 … 2^16 - 1] (i.e. [0 … 65,535]).  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- Related operations: [seq.r.long()](seq.r.long.md)
- Inverse operations: [seq.w.long()](seq.w.long.md), [seq.w.short()](seq.w.short.md)
- Special operations for UTC long format values: [seq.r.utc()](seq.r.utc.md), [seq.w.utc()](seq.w.utc.md)
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
