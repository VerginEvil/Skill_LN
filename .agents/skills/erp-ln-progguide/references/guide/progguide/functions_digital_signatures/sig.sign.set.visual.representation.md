# sig.sign.set.visual.representation

## Syntax:
`#include <bic_sig>`
`function long sig.sign.set.visual.representation( long i.request, string i.text, string i.image.path, string i.signature.field )`

## Description
Enable a visual representation of the signature in the document. The representation can be text, an image, or both. It is possible to fill in an existing signature field in the document, or to create a new signature field. Visual representations are only supported when signing a PDF document with format `PAdES`.

## Arguments
| | | |
|---|---|---|
| `long` | `i.request` |  The handle to the signing request as returned by a previous call to [sig.init.sign.request](sig.init.sign.request.md)  |
| `string` | `i.text` |  The text to show in the visual representation. May be empty.  |
| `string` | `i.image.path` |  The image to show in the visual representation. May be empty.  |
| `string` | `i.signature.field` |  The identifier of the existing, empty, signature field in the document. If empty, a new field will be created and [sig.sign.set.visual.representation.position](sig.sign.set.visual.representation.position.md) should be called.  |

## Return values
An identifier for this visual representation, required as input for other visual representation functions.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)

- [Digital Signatures synopsis](synopsis.md)

- [Digital Signatures examples](examples.md)
