# sig.sign.set.key.info

## Syntax:
`#include <bic_sig>`
`function void sig.sign.set.key.info( long i.request, boolean i.on.hsm, long i.slot, string i.password, [ string i.alias ] )`

## Description
Set the information of the key to use to sign the document.

## Arguments
| | | |
|---|---|---|
| `long` | `i.request` |  The handle to the signing request as returned by a previous call to [sig.init.sign.request](sig.init.sign.request.md)  |
| `boolean` | `i.on.hsm` |  Indicates whether the key is stored on a Hardware Security Module or in a PKCS #12 key store.  |
| `long` | `i.slot` |  The slot number of the HSM which contains the user's token. If `i.on.hsm` is false, this parameter is ignored.  |
| `string` | `i.password` |  The password to access the token or key store.  |
| `[ string` | `i.alias ]` |  The alias of the key to use. This parameter is required when the token contains multiple keys.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)

- [Digital Signatures synopsis](synopsis.md)

- [Digital Signatures examples](examples.md)
