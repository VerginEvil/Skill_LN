# dms.idm.upload.document

## Syntax:
`#include <bic_dms>`
`function long dms.idm.upload.document( string i.document.type, long i.attr.list, string i.filename, string i.display.name, string i.mimetype, boolean i.create.revision, long o.document, string o.error.mesg )`

## Description
Upload a document to IDM.

## Arguments
| | | |
|---|---|---|
| `string` | `i.document.type` |  The document type to be used for the upload.  |
| `long` | `i.attr.list` |  The document type attribute values to be used in the upload. The list is a handle as returned by an earlier call to [dms.idm.create.doctype.attribute.list](dms.idm.create.doctype.attribute.list.md)  |
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
- [Document handling in IDM synopsis](idm_synopsis.md)
- [Document Management (IDM) examples](idm_examples.md)
