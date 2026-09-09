# sig.sign.set.document

## Syntax:
`#include <bic_sig>`
`function void sig.sign.set.document( long i.request, string i.document )`

## Description
Set the document to sign.

## Arguments
| | | |
|---|---|---|
| `long` | `i.request` |  The handle to the signing request as returned by a previous call to [sig.init.sign.request](sig.init.sign.request.md)  |
| `string` | `i.document` |  The path to the document to be signed. The document does not need to exist yet.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)

- [Digital Signatures synopsis](synopsis.md)

- [Digital Signatures examples](examples.md)
