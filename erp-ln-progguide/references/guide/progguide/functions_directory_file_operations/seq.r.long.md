# seq.r.long()

## Syntax:
`function long seq.r.long( long fp )`

## Description
Reads a 32-bit value from the file. The 4 bytes read from the file are interpreted as the 32-bit two’s complement representation of a signed integer value.

## Arguments
| | | |
|---|---|---|
| `long` | `fp` |  The file pointer returned by [seq.open()](seq.open.md) when the particular file was opened. This function reads 4 bytes from the file.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *fp* is not a valid file pointer or end-of-file was reached. The last system error is available in [predefined variable](../misc/predefined_variables.md) *e*. Notice that this error value -1 cannot be distinguished from normal value -1. This is problematic, unless it is known that value -1 is not expected as a normal value to be read from the file. |
| >= -2^31 and < 2^31 | The numerical value of the 4 bytes read from the supplied file. This is a value in the signed 32-bit range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]). |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [seq.r.short()](seq.r.short.md)

- [seq.w.long()](seq.w.long.md)

- [seq.w.short()](seq.w.short.md)

- [UTC](../functions_date_time_zones/overview.md#utc)

- [seq.r.utc()](seq.r.utc.md)

- [seq.w.utc()](seq.w.utc.md)

- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
