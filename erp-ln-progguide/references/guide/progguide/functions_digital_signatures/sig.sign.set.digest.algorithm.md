# sig.sign.set.digest.algorithm

## Syntax:
`#include <bic_sig>`
`function void sig.sign.set.digest.algorithm( long i.request, string i.digest )`

## Description
Set the digest algorithm used to generate a fingerprint of the document.

## Arguments
| | | |
|---|---|---|
| `long` | `i.request` |  The handle to the signing request as returned by a previous call to [sig.init.sign.request](sig.init.sign.request.md)  |
| `string` | `i.digest` |  The hash function to use. Must be one of the following values (defined in `bic_sig`): `SHA1` `SHA224` `SHA256` `SHA384` `SHA512` `SHA3_224` `SHA3_256` `SHA3_384` `SHA3_512` `RIPEMD160` `MD2` `MD5`  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)

- [Digital Signatures synopsis](synopsis.md)

- [Digital Signatures examples](examples.md)
