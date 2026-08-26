# vwr.start

## Syntax:
`#include <bic_vwr>`
`function void vwr.start( )`

## Description
This function activates the Document Viewer. Control will be returned to the script after the Viewer has been closed. Function vwr.init must have been called before vwr.start can be called.

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Document Viewer synopsis](synopsis.md)
- [Document Viewer overview](overview.md)
