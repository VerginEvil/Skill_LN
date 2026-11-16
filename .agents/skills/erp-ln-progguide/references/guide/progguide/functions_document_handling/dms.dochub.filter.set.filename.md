# dms.dochub.filter.set.filenamee

## Syntax:
`#include <bic_dms>`
`function [long] dms.dochub.filter.set.filename( long i.filter, string i.filename )`

## Description
Set a filename filter to be used for a query request.
The filename filter is a (part of a) logical expression which will be compiled with expr.compile. The expression being compiled is in the format: document_file_name IN “filename_filter”.

## Arguments
| | | |
|---|---|---|
| `long` | `i.filter` |  The handle to filter as returned by a previous call to [dms.dochub.create.filter](dms.dochub.create.filter.md)  |
| `string` | `i.filename` |  The filename for the filter.  |

## Return values
| | |
|---|---|
| 0 | An error occurred. |
| <>0 | A handle to the added filter filename. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [DMS Document handling API](overview.md)

- [Document handling via Document Hub synopsis](dochub_synopsis.md)

- [Document Management via Document Hub examples](dochub_examples.md)
