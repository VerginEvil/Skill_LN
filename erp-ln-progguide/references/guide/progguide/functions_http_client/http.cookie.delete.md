# http.cookie.delete()

## Syntax:
`#include <bic_httpclt>`
`function void http.cookie.delete( long cookie )`

## Description
Deletes an http.cookie object. If the http.cookie object is part of an http.cookiejar object, it is removed from the cookiejar as well.

## Arguments
| | | |
|---|---|---|
| `long` | `cookie` |  an http.cookie object  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- the passed id must be a valid http.cookie object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
