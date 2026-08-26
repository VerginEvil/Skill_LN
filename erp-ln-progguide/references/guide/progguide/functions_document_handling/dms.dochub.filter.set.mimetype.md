# dms.dochub.filter.set.mimetype

## Syntax:
`#include <bic_dms>`
`function [long] dms.dochub.filter.set.mimetype( long i.filter, string i.mimetype )`

## Description
Set a mimetype filter to be used for a query request.

## Arguments
| | | |
|---|---|---|
| `long` | `i.filter` |  The handle to filter as returned by a previous call to [dms.dochub.create.filter](dms.dochub.create.filter.md)  |
| `string` | `i.mimetype` |  The mimetype for the filter.  |

## Return values
| | |
|---|---|
| 0 | An error occurred. |
| <>0 | A handle to the added filter mimetype. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [DMS Document handling API](overview.md)
- [Document handling via Document Hub synopsis](dochub_synopsis.md)
- [Document Management via Document Hub examples](dochub_examples.md)
