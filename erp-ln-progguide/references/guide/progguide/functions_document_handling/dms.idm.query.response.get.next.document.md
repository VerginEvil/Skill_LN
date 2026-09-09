# dms.idm.query.response.get.next.document

## Syntax:
`#include <bic_dms>`
`function long dms.idm.query.response.get.next.document( long i.document )`

## Description
Get a handle to the next document in a query response.

## Arguments
| | | |
|---|---|---|
| `long` | `i.document` |  The handle to a document in a query response as returned by an earlier call to [dms.idm.query.documents](dms.idm.query.documents.md)  |

## Return values
| | |
|---|---|
| 0 | No next document found. |
| <>0 | Handle to next document. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [DMS Document handling API](overview.md)

- [Document handling in IDM synopsis](idm_synopsis.md)

- [Document Management (IDM) examples](idm_examples.md)
