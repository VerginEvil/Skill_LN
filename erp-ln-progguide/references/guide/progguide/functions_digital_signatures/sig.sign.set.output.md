# sig.sign.set.output

## Syntax:
`#include <bic_sig>`
`function void sig.sign.set.output( long i.request, string i.document )`

## Description
Set the filename to which the signed document should be written.

## Arguments
| | | |
|---|---|---|
| `long` | `i.request` |  The handle to the signing request as returned by a previous call to [sig.init.sign.request](sig.init.sign.request.md)  |
| `string` | `i.document` |  The filename to which the document should be written.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)
- [Digital Signatures synopsis](synopsis.md)
- [Digital Signatures examples](examples.md)
