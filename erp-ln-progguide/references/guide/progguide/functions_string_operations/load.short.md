# load.short()

## Syntax:
`function long load.short( string record$, [ long endian ] )`

## Description
The function load.short() treats the supplied string merely as a sequence of bytes. The 2 bytes read from the string are interpreted as the 16-bit two’s complement representation of a signed integer value.
The load.short() function is machine independent and can be used (for example) in network communications.

## Arguments
| | | |
|---|---|---|
| `string` | `record$` |  String value of which the first 2 bytes are used as input bit pattern. It is an error to supply a string with a byte limit less than 2. In such a case, at least a log message will be generated. Above that, it may cause (now or in a future bshell version) the current 3GL process to be terminated. When a multibyte string is supplied, the behavior is undefined.  |
| `[ long` | `endian ]` |  Optional argument indicating the byte order (big endian or little endian) to be used. Value 1 indicates that little endian byte order must be used. Any other value indicates that big endian byte order must be used. Default behavior is to use big endian byte order.  |

## Return values
The numerical value of the first 2 bytes of the supplied string. This is a value in the signed 16-bit range [-2^15 … 2^15 - 1] (i.e. [-32,768 … 32,767]).

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

| Load a short from a string
string tmp(2)
long value
tmp = "S5"
value = load.short( tmp )
| The variable value contains now the value 21301
```

## Related topics
- Related operations: [load.byte()](load.byte.md), [load.double()](load.double.md), [load.float()](load.float.md), [load.long()](load.long.md)
- Inverse operations: [store.byte()](store.byte.md), [store.double()](store.double.md), [store.float()](store.float.md), [store.long()](store.long.md), [store.short()](store.short.md)
- Special operations for UTC long format values: [load.utc()](load.utc.md), [store.utc()](store.utc.md)
- Definition of the byte limit of a string variable: length limit in bytes
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
