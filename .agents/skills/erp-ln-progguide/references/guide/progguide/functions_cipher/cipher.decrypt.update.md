# cipher.decrypt.update()

## Syntax:
`function long cipher.decrypt.update( long handle, string data.out, long data.out.size, string data.in, long data.in.size )`

## Description
Feeds data to the decryption algorithm to be decrypted using the key (and optionally IV) given in [cipher.decrypt.initialize()](cipher.decrypt.initialize.md).

## Arguments
| | | |
|---|---|---|
| `long` | `handle` |  A (valid) handle obtained by a previous call to [cipher.decrypt.initialize()](cipher.decrypt.initialize.md).  |
| `string` | `data.out` |  The output buffer that will receive the result of the decryption operation. It is the responsibility of the programmer to make sure that the buffer is big enough.  |
| `long` | `data.out.size` |  Receives the number of bytes written to the *data.out* buffer.  |
| `string` | `data.in` |  The data that must be decrypted.  |
| `long` | `data.in.size` |  The number of bytes in the *data.in* buffer that must be decrypted (zero or more bytes). When this parameter is omitted, the value returned by *len(data.in)* is assumed. Warning: When handling binary data always pass the number of bytes.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error. The specifics of the error are logged by the Bshell. The problem can be caused by the underlying OpenSSL function, an invalid buffer length or an invalid handle. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.

## Related topics
- [Cipher Functions overview](cipher_overview.md)

- [Cipher Function synopsis](cipher_synopsis.md)
