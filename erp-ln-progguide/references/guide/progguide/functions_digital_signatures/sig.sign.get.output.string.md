# sig.sign.get.output.string

## Syntax:
`#include <bic_sig>`
`function string sig.sign.get.output.string( long i.request )`

## Description
Get the MD5 hash of the signed string for the given sign request. The sig.sign.execute.request must be executed before. When sig.destroy.request(i.request) is called already, the hash cannot be retrieved anymore for the request.

## Arguments
| | | |
|---|---|---|
| `long` | `i.request` |  The handle to the signing request as returned by a previous call to [sig.init.sign.request](sig.init.sign.request.md)  |

## Return values
| | |
|---|---|
| "" | An error did occur |
| not empty | The MD5 hash of the signed string. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)

- [Digital Signatures synopsis](synopsis.md)

- [Digital Signatures examples](examples.md)
