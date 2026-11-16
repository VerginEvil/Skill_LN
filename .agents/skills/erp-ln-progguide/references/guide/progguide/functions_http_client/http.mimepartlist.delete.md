# http.mimepartlist.delete()

## Syntax:
`#include <bic_httpclt>`
`function void http.mimepartlist.delete( long http.mimepartlist )`

## Description
Deletes an http.mimepartlist object. All contained http.mimepart objects are deleted as well.

## Arguments
| | | |
|---|---|---|
| `long` | `http.mimepartlist` |  an mimepartlist object  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2220.

## Preconditions
- the passed id must be a valid http.mimepartlist object

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
