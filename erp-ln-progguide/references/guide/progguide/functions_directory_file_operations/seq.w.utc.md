# seq.w.utc()

## Syntax:
`function long seq.w.utc( long value, long fp, [ long byte.count ] )`

## Description
Writes an integer value into the file.
The function seq.w.utc() writes the *byte.count* least significant bytes of the two’s complement representation of the supplied integer value into the first *byte.count* bytes of the supplied file.
The inverse function [seq.r.utc()](seq.r.utc.md) will retrieve the original supplied integer value, wrapped to the signed *byte.count*-byte value range [-(256^ *byte.count*)/2 … (256^ *byte.count*)/2 - 1] by repeatedly adding or subtracting 256^ *byte.count* until the value is in the signed *byte.count*-byte value range.
More specifically, the inverse function [seq.r.utc()](seq.r.utc.md) will retrieve the exact original supplied integer value if and only if that integer value is within the signed *byte.count*-byte value range [-(256^ *byte.count*)/2 … (256^ *byte.count*)/2 - 1].

## Arguments
| | | |
|---|---|---|
| `long` | `value` |  The value to write into the file. Typically, this is a (non-negative) UTC long format value. In 64-bit mode, the bshell is less forgiving than in 32-bit mode. When the bshell is in 64-bit mode, it is a fatal error to supply a negative *value*. When the bshell is in 64-bit mode, it is a fatal error to supply a *value* which cannot be stored in the available *byte.count* bytes without loss of information. Typically, this is the case when *byte.count* is 4 and the supplied *value* is outside the signed 32-bit value range, i.e. is greater than 2,147,483,647 (0x7fff,ffff), which corresponds to January 19, 2038, 03:14:07 UTC. When the bshell is in 64-bit mode, it is a fatal error to supply a *value* which is a UTC long format value greater than the current maximum DB.TIME domain value. Typically, this maximum is 253,402,214,400 (0x3a,fff2,f000), which corresponds to the begin of the last day of the last four-digit year, i.e. December 31, 9999, 00:00:00 UTC.  |
| `long` | `fp` |  The file pointer returned by [seq.open()](seq.open.md) when the particular file was opened. This function writes an amount of bytes to the file as specified by *byte.count*.  |
| `[ long` | `byte.count ]` |  Optional argument specifying the amount of bytes to be written to the file. Allowed values are 4, 5, and 8. Any other value is interpreted as 4. Default value is ByteCountOfUtc. According to the value of this argument, the (big endian) byte layout of the Utc32 mode, the Utc40 mode, or the Utc64 mode is used.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *fp* is not a valid file pointer. The last system error is available in [predefined variable](../misc/predefined_variables.md) *e*.  |
| 0 | Success. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.

## Related topics
- Related operations: [seq.w.long()](seq.w.long.md), [seq.w.short()](seq.w.short.md)
- Inverse operations: [seq.r.long()](seq.r.long.md), [seq.r.short()](seq.r.short.md), [seq.r.utc()](seq.r.utc.md)
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
- Universal Coordinated Time
- BitCountOfUtc
- ByteCountOfUtc
- Utc32 mode
- Utc40 mode
- Utc64 mode
