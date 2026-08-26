# store.float()

## Syntax:
`function void store.float( double value, ref string rec$ )`

## Description
The function store.float() treats the supplied string merely as a sequence of bytes. The bytes written to the string are not the encoding of certain characters, but the encoding of the numerical value of the first argument of the function.
The function *store.float* writes four bytes to the supplied string, representing the four-byte encoding of the floating point value of its first argument.
The store.float() function is *not* machine independent and must be used with care in (for example) network communications.

## Arguments
| | | |
|---|---|---|
| `double` | `value` |  The value to write into the string.  |
| `ref string` | `rec$` |  String of which the first 4 bytes will be filled. Any further bytes of the string are left unchanged. It is an error to supply a string with a byte limit less than 4. In such a case, at least a log message will be generated. Above that, it may cause (now or in a future bshell version) the current 3GL process to be terminated. When a multibyte string is supplied, the behavior is undefined.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

| Store a float at position 1 in a string
string tmp(4)
store.float( 3.14, tmp )
| tmp(1;4) will now contain the float 3.14 (in the debugger it shows rubbish)
```

## Related topics
- Related operations: [store.byte()](store.byte.md), [store.double()](store.double.md), [store.long()](store.long.md), [store.short()](store.short.md)
- Inverse operations: [load.byte()](load.byte.md), [load.double()](load.double.md), [load.float()](load.float.md), [load.long()](load.long.md), [load.short()](load.short.md)
- Special operations for UTC long format values: [load.utc()](load.utc.md), [store.utc()](store.utc.md)
- Definition of the byte limit of a string variable: length limit in bytes
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
