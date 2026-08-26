# seq.r.utc()

## Syntax:
`function long seq.r.utc( long fp, [ long byte.count ] )`

## Description
Reads a specified amount of bytes from the file. The bytes read from the file are interpreted as the two’s complement representation of a signed integer value.

## Arguments
| | | |
|---|---|---|
| `long` | `fp` |  The file pointer returned by [seq.open()](seq.open.md) when the particular file was opened. This function reads an amount of bytes from the file as specified by *byte.count*.  |
| `[ long` | `byte.count ]` |  Optional argument specifying the amount of bytes to be read from the file. Allowed values are 4, 5, and 8. Any other value is interpreted as 4. Default value is ByteCountOfUtc. According to the value of this argument, the (big endian) byte layout of the Utc32 mode, the Utc40 mode, or the Utc64 mode is used.  |

## Return values
| | |
|---|---|
| -1 |  Error, most probably *fp* is not a valid file pointer. The last system error is available in [predefined variable](../misc/predefined_variables.md) *e*. Notice that this error value -1 cannot be distinguished from normal value -1. This is problematic, unless it is known that value -1 is not expected as a normal value to be read from the file.  |
| >= -(256^ *byte.count*)/2 and < (256^ *byte.count*)/2  |  The numerical value of the bytes read from the supplied file. Typically, this is a (non-negative) UTC long format value stored earlier by the function [seq.w.utc()](seq.w.utc.md), or prepared by any other means. This function does not perform any value check.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.

## Related topics
- Related operations: [seq.r.long()](seq.r.long.md), [seq.r.short()](seq.r.short.md)
- Inverse operations: [seq.w.long()](seq.w.long.md), [seq.w.short()](seq.w.short.md), [seq.w.utc()](seq.w.utc.md)
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
- Universal Coordinated Time
- BitCountOfUtc
- ByteCountOfUtc
- Utc32 mode
- Utc40 mode
- Utc64 mode
