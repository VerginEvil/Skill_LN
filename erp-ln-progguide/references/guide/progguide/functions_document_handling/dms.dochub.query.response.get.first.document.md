# dms.dochub.query.response.get.first.document

## Syntax:
`#include <bic_dms>`
`function long dms.dochub.query.response.get.first.document( long i.documents )`

## Description
Get a handle to the first document of a query response.

## Arguments
| | | |
|---|---|---|
| `long` | `i.documents` |  The handle to a query response as returned by an earlier call to [dms.dochub.query.documents](dms.dochub.query.documents.md)  |

## Return values
| | |
|---|---|
| 0 | No documents found. |
| <>0 | Handle to first document. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [DMS Document handling API](overview.md)
- [Document handling via Document Hub synopsis](dochub_synopsis.md)
- [Document Management via Document Hub examples](dochub_examples.md)
