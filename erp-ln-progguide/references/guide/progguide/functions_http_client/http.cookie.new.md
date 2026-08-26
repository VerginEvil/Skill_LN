# http.cookie.new()

## Syntax:
`#include <bic_httpclt>`
`function long http.cookie.new( ... )`

## Description
Constructs a new http.cookie object. Use the attributes as specified below to configure the cookie.
Example:
```

        long    cookie

        cookie = http.cookie.new(
           HTTP_COOKIE_NAME,     "SID",
           HTTP_COOKIE_VALUE,    "1234abcd",
           HTTP_COOKIE_DOMAIN,   ".infor.com",
           HTTP_COOKIE_PATH,     "/api",
           HTTP_COOKIE_SECURE,   true,
           HTTP_COOKIE_HTTPONLY, true,
           HTTP_EXPIRES,         0)             |* 0 = session cookie
```

## Arguments
| | | |
|---|---|---|
| `` | `...` |  Attribute-value pairs s to configure the cookie; the following HTTP_COOKIE attributes are supported:  |

## Return values
a new http.cookie object, or 0 in case of an error

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- passed number of arguments must be valid
- passed argument types must be valid
- passed attributes/flags must be known
- the HTTP_COOKIE_NAME attribute is required
- the HTTP_COOKIE_DOMAIN attribute is required

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
