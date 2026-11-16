# sig.sign.set.visual.representation.text.position

## Syntax:
`#include <bic_sig>`
`function void sig.sign.set.visual.representation.text.position( long i.request, long i.visual.representation, string i.horizontal.alignment, string i.position, [ string i.vertical.alignment ] )`

## Description
Set the alignment and position of the text in the visual representation. The position determines how the image and text are combined.

## Arguments
| | | |
|---|---|---|
| `long` | `i.request` |  The handle to the signing request as returned by a previous call to [sig.init.sign.request](sig.init.sign.request.md)  |
| `long` | `i.visual.representation` |  The handle to the visual representation as returned by a previous call to [sig.sign.set.visual.representation](sig.sign.set.visual.representation.md)  |
| `string` | `i.horizontal.alignment` |  The horizontal alignment of the text within the field. Must be one of the following values (defined in `bic_sig`): `ALIGN_LEFT` `ALIGN_CENTER` `ALIGN_RIGHT`  |
| `string` | `i.position` |  The position of the text when combined with an image. Must be one of the following values (defined in `bic_sig`): TEXT_TOP TEXT_BOTTOM TEXT_LEFT TEXT_RIGHT  |
| `[ string` | `i.vertical.alignment ]` |  The verticalal alignment of the text within the field. Must be one of the following values (defined in `bic_sig`): `ALIGN_TOP` `ALIGN_MIDDLE` `ALIGN_BOTTOM`  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)

- [Digital Signatures synopsis](synopsis.md)

- [Digital Signatures examples](examples.md)
