# load.float()

## Syntax:
`function double load.float( string record$, [ long swap ] )`

## Description
The function load.float() treats the supplied string merely as a sequence of bytes, without trying to interpret that sequence of bytes as the encoding of a sequence of characters. Instead, the bytes are interpreted as the encoding of numerical values.
The function *load.float* returns the numerical value of the first four bytes of the supplied string, interpreted as the four-byte encoding of a floating point value.
The load.float() function is *not* machine independent and must be used with care in (for example) network communications.

## Arguments
| | | |
|---|---|---|
| `string` | `record$` |  String value of which the first 4 bytes are used as input bit pattern. It is an error to supply a string with a byte limit less than 4. In such a case, at least a log message will be generated. Above that, it may cause (now or in a future bshell version) the current 3GL process to be terminated. When a multibyte string is supplied, the behavior is undefined.  |
| `[ long` | `swap ]` |  This function assumes that the data in *record$* is stored in *machine dependent* format. To compensate for a difference in the endianess of the data and the host running the program set this optional argument to 1. In effect all four byte will be swapped.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

| Load a float from a string
string tmp(4)
double value
store.float(3.14,tmp)
value = load.float( tmp )
| The variable value contains now the value 3.14
```

## Related topics
- Related operations: [load.byte()](load.byte.md), [load.double()](load.double.md), [load.long()](load.long.md), [load.short()](load.short.md)
- Inverse operations: [store.byte()](store.byte.md), [store.double()](store.double.md), [store.float()](store.float.md), [store.long()](store.long.md), [store.short()](store.short.md)
- Special operations for UTC long format values: [load.utc()](load.utc.md), [store.utc()](store.utc.md)
- Definition of the byte limit of a string variable: length limit in bytes
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
