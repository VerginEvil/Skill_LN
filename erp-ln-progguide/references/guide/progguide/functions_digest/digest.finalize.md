# digest.finalize())

## Syntax:
`function long digest.finalize( long handle, ref string result )`

## Description
After the last data has been fed into the hash-algorithm using [digest.update()](digest.update.md), the *digest.finalize* function can be used to retrieve the resulting hash value.

## Arguments
| | | |
|---|---|---|
| `long` | `handle` |  A valid handle obtained by a previous call to [digest.initialize()](digest.initialize.md).  |
| `ref string` | `result` |  The calculated digest. The format is in "raw hex", a string of upper-case hexadecimal digits. The length depends on the algorithm chosen with [digest.initialize()](digest.initialize.md).  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error. The specifics of the error are logged by the Bshell. The problem can be caused by the underlying OpenSSL function, a *result* string that is too small to hold the result or an invalid *handle*.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.

## Related topics
- [Secure Digest Functions overview](digest_overview.md)
- [Secure Digest Functions synopsis](digest_synopsis.md)
