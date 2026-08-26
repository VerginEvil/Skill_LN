# url.to_string()

## Syntax:
`#include <bic_web>`
`function string url.to_string( long url_instance )`

## Description
Returns a URL-encoded string representation of the specified URL instance.
The function does the following:
- start with an empty buffer
- if the URL has a scheme, it is appended to the buffer and a `:` is added
- if the URL has a user info part or a host part or a port, `//` is appended
- if the URL has user info, it is appended and `@` is added
- if the URL has a host, it is appended
- if the URL has a port, `:` is appended and the port is added
- if the URL has a path, it is appended
- if the URL has a query, `?` is appended and the query is added
- if the URL has a fragment, `#` is appended and the fragment is added

## Arguments
| | | |
|---|---|---|
| `long` | `url_instance` |  A URL instance.  |

## Return values
A URL-encoded URL string.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Example
```

long    url_instance
string  url_string(100)

|* create empty URL instance
url_instance = url.new()

|* set URL components
url.set_scheme(url_instance, "https")
url.set_host(url_instance, "www.google.com")
url.set_port(url_instance, 443)
url.set_path(url_instance, "/search")
url.set_query(url_instance, "q=url encoding and decoding")

|* convert to URL-encoded string
url_string = url.to_string(url_instance)
|* url_string now contains: "https://www.google.com:443/search?q=url+encoding+and+decoding"

|* cleanup
url.delete(url_instance)
```

## Availability
This function is available in the following TIV level ranges:
- 2153 - 2199 (ES 10.5.2.1)
- 2231 - 2299 (ES 10.6.1.1)
- 2393 - 2399 (ES 10.7.4.1)
- 2451 and above (ES 10.8.5)

## Related topics
- [URL Functions Overview](overview.md)
