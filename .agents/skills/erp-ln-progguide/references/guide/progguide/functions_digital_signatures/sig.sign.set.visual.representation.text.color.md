# sig.sign.set.visual.representation.text.color

## Syntax:
`#include <bic_sig>`
`function void sig.sign.set.visual.representation.text.color( long i.request, long i.visual.representation, long i.foreground, long i.background )`

## Description
Set the foreground and background color of the text in the visual representation.

## Arguments
| | | |
|---|---|---|
| `long` | `i.request` |  The handle to the signing request as returned by a previous call to [sig.init.sign.request](sig.init.sign.request.md)  |
| `long` | `i.visual.representation` |  The handle to the visual representation as returned by a previous call to [sig.sign.set.visual.representation](sig.sign.set.visual.representation.md)  |
| `long` | `i.foreground` |  The foreground color.  |
| `long` | `i.background` |  The background color.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)

- [Digital Signatures synopsis](synopsis.md)

- [Digital Signatures examples](examples.md)
