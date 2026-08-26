# vwr.init

## Syntax:
`#include <bic_vwr>`
`function long vwr.init( )`

## Description
This function must be the first to be called, it initializes the Document Viewer. The Document Viewer is not supported in Worktop. When this session was started from a parent session in modeless mode, this function will reactive the parent session. So any imports which must be done by this session from the parent should be done before this function is called.

## Return values
| | |
|---|---|
| 0 | Success |
| -1 | Failure, not supported with this user interface |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Document Viewer synopsis](synopsis.md)
- [Document Viewer overview](overview.md)
- [Document Viewer example](example.md)
