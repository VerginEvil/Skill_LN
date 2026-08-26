# cipher.encrypt.update()

## Syntax:
`function long cipher.encrypt.update( long handle, ref string data.out, ref long data.out.size, const string data.in, long data.in.size )`

## Description
Feeds data to the encryption algorithm to be encrypted using the key (and optionally the IV) given in [cipher.encrypt.initialize()](cipher.encrypt.initialize.md).

## Arguments
| | | |
|---|---|---|
| `long` | `handle` |  A (valid) handle obtained by a previous call to [cipher.encrypt.initialize()](cipher.encrypt.initialize.md).  |
| `ref string` | `data.out` |  The output buffer that will receive the result of the encryption operation. It is the responsibility of the programmer to make sure that the buffer is big enough.  |
| `ref long` | `data.out.size` |  Receives the number of bytes written to the *data.out* buffer.  |
| `const string` | `data.in` |  The data that must be encrypted.  |
| `long` | `data.in.size` |  The number of bytes in the *data.in* buffer that must be encrypted (zero or more bytes). When this parameter is omitted, the value returned by *len(data.in)* is assumed. Warning: When handling binary data always pass the number of bytes.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error. The specifics of the error are logged by the Bshell. The problem can be caused by the underlying OpenSSL function, an invalid buffer length or an invalid handle.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.

## Related topics
- [Cipher Functions overview](cipher_overview.md)
- [Cipher Function synopsis](cipher_synopsis.md)
