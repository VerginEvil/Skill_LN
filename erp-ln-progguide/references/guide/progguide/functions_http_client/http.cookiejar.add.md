# http.cookiejar.add()

## Syntax:
`#include <bic_httpclt>`
`function void http.cookiejar.add( long cookiejar, long cookie )`

## Description
Adds an http.cookie object to an http.cookiejar object.

## Arguments
| | | |
|---|---|---|
| `long` | `cookiejar` |  an http.cookiejar object  |
| `long` | `cookie` |  an http.cookie object  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- parameter 'http.cookiejar' must be a valid http.cookiejar object
- parameter 'http.cookie' must be a valid http.cookie object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
