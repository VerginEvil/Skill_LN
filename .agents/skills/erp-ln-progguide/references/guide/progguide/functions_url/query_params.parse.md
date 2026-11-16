# query_params.parse()

## Syntax:
`#include <bic_web>`
`function long query_params.parse( const string encoded_params )`

## Description
Parses the specified URL-encoded params string and creates a query_params instance based on it.
A URL-encoded parameters string is a string like `"p1=v1&p2=v%2F2"` of which the invididual parts have been encoded using [url.encode_query_part()](url.encode_query_part.md). Such a string can be used in the query component of a URL or in the body of an `application/x-www-form-urlencoded` HTTP POST request.
Usually the ampsersand character is used to separate the key-value pairs, but the semi-colon is understood as well.
Note  Note that if a key occurs multiple times, all values are kept. E.g. if the string `a=1&b=3&a=2` is parsed, both 1 and 2 are stored as values of parameter 'a' in the query_params instance, and 3 is stored as the value of parameter 'b'.

## Arguments
| | | |
|---|---|---|
| `const string` | `encoded_params` |  A URL encoded params string. If an empty string is passed, an empty query_params instance is returned.  |

## Return values
A new query_params instance.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Example
```

long    params

params = query_params.parse("x=1&y&x=2&sort%20mode=desc")

|* This results in a query_params instance with the following contents (represented here as JSON):
|*
|* {
|*   "x": [ "1", "2" ],
|*   "y": [ "" ],
|*   "sort mode": [ "desc" ]
|* }
```

## Availability
This function is available in the following TIV level ranges:

- 2153 - 2199 (ES 10.5.2.1)

- 2231 - 2299 (ES 10.6.1.1)

- 2393 - 2399 (ES 10.7.4.1)

- 2451 and above (ES 10.8.5)

## Related topics
- [URL Functions Overview](overview.md)
