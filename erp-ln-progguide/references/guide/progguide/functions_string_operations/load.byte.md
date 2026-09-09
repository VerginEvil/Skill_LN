# load.byte()

## Syntax:
`function long load.byte( string record$ )`

## Description
The function load.byte() treats the supplied string merely as a sequence of bytes. The byte read from the string is interpreted as the 8-bit binary representation of an unsigned integer value.
The load.byte() function is machine independent and can be used (for example) in network communications.

## Arguments
| | | |
|---|---|---|
| `string` | `record$` |  String value of which the first byte is used as input bit pattern. It is an error to supply a string with a [byte capacity](../3gl_features/data_types.md#byte capacity) less than 1. In such a case, at least a log message will be generated. Above that, it may cause (now or in a future bshell version) the current 3GL process to be terminated. When a multibyte string is supplied, the behavior is undefined.  |

## Return values
The numerical value of the first byte of the supplied string. This is a value in the *unsigned* 8-bit range [0 … 2^8 - 1] (i.e. [0 … 255]).

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

| Load a byte from a string
string tmp(2)
long value
tmp = "S5"
value = load.byte( tmp )
| The variable value contains now the value 83
```

## Related topics
- [load.double()](load.double.md)

- [load.float()](load.float.md)

- [load.long()](load.long.md)

- [load.short()](load.short.md)

- [store.byte()](store.byte.md)

- [store.double()](store.double.md)

- [store.float()](store.float.md)

- [store.long()](store.long.md)

- [store.short()](store.short.md)

- [UTC](../functions_date_time_zones/overview.md#utc)

- [load.utc()](load.utc.md)

- [store.utc()](store.utc.md)

- [capacity in bytes](../3gl_features/data_types.md#byte capacity)

- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
