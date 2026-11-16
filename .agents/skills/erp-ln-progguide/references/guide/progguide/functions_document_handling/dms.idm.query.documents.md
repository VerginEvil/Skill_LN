# dms.idm.query.documents

## Syntax:
`#include <bic_dms>`
`function long dms.idm.query.documents( string i.document.type, long i.attr.list, long i.filter, long o.documents, string o.error.mesg, [ ref long o.nr.documents ] )`

## Description
Query documents of a DMS via the Document Hub.

## Arguments
| | | |
|---|---|---|
| `string` | `i.document.type` |  The document type to be used for the query.  |
| `long` | `i.attr.list` |  The document type attribute values to be used in the query. The list is a handle as returned by an earlier call to [dms.idm.create.doctype.attribute.list](dms.idm.create.doctype.attribute.list.md)  |
| `long` | `i.filter` |  The handle to a filter as returned by an earlier call to [dms.idm.create.filter](dms.idm.create.filter.md)  |
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

- [Document handling in IDM synopsis](idm_synopsis.md)

- [Document Management (IDM) examples](idm_examples.md)
