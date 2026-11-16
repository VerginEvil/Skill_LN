# http.headerlist.first()

## Syntax:
`#include <bic_httpclt>`
`function long http.headerlist.first( long headerlist )`

## Description
Returns the first http.header object of an http.headerlist. This can be used to iterate all HTTP headers in the list.
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
| `long` | `headerlist` |  an http.headerlist object  |

## Return values
the first http.header object in the list, or 0 if the list is empty

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the passed id must be a valid http.headerlist object

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
