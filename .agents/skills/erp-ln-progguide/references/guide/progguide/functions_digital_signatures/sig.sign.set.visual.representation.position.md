# sig.sign.set.visual.representation.position

## Syntax:
`#include <bic_sig>`
`function void sig.sign.set.visual.representation.position( long i.request, long i.visual.representation, long i.xpos, long i.ypos, [ long i.width, long i.height ] )`

## Description
Set the position of the visual representation field, if an existing field was not used. Units are in points, with the origin at the top-left corner of the page. The signature will always be created on the first page of the document. The size is optional, if not set, the visual representation will be resized to fit its contents.

## Arguments
| | | |
|---|---|---|
| `long` | `i.request` |  The handle to the signing request as returned by a previous call to [sig.init.sign.request](sig.init.sign.request.md)  |
| `long` | `i.visual.representation` |  The handle to the visual representation as returned by a previous call to [sig.sign.set.visual.representation](sig.sign.set.visual.representation.md)  |
| `long` | `i.xpos` |  The horizontal position of the field.  |
| `long` | `i.ypos` |  The vertical position of the field.  |
| `[ long` | `i.width ]` |  The width of the field.  |
| `[ long` | `i.height ]` |  The height of the field.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)

- [Digital Signatures synopsis](synopsis.md)

- [Digital Signatures examples](examples.md)
