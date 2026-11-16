# http.mimepart.delete()

## Syntax:
`#include <bic_httpclt>`
`function void http.mimepart.delete( long mimepart )`

## Description
Deletes an http.mimepart object. If the http.mimepart object is part of an http.mimepartlist object is it removed from the mimepart list as well.

## Arguments
| | | |
|---|---|---|
| `long` | `mimepart` |  an http.mimepart object  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2220.

## Preconditions
- the passed id must be a valid http.mimepart object

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
