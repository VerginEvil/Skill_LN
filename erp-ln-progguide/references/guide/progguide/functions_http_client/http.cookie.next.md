# http.cookie.next()

## Syntax:
`#include <bic_httpclt>`
`function long http.cookie.next( long cookie )`

## Description
Returns an http.cookie object's next http.cookie object. This can be used to traverse http.cookie objects in an http.cookiejar object.
Example:
```

        long	cookiejar
        long    cookie

        |* assume cookiejar refers to a filled http.cookiejar object

        |* get the first cookie from the cookiejar
        cookie = http.cookiejar.first(cookiejar)

        while cookie <> 0
                |* handle cookie here ...

                |* get next cookie
                cookie = http.cookie.next(cookie)
        endwhile
```

## Arguments
| | | |
|---|---|---|
| `long` | `cookie` |  an http.cookie object  |

## Return values
the next http.cookie object, or 0 if there is no next http.cookie object

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- the passed id must be a valid http.cookie object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
