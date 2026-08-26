# http.cookie.to_string()

## Syntax:
`#include <bic_httpclt>`
`function string http.cookie.to_string( long cookie, const string format )`

## Description
Returns a cookie string in Netscape format or Set-Cookie format.
A Netscape formatted cookie string consist of 7 parts, separated by tabs:
- domain
- subdomains (TRUE/FALSE)
- path
- secure (TRUE/FALSE)
- expires
- name
- value (can be empty)  See https://curl.se/docs/http-cookies.html for more info.
A Set-Cookie cookie string consists of a name=value pair with 0 or more attributes, separated by ';':
- Path=/some/path
- Domain=some.domain.com
- Secure
- HttpOnly
- Expires=Wed, 01 Sep 2021 15:16:17 GMT
- Max-Age=86400 (this is not returned as internally a Max-Age is converted to an Expires attribute based on the current date/time)  See https://www.ietf.org/rfc/rfc6265.txt for more info.

## Arguments
| | | |
|---|---|---|
| `long` | `cookie` |  an http.cookie object  |
| `const string` | `format` |  the format of the specified cookie string; you can use one of the following defines: HTTP_COOKIE_NETSCAPE_FORMAT, HTTP_COOKIE_SET_COOKIE_FORMAT  |

## Return values
a cookie string in the requested format

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- the passed id must be a valid http.cookie object
- the passed format must be one of the following defines: HTTP_COOKIE_NETSCAPE_FORMAT, HTTP_COOKIE_SET_COOKIE_FORMAT

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
