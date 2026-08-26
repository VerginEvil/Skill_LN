# sig.sign.execute.request

## Syntax:
`#include <bic_sig>`
`function long sig.sign.execute.request( long i.request )`

## Description
Execute the given request to sign a document.

## Arguments
| | | |
|---|---|---|
| `long` | `i.request` |  The handle to the signing request as returned by a previous call to [sig.init.sign.request](sig.init.sign.request.md)  |

## Return values
| | |
|---|---|
| 0 | The request was processed successfully. |
| DALHOOKERROR | The request failed. A DAL message has been set. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)
- [Digital Signatures synopsis](synopsis.md)
- [Digital Signatures examples](examples.md)
