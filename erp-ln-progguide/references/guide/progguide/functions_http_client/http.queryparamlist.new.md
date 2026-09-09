# http.queryparamlist.new()

## Syntax:
`#include <bic_httpclt>`
`function long http.queryparamlist.new(... )`

## Description
Constructs a new http.queryparamlist object. It is possible to initialize the http.queryparamlist object with name-value query parameter pairs. When the http.queryparamlist object is passed to eg. [http.get()](http.get.md), the name and value pairs will be used to build a url-encoded querystring. The querystring is then appended to the url after the '?' sign.
Example:
```

        long    queryparamlist
        long    response

        queryparamlist = http.queryparamlist.new(
           "name",              "John Doe",
           "address",           "34, Mainstreet",
           "city",              "New York")

        response = http.get("http://example.com/get",
           HTTP_QUERYPARAMLIST, queryparamlist)

        http.queryparamlist.delete(queryparamlist)
```
This results in the following url: http://example.com/get?name=John%20Doe&address=34,%20Mainstreet&city=New%20York

## Arguments
| | | |
|---|---|---|
|  | `...` | pairs of name and value parameters; they can be of any type and should not yet have been url-encoded |

## Return values
a new http.queryparamlist object, or 0 in case of an error

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the number of arguments passed must be an even number (0, 2, 4,...)

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
