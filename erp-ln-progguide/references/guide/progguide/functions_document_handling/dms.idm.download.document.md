# dms.idm.download.document

## Syntax:
`#include <bic_dms>`
`function long dms.idm.download.document( long i.document, string io.document.file, string o.error.mesg )`

## Description
Download a document.

## Arguments
| | | |
|---|---|---|
| `long` | `i.document` |  The handle to a document in a query response as returned by an earlier call to [dms.idm.query.documents](dms.idm.query.documents.md)  |
| `string` | `io.document.file` |  The file path the document is downloaded to. When not specified, the document is downloaded to $BSE/tmp/filetransfer/logname$/download./>  |
| `string` | `o.error.mesg` |  Error message in case of a failure.  |

## Return values
| | |
|---|---|
| 0 | Download did succeed. |
| <>0 | An error occurred. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [DMS Document handling API](overview.md)
- [Document handling in IDM synopsis](idm_synopsis.md)
- [Document Management (IDM) examples](idm_examples.md)
