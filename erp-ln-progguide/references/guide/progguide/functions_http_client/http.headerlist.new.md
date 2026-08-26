# http.headerlist.new()

## Syntax:
`#include <bic_httpclt>`
`function long http.headerlist.new( ... )`

## Description
Constructs a new http.headerlist object. It is possible to initialize the http.headerlist object with HTTP header name-value pairs.
Example:
```

        long	headerlist

        headerlist = http.headerlist.new(
           "Content-Type",        "application/json",
           "X-Infor-LnCompany",   422)
```

## Arguments
| | | |
|---|---|---|
| `` | `...` |  pairs of name and value parameters; they can be of any type but will be converted to strings  |

## Return values
a new http.headerlist object, or 0 in case of an error

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the number of arguments passed must be an even number (0, 2, 4, ...)

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
