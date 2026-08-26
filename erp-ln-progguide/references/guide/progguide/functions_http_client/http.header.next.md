# http.header.next()

## Syntax:
`#include <bic_httpclt>`
`function long http.header.next( long header )`

## Description
Returns an http.header object's next http.header object.
Example:
```

        long	headerlist
        long    header

        |* assume headerlist refers to a filled http.headerlist object

        |* get the first header from the headerlist
        header = http.headerlist.first(headerlist)

        while header <> 0
                |* get name and values from header here ...

                |* get next header
                header = http.header.next(header)
        endwhile
```

## Arguments
| | | |
|---|---|---|
| `long` | `header` |  an http.header object  |

## Return values
the next http.header object, or 0 if there is no next http.header object

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the passed id must be a valid http.header object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
