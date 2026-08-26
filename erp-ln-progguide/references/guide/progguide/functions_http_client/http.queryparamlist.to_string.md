# http.queryparamlist.to_string()

## Syntax:
`#include <bic_httpclt>`
`function string http.queryparamlist.to_string( long queryparamlist, [ string sep(1) ] )`

## Description
Converts the key-value pairs in an http.queryparamlist object to an application/x-www-form-urlencoded string. The string can be used as the body of an HTTP request to post form data.
By default the '&' is used to separate key-value pairs, but this can be overruled.
Example:
```

        long    queryparamlist
        string  formdata(1)	based

        queryparamlist = http.queryparamlist.new(
           "name",                 "John Doe",
           "address",              "34, Mainstreet",
           "city",                 "New York")

        str.assign(formdata, http.queryparamlist.to_string(queryparamlist))

        |* formdata now contains: "name=John%20Doe&address=34,%20Mainstreet&city=New%20York"

        http.queryparamlist.delete(queryparamlist)
```

## Arguments
| | | |
|---|---|---|
| `long` | `queryparamlist` |  an http.queryparamlist object  |
| `[ string` | `sep(1) ]` |  optional, the separator to use between the key-value pairs; is not specified '&' is used  |

## Return values
an application/x-www-form-urlencoded string; or an empty string if the http.queryparamlist object is empty

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- the passed id must be a valid http.queryparamlist object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
