# http.headerlist.get()

## Syntax:
`#include <bic_httpclt>`
`function long http.headerlist.get( long headerlist, const string name )`

## Description
Gets the HTTP header with the specified name from an http.headerlist object. The name is searched in a case-insensitive way. The HTTP header is returned as an http.header object.
Note: The Set-Cookie header can occur multiple times in an http.headerlist object. This function returns the first Set-Cookie header found. An http.headerlist object stores Set-Cookie headers in sequence. In this way it is possible to get the next Set-Cookie header(s) by calling [http.header.next()](http.header.next.md) on the first Set-Cookie header returned by this function.
Example:
```

        long	headerlist
        long    header

        |* assume headerlist refers to a filled http.headerlist object

        |* get the "Content-Type" header
        |* searching is done in a case-insensitive manner, so the following names also work:
        |* "CONTENT-TYPE", "content-type", "Content-type"
        header = http.headerlist.get(headerlist, "Content-Type")

        if header <> 0 then
                |* header found
        endif
```

## Arguments
| | | |
|---|---|---|
| `long` | `headerlist` |  an http.headerlist object  |
| `const string` | `name` |  an HTTP header name, like "Content-Type"  |

## Return values
the (first) http.header object with the specified name, or 0 if no header with the specified name was found

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the passed id must be a valid http.headerlist object

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
