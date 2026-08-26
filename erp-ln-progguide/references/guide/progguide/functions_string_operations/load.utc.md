# load.utc()

## Syntax:
`function long load.utc( string record$, [ long endian, long byte.count ] )`

## Description
The function load.utc() treats the supplied string merely as a sequence of bytes. The bytes read from the string are interpreted as the two’s complement representation of a signed integer value.
The load.utc() function is machine independent and can be used (for example) in network communications.

## Arguments
| | | |
|---|---|---|
| `string` | `record$` |  String value of which the first *byte.count* bytes are used as input bit pattern. It is an error to supply a string with a byte limit less than *byte.count*. In such a case, at least a log message will be generated. Above that, it may cause (now or in a future bshell version) the current 3GL process to be terminated. When a multibyte string is supplied, the behavior is undefined.  |
| `[ long` | `endian ]` |  Optional argument indicating the byte order (big endian or little endian) to be used. According to the value of this argument, either the little endian byte layout or the big endian byte layout of the Utc32 mode, the Utc40 mode, or the Utc64 mode is used. Value 1 indicates that little endian byte order must be used. Any other value indicates that big endian byte order must be used. Default behavior is to use big endian byte order.  |
| `[ long` | `byte.count ]` |  Optional argument specifying the amount of bytes to be read from *record$*. Allowed values are 4, 5, and 8. Any other value is interpreted as 4. Default value is ByteCountOfUtc. According to the value of this argument, the byte layout of the Utc32 mode, the Utc40 mode, or the Utc64 mode is used. If this optional argument is used, then first the *endian* argument must be supplied.  |

## Return values
The numerical value of the bytes read from the supplied string. This is a value in the signed *byte.count*-byte range [-(256^ *byte.count*)/2 … (256^ *byte.count*)/2 - 1].
Typically, this is a (non-negative) UTC long format value stored earlier by the function [store.utc()](store.utc.md), or prepared by any other means.
This function does not perform any value check.

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.

## Related topics
- Related operations: [load.byte()](load.byte.md), [load.double()](load.double.md), [load.float()](load.float.md), [load.long()](load.long.md), [load.short()](load.short.md)
- Inverse operations: [store.byte()](store.byte.md), [store.double()](store.double.md), [store.float()](store.float.md), [store.long()](store.long.md), [store.short()](store.short.md), [store.utc()](store.utc.md)
- Definition of the byte limit of a string variable: length limit in bytes
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
- Universal Coordinated Time
- BitCountOfUtc
- ByteCountOfUtc
- Utc32 mode
- Utc40 mode
- Utc64 mode
