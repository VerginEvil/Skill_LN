# digest.update()

## Syntax:
`function long digest.update( long handle, string data, long data.size )`

## Description
Feeds data to the hash algorithm. This function can be called as many times as required to process the entire message. The third parameter can be used to explicitly specify the length of a binary string (when omitted, the logical length of the string argument is used).
When all your data has been fed into the update routine, use [digest.finalize())](digest.finalize.md) to obtain the resulting hash value.

## Arguments
| | | |
|---|---|---|
| `long` | `handle` |  A valid handle obtained by a previous call to [digest.initialize()](digest.initialize.md).  |
| `string` | `data` |  The data to compute the digest of. Can be any length.  |
| `long` | `data.size` |  Optional. The number of bytes to read from the data argument. When omitted, the length() function is used to obtain the number of bytes in *string*.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error. The specifics of the error are logged by the Bshell. The problem can be caused by the underlying OpenSSL function, an invalid buffer length (bigger than the actual length of string) or an invalid handle. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.

## Related topics
- [Secure Digest Functions overview](digest_overview.md)

- [Secure Digest Functions synopsis](digest_synopsis.md)
