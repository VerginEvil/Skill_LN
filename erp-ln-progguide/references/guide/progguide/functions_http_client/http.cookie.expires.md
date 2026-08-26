# http.cookie.expires()

## Syntax:
`#include <bic_httpclt>`
`function long http.cookie.expires( long cookie )`

## Description
Returns when the cookie expires as a UTC date/time. A value of 0 indicates this is a session cookie.

## Arguments
| | | |
|---|---|---|
| `long` | `cookie` |  an http.cookie object  |

## Return values
| | |
|---|---|
| > 0 | a UTC date/time indicating when the cookie expires |
| 0 | the cookie is a session cookie |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- the passed id must be a valid http.cookie object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
