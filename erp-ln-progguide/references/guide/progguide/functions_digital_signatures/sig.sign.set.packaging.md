# sig.sign.set.packaging

## Syntax:
`#include <bic_sig>`
`function void sig.sign.set.packaging( long i.request, string i.packaging )`

## Description
Set the packaging method of the signature.

## Arguments
| | | |
|---|---|---|
| `long` | `i.request` |  The handle to the signing request as returned by a previous call to [sig.init.sign.request](sig.init.sign.request.md)  |
| `string` | `i.packaging` |  The packaging to be used for the signature. The applicable packaging formats depend on the signature format. Must be one of the following values (defined in `bic_sig`):  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)
- [Digital Signatures synopsis](synopsis.md)
- [Digital Signatures examples](examples.md)
