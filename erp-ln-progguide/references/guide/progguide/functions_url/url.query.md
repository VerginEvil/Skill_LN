# url.query()

## Syntax:
`#include <bic_web>`
`function string url.query( long url_instance )`

## Description
Returns the query component of a URL instance. This is an empty string if the URL does not specify a query.
Note  The query is returned in its non-decoded form. The reason is that the returned query will typically need further processing, like retrieving the names and values of query parameters. If the query string would be returned in its decoded form, it would be impossible to distinguish between actual query parameter separators (like the `&` and the `=` characters) and these characters as part of the query parameter names and/or values.

## Arguments
| | | |
|---|---|---|
| `long` | `url_instance` |  A URL instance.  |

## Return values
The non-decoded query component of a URL instance.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Availability
This function is available in the following TIV level ranges:
- 2153 - 2199 (ES 10.5.2.1)
- 2231 - 2299 (ES 10.6.1.1)
- 2393 - 2399 (ES 10.7.4.1)
- 2451 and above (ES 10.8.5)

## Related topics
- [URL Functions Overview](overview.md)
