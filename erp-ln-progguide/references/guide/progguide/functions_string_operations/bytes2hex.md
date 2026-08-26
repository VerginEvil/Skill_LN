# bytes2hex()

## Syntax:
`function string bytes2hex( const string bytes, long length )`

## Description
Converts a string containing raw bytes to hex characters. Note that the length of the returned string becomes twice the length specified.

## Arguments
| | | |
|---|---|---|
| `const string` | `bytes` |  a string containing raw bytes  |
| `long` | `length` |  the number of bytes in the string; this is required as the string may contain \0 bytes  |

## Return values
a hexadecimal representation of the bytes in the specified string

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2100.

## Example
```

string	bytes(4)
string	hex(8)

| construct the Euro Sign € in UTF-T encoding
store.byte(0x9b, bytes(1))
store.byte(0xbc, bytes(2))
store.byte(0xc1, bytes(3))
store.byte(0xac, bytes(4))

| convert it to hex
hex = bytes2hex(bytes, 4)
| hex now contains "9bbcc1ac"
```

## Related topics
- Inverse operation: [hex2bytes()](hex2bytes.md)
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
