# sig.sign.set.container

## Syntax:
`#include <bic_sig>`
`function void sig.sign.set.container( long i.request, string i.container )`

## Description
Set the container type of the signature.

## Arguments
| | |
|---|---|
| ASiC_S | Simple container. A single file is associated with a signature or timestamp. |
| ASiC_E | Extended container. Multiple signatures or timestamps can be present. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)

- [Digital Signatures synopsis](synopsis.md)

- [Digital Signatures examples](examples.md)
