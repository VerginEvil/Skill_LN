# http.cookie.domain()

## Syntax:
`#include <bic_httpclt>`
`function string http.cookie.domain( long cookie )`

## Description
Returns the cookie domain of an http.cookie object.
The cookie domain is a value like "www.infor.com" (in which case subdomains is false) or ".infor.com" (in which case subdomains is true).

## Arguments
| | | |
|---|---|---|
| `long` | `cookie` |  an http.cookie object  |

## Return values
the cookie domain

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- the passed id must be a valid http.cookie object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
