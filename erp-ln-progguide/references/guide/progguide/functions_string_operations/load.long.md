# load.long()

## Syntax:
`function long load.long( string record$, [ long endian ] )`

## Description
The function load.long() treats the supplied string merely as a sequence of bytes. The 4 bytes read from the string are interpreted as the 32-bit two’s complement representation of a signed integer value.
The load.long() function is machine independent and can be used (for example) in network communications.

## Arguments
| | | |
|---|---|---|
| `string` | `record$` |  String value of which the first 4 bytes are used as input bit pattern. It is an error to supply a string with a byte limit less than 4. In such a case, at least a log message will be generated. Above that, it may cause (now or in a future bshell version) the current 3GL process to be terminated. When a multibyte string is supplied, the behavior is undefined.  |
| `[ long` | `endian ]` |  Optional argument indicating the byte order (big endian or little endian) to be used. Value 1 indicates that little endian byte order must be used. Any other value indicates that big endian byte order must be used. Default behavior is to use big endian byte order.  |

## Return values
The numerical value of the first 4 bytes of the supplied string. This is a value in the signed 32-bit range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]).

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

| Load a long from a string
string tmp(4)
long value
tmp = "cafe"
value = load.long( tmp )
| The variable value contains now the value 1667327589
```

## Related topics
- Related operations: [load.byte()](load.byte.md), [load.double()](load.double.md), [load.float()](load.float.md), [load.short()](load.short.md)
- Inverse operations: [store.byte()](store.byte.md), [store.double()](store.double.md), [store.float()](store.float.md), [store.long()](store.long.md), [store.short()](store.short.md)
- Special operations for UTC long format values: [load.utc()](load.utc.md), [store.utc()](store.utc.md)
- Definition of the byte limit of a string variable: length limit in bytes
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
