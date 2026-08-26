# http.mimepartlist.add()

## Syntax:
`#include <bic_httpclt>`
`function void http.mimepartlist.add( long mimepartlist, long http.mimepart )`

## Description
Adds an http.mimepart object to an http.mimepartlist object.

## Arguments
| | | |
|---|---|---|
| `long` | `mimepartlist` |  an http.mimepartlist object  |
| `long` | `http.mimepart` |  an http.mimepart object  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2220.

## Preconditions
- parameter 'http.mimepartlist' must be a valid http.mimepartlist object
- parameter 'http.mimepart' must be a valid http.mimepart object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
