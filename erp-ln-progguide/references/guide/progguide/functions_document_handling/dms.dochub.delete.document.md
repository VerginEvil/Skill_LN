# dms.dochub.delete.document

## Syntax:
`#include <bic_dms>`
`function long dms.dochub.delete.document( long i.document, string i.reason, string o.error.mesg )`

## Description
Delete a document.

## Arguments
| | | |
|---|---|---|
| `long` | `i.document` |  The handle to a document in a query response as returned by an earlier call to [dms.dochub.query.documents](dms.dochub.query.documents.md)  |
| `string` | `i.reason` |  The reason the document is deleted.  |
| `string` | `o.error.mesg` |  Error message in case of a failure.  |

## Return values
| | |
|---|---|
| 0 | Delete did succeed. |
| <>0 | An error occurred. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [DMS Document handling API](overview.md)
- [Document handling via Document Hub synopsis](dochub_synopsis.md)
- [Document Management via Document Hub examples](dochub_examples.md)
