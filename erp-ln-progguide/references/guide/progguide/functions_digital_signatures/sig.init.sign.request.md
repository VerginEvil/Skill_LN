# sig.init.sign.request

## Syntax:
`#include <bic_sig>`
`function long sig.init.sign.request( )`

## Description
Initialize a new request to sign a document. A request can be modified and executed multiple times. To release all resources linked to the request, call [sig.destroy.request](sig.destroy.request.md)

## Return values
| | |
|---|---|
| >0 | A handle to the request - this handle can be passed to other signature functions. |
| <=0 | An error occurred. A DAL message has been set. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)
- [Digital Signatures synopsis](synopsis.md)
- [Digital Signatures examples](examples.md)
