# sig.sign.set.string

## Syntax:
`#include <bic_sig>`
`function void sig.sign.set.string( long i.request, string i.string )`

## Description
Set the string to be signed. An MD5 hash of the signed string value is created, which can be retrieved by calling [sig.sign.get.output.string](sig.sign.get.output.string.md).

## Arguments
| | | |
|---|---|---|
| `long` | `i.request` |  The handle to the signing request as returned by a previous call to [sig.init.sign.request](sig.init.sign.request.md)  |
| `string` | `i.string` |  The string to be signed.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)

- [Digital Signatures synopsis](synopsis.md)

- [Digital Signatures examples](examples.md)
