# sig.sign.set.visual.representation.image.alignment

## Syntax:
`#include <bic_sig>`
`function void sig.sign.set.visual.representation.image.alignment( long i.request, long i.visual.representation, string i.vertical )`

## Description
Set the vertical alignment of the image in the visual representation. This affects the alignment when the text is higher than the image and the image and text are next to each other.

## Arguments
| | | |
|---|---|---|
| `long` | `i.request` |  The handle to the signing request as returned by a previous call to [sig.init.sign.request](sig.init.sign.request.md)  |
| `long` | `i.visual.representation` |  The handle to the visual representation as returned by a previous call to [sig.sign.set.visual.representation](sig.sign.set.visual.representation.md)  |
| `string` | `i.vertical` |  The vertical alignment. Must be one of the following values (defined in `bic_sig`): `ALIGN_TOP` `ALIGN_MIDDLE` `ALIGN_BOTTOM`  |
-
-
-

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)
- [Digital Signatures synopsis](synopsis.md)
- [Digital Signatures examples](examples.md)
