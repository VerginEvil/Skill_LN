# dms.dochub.query.documents

## Syntax:
`#include <bic_dms>`
`function long dms.dochub.query.documents( string i.ln.table, string i.document.type, long i.attr.list, long i.filter, long o.documents, string o.error.mesg, [ ref long o.nr.documents ] )`

## Description
Query documents of a DMS via the Document Hub.

## Arguments
| | | |
|---|---|---|
| `string` | `i.ln.table` |  The LN table to be used in the Document Hub for finding the document types to be used for the query.  |
| `string` | `i.document.type` |  The document type to be used for the query. When empty, all document types defined for the LN table are used.  |
| `long` | `i.attr.list` |  The application attribute values to be used in the query. The list is a handle as returned by an earlier call to [dms.dochub.create.application.attribute.list](dms.dochub.create.application.attribute.list.md)  |
| `long` | `i.filter` |  The handle to a filter as returned by an earlier call to [dms.dochub.create.filter](dms.dochub.create.filter.md)  |
| `long` | `o.documents` |  A handle to the query response, containing unique identifications to the documents.  |
| `string` | `o.error.mesg` |  Error message in case of a failure.  |
| `[ ref long` | `o.nr.documents ]` |  The number of documents returned in the query response.  |

## Return values
| | |
|---|---|
| 0 | Query did succeed. |
| <>0 | An error occurred. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [DMS Document handling API](overview.md)

- [Document handling via Document Hub synopsis](dochub_synopsis.md)

- [Document Management via Document Hub examples](dochub_examples.md)
