# http.routeparamlist.new()

## Syntax:
`#include <bic_httpclt>`
`function void http.routeparamlist.new(... )`

## Description
Constructs a new http.routeparamlist object. It is possible to initialize the http.routeparamlist object with name-value route parameter pairs. When the http.routeparamlist object is passed to eg. http.get(), the name and value pairs will be used to fill in route parameters in the url.
Example:
```

        long    routeparamlist
        long    response

        routeparamlist = http.routeparamlist.new(
           "app",               "eln",
           "farm",              "euwe1prda",
           "tenant",            "ACME_PRD")

        response = http.get(
           "https://aws.com/apps/{app}/farms/{farm}/tenant/{tenant}",
           HTTP_ROUTEPARAMLIST, routeparamlist)

        http.routeparamlist.delete(routeparamlist)
```
This results in the following url: https://aws.com/apps/eln/farms/euwe1prda/tenant/ACME_PRD

## Arguments
| | | |
|---|---|---|
|  | `...` | pairs of name and value parameters |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the number of arguments passed must be an even number (0, 2, 4,...)

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
