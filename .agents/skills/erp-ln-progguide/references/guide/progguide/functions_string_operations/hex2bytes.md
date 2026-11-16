# hex2bytes()

## Syntax:
`function long hex2bytes( const string hex, ref string bytes )`

## Description
Converts a string of hexadecimal characters to bytes.

## Arguments
| | | |
|---|---|---|
| `const string` | `hex` |  a string containing hex characters, like "deadbeef" or "9b81c3bd"  |
| `ref string` | `bytes` |  the returned binary representation of the hex value; this string should be large enough to contain the result bytes (the size of the hex string divided by 2 is enough)  |

## Return values
>= 0: the number of bytes stored in parameter 'bytes'
-1: in case of an invalid hex string

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2100.

## Example
```

string	bytes(4)
long	numbytes

numbytes = hex2bytes("9bbcc1ac", bytes)
| numbytes is now 4
| bytes contains the binary representation of the hexadecimal characters, in this case the Euro Sign € in UTF-T encoding
```

## Related topics
- [bytes2hex()](bytes2hex.md)

- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
