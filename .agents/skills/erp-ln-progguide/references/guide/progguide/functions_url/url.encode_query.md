# url.encode_query()

## Syntax:
`#include <bic_web>`
`function string url.encode_query( const string query )`

## Description
Encodes a query string according to [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986), so it can be safely used in a URL.
Note that this function encodes the query string as a whole, it does not look for individual parts like query parameters and values. Use [query_params.new()](query_params.new.md) and [query_params.to_string()](query_params.to_string.md) to create a query string of which the individual parts are encoded.
The following characters are not escaped:

- The 'pchar' set of characters. This set consists of:

- The 'unreserved' set of characters: `a-zA-Z0-9-._~`

- The 'sub-delims' set of characters: `!$&'()*+,;=`

- The characters: `:@`

- The path separator and the question mark: `/?`

## Arguments
| | | |
|---|---|---|
| `const string` | `query` |  A query string.  |

## Return values
The URL encoded query string.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Example
```

string  encoded_str(100)

encoded_str = url.encode_query("a=1&b=3&a\b/c=!")
|* encoded_str now contains: "a=1&b=3&a%5Cb/c=!"
```

## Availability
This function is available in the following TIV level ranges:

- 2153 - 2199 (ES 10.5.2.1)

- 2231 - 2299 (ES 10.6.1.1)

- 2393 - 2399 (ES 10.7.4.1)

- 2451 and above (ES 10.8.5)

## Related topics
- [URL Functions Overview](overview.md)
