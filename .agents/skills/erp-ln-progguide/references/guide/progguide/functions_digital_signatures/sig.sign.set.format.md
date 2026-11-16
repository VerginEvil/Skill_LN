# sig.sign.set.format

## Syntax:
`#include <bic_sig>`
`function void sig.sign.set.format( long i.request, string i.format )`

## Description
Set the format to use for the signature.

## Arguments
| | |
|---|---|
| `CAdES` | Based on Cryptographic Message Syntax, can be used to sign any data. |
| `PAdES` | Specific for PDF documents. |
| `XAdES` | Specific for XML documents. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)

- [Digital Signatures synopsis](synopsis.md)

- [Digital Signatures examples](examples.md)
