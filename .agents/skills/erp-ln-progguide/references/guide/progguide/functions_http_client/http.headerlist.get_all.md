# http.headerlist.get_all()

## Syntax:
`#include <bic_httpclt>`
`function long http.headerlist.get_all( long headerlist, const string name )`

## Description
Returns a new http.headerlist object containing http.header objects with the given name. As this is a new list, you have to take care of deleting it when it is no longer needed.
If no header was found with the given name, 0 is returned.
Currently, this function is only useful for Set-Cookie HTTP response headers, as that is the only HTTP header that can occur multiple times.
Example:
```

        long	headerlist
        long    set_cookie_headers
        long    set_cookie_header

        |* assume headerlist refers to a filled http.headerlist object

        |* get all "Set-Cookie" headers; this returns a new http.headerlist
        |* with copies of the found Set-Cookie http.header objects;
        |* searching is done in a case-insensitive manner, so the following names also work:
        |* "SET-COOKIE", "set-cookie"
        set_cookie_headers = http.headerlist.get_all(headerlist, "Set-Cookie")

        set_cookie_header = http.headerlist.first(set_cookie_headers)

        while set_cookie_header <> 0
                |* process the header

                |* get the next header
                set_cookie_header = http.header.next(set_cookie_header)
        endwhile

        |* delete the list of Set-Cookie headers
        http.headerlist.delete(set_cookie_headers)
```

## Arguments
| | | |
|---|---|---|
| `long` | `headerlist` |  an http.headerlist object  |
| `const string` | `name` |  an HTTP header name, like "Set-Cookie"  |

## Return values
an http.headerlist object containing http.header objects with the specified name, or 0 if the specified header name was not found

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- the passed id must be a valid http.headerlist object

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
