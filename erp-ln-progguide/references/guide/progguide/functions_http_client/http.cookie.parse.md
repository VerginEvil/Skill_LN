# http.cookie.parse()

## Syntax:
`#include <bic_httpclt>`
`function long http.cookie.parse( const string format, const string cookie_string )`

## Description
Parses a cookie string and constructs a new http.cookie object based on it. The cookie string can be in Netscape format or in Set-Cookie format.
A Netscape formatted cookie string consist of 7 parts, separated by tabs:
- domain
- subdomains (TRUE/FALSE)
- path
- secure (TRUE/FALSE)
- expires
- name
- value (can be empty)  See https://curl.se/docs/http-cookies.html for more info.
Notes
- A string starting with # is treated as comments, except when the string starts with #HttpOnly_ which is a valid prefix for the cookie domain.
- Only basic checking is done; whether the parts match with each other is not checked!  A Set-Cookie cookie string consists of a name=value pair with 0 or more attributes, separated by ';'. The following attributes are recognized (others are silently ignored):
- Path=/some/path
- Domain=some.domain.com
- Secure
- HttpOnly
- Expires=Wed, 01 Sep 2021 15:16:17 GMT
- Max-Age=86400 (this is converted to an Expires attribute based on the current date/time)  See https://www.ietf.org/rfc/rfc6265.txt for more info.
Notes
- A Set-Cookie string without a Domain is not accepted. The reason is that in the context of the this function call, no default domain is known.

## Arguments
| | | |
|---|---|---|
| `const string` | `format` |  the format of the specified cookie string; you can use one of the following defines: HTTP_COOKIE_NETSCAPE_FORMAT, HTTP_COOKIE_SET_COOKIE_FORMAT  |
| `const string` | `cookie_string` |  a cookie string in either Netscape or Set-Cookie format  |

## Return values
a new http.cookie object, or 0 in case the specified cookie string could not be parsed

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- the passed format must be one of the following defines: HTTP_COOKIE_NETSCAPE_FORMAT, HTTP_COOKIE_SET_COOKIE_FORMAT

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
