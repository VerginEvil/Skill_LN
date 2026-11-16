# digest.initialize()

## Syntax:
`function long digest.initialize( long digest.type )`

## Description
Initializes the state of the Secure Hash Algorithm and selects the apropriate Secure Hash algorithm.
Note: the older DIGEST_SHA algorithm (also known as SHA-0) has been removed from the bshell version 9.1c, TIV 2140, as versions of OpenSSL starting with 1.1.0c do not support the SHA digest anymore. The SHA-0 algorithm has been considered insecure ever since 1995.
If you use the DIGEST_SHA name, you will get a runtime error for compiled objects if this method is used and an intentional compilation error of 3GL objects when you try to compile a source containing it. You will have to alter your software to use one of the newer digest algorithms.
DIGEST_SHA384 is available only in bshells with a TIV higher or equal to 2510.

## Arguments
| | | |
|---|---|---|
| `long` | `digest.type` |  The name of the secure hash algorithm. This must be one of: DIGEST_MD5 DIGEST_SHA (invalid) DIGEST_SHA1 DIGEST_SHA224 DIGEST_SHA256 DIGEST_SHA384 DIGEST_SHA512 DIGEST_SHA3_224 DIGEST_SHA3_256 DIGEST_SHA3_384 DIGEST_SHA3_512  |

## Return values
A handle for this digest operation that must be used in subsequent calls to [digest.update()](digest.update.md) and [digest.finalize())](digest.finalize.md). The value -1 is returned upon error. Details of the error are logged by the bshell. The returned *Id* can only be used in the original process where digest.initialize was called, and is useless in other processes in the same bshell. The allocated memory is freed explicitly by passing the *Id* to digest.finalize(). The allocated memory is freed implicitly when the process exits. Any number of Secure Digest Algorithm states may be in use concurrently.

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.

## Related topics
- [Secure Digest Functions overview](digest_overview.md)

- [Secure Digest Functions synopsis](digest_synopsis.md)
