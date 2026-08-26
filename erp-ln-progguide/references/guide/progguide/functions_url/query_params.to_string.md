# query_params.to_string()

## Syntax:
`#include <bic_web>`
`function string query_params.to_string( long query_params_instance, [ string separator ] )`

## Description
Returns a URL-encoded string representation of the specified query_params instance.
Parameter names and values are encoded before appending them to the string. By default the ampersand is used to separate key-value pairs, but this can be overruled.
Note that if a parameter has multiple values, the returned string will have multiple key-value pairs with the same key, but different values.

## Arguments
| | | |
|---|---|---|
| `long` | `query_params_instance` |  A query_params instance.  |
| `[ string` | `separator ]` |  A separator character. If not specified, the ampersand is used.  |

## Return values
A URL-encoded query parameter string.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Example
```

long    query_params
string  query_string(100)

|* create empty query_params instance
query_params = query_params.new()

|* add parameters
query_params.add(query_params, "page size", "100")
query_params.add(query_params, "tenant", "ACME_PRD")
query_params.add(query_params, "sort mode", "asc")

|* convert to URL-encoded string
query_string = query_params.to_string(query_params)
|* query_string now contains: "page+size=100&tenant=ACME_PRD&sort+mode=asc"

|* cleanup
query_params.delete(query_instance)
```

## Availability
This function is available in the following TIV level ranges:
- 2153 - 2199 (ES 10.5.2.1)
- 2231 - 2299 (ES 10.6.1.1)
- 2393 - 2399 (ES 10.7.4.1)
- 2451 and above (ES 10.8.5)

## Related topics
- [URL Functions Overview](overview.md)
