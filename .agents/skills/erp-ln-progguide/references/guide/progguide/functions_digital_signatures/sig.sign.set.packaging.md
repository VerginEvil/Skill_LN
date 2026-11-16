# sig.sign.set.packaging

## Syntax:
`#include <bic_sig>`
`function void sig.sign.set.packaging( long i.request, string i.packaging )`

## Description
Set the packaging method of the signature.

## Arguments
| | |
|---|---|
| `Enveloped` | The signature becomes part of the document that was signed. |
| `Enveloping` | The document that was signed is contained in the signature. |
| `Detached` | The signature is separate from the document. The output file will only contain the signature. |
| `Internally_Detached` | Applies only to XAdES, both the document that was signed and the signature are enveloped with a new element. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)

- [Digital Signatures synopsis](synopsis.md)

- [Digital Signatures examples](examples.md)
