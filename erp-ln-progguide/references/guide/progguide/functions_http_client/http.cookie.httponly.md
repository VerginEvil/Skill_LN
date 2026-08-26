# http.cookie.httponly()

## Syntax:
`#include <bic_httpclt>`
`function boolean http.cookie.httponly( long cookie )`

## Description
Returns whether an http.cookie object only applies to a HTTP (and not to other protocols, like FTP).
Although this attribute has no meaning for the HTTP Client, it is still retained, so that when the cookie is part of an http.cookiejar object, and the cookiejar is saved to a file, this attribute is stored in the file as well.

## Arguments
| | | |
|---|---|---|
| `long` | `cookie` |  an http.cookie object  |

## Return values
true if the cookie appies to HTTP only, else false

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- the passed id must be a valid http.cookie object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
