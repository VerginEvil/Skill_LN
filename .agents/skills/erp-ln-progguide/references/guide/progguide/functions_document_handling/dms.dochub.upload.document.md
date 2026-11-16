# dms.dochub.upload.document

## Syntax:
`#include <bic_dms>`
`function long dms.dochub.upload.document( string i.ln.table, string i.document.type, long i.attr.list, string i.filename, string i.display.name, string i.mimetype, boolean i.create.revision, long o.document, string o.error.mesg )`

## Description
Upload a document to a DMS via the Document Hub.

## Arguments
| | | |
|---|---|---|
| `string` | `i.ln.table` |  The LN table to be used in the Document Hub for finding the document type to be used for the upload.  |
| `string` | `i.document.type` |  The document type to be used for the upload. When empty, the document type to be used for upload defined for the LN table in the Document Hub is used. An active mapping for the document type must exist in the Document Hub.  |
| `long` | `i.attr.list` |  The application attribute values to be used in the upload. The list is a handle as returned by an earlier call to [dms.dochub.create.application.attribute.list](dms.dochub.create.application.attribute.list.md)  |
| `string` | `i.filename` |  The file path of the document file.  |
| `string` | `i.display.name` |  The display name of the document.  |
| `string` | `i.mimetype` |  The mimetype of the document file.  |
| `boolean` | `i.create.revision` |  Whether or not a new revision must be created of the document when it already exists.  |
| `long` | `o.document` |  A handle to the upload response, containing unique identification of the uploaded document.  |
| `string` | `o.error.mesg` |  Error message in case of a failure.  |

## Return values
| | |
|---|---|
| 0 | Upload did succeed. |
| <>0 | An error occurred. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [DMS Document handling API](overview.md)

- [Document handling via Document Hub synopsis](dochub_synopsis.md)

- [Document Management via Document Hub examples](dochub_examples.md)
