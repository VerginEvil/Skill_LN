# http.cookiejar.first()

## Syntax:
`#include <bic_httpclt>`
`function long http.cookiejar.first( long cookiejar )`

## Description
Returns the first http.cookie object of an http.cookiejar. This can be used to iterate all cookies in the cookiejar.
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
| `long` | `cookiejar` |  an http.cookiejar object  |

## Return values
the first http.cookie object in the cookiejar, or 0 if the cookiejar is empty

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- the passed id must be a valid http.cookiejar object

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
