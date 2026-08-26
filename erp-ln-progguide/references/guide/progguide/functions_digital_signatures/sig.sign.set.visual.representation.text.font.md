# sig.sign.set.visual.representation.text.font

## Syntax:
`#include <bic_sig>`
`function long sig.sign.set.visual.representation.text.font( long i.request, long i.visual.representation, string i.name, long i.size, boolean i.bold, boolean i.italic, boolean i.underline )`

## Description
Set the font settings for the text of the visual representation.

## Arguments
| | | |
|---|---|---|
| `long` | `i.request` |  The handle to the signing request as returned by a previous call to [sig.init.sign.request](sig.init.sign.request.md)  |
| `long` | `i.visual.representation` |  The handle to the visual representation as returned by a previous call to [sig.sign.set.visual.representation](sig.sign.set.visual.representation.md)  |
| `string` | `i.name` |  The name of the font, as defined in the Fonts session.  |
| `long` | `i.size` |  The font size, in points.  |
| `boolean` | `i.bold` |  |
| `boolean` | `i.italic` |  |
| `boolean` | `i.underline` |  |

## Return values
| | |
|---|---|
| 0 | The request was modified successfully |
| `DALHOOKERROR` | The font cannot be found. A DAL message has been set. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)
- [Digital Signatures synopsis](synopsis.md)
- [Digital Signatures examples](examples.md)
