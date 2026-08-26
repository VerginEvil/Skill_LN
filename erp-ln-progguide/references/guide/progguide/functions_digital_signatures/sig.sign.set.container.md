# sig.sign.set.container

## Syntax:
`#include <bic_sig>`
`function void sig.sign.set.container( long i.request, string i.container )`

## Description
Set the container type of the signature.

## Arguments
| | | |
|---|---|---|
| `long` | `i.request` |  The handle to the signing request as returned by a previous call to [sig.init.sign.request](sig.init.sign.request.md)  |
| `string` | `i.container` |  The container type to be used for the signature. Must be one of the following values (defined in `bic_sig`):  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)
- [Digital Signatures synopsis](synopsis.md)
- [Digital Signatures examples](examples.md)
