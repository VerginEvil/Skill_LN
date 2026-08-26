# cipher.encrypt.finalize()

## Syntax:
`function long cipher.encrypt.finalize( long handle, string data.out, long data.out.length )`

## Description
Most cipher algorithms operate in block mode, which means the output is always a multiple of the block size. Because the input is not necessarily a multiple of that block size, this function returns the last (partial) block. It also frees up the resources that are used by the encryption and invalidates (closes) the *handle*.

## Arguments
| | | |
|---|---|---|
| `long` | `handle` |  A valid handle obtained from a previous call to [cipher.encrypt.initialize()](cipher.encrypt.initialize.md). Also, some data should have been encrypted using [cipher.encrypt.update()](cipher.encrypt.update.md).  |
| `string` | `data.out` |  The output buffer. This buffer must be big enough to hold the result.  |
| `long` | `data.out.length` |  The number of bytes written to the *data.out* buffer.  |

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
