# url.encode_query_part()

## Syntax:
`#include <bic_web>`
`function string url.encode_query_part( const string query_part )`

## Description
Encodes a query part according to the `application/x-www-form-urlencoded` MIME type, so it can be safely used in the query string of a URL, or in the body of an `application/x-www-form-urlencoded` HTTP POST request.
An `application/x-www-form-urlencoded` string consists of one or more `param=value` pairs, where each pair is separated by an ampersand or a semi-colon character.
The following characters are not escaped:
- The 'unreserved' set of characters, except the tilde: `a-zA-Z0-9-._`
- The asterisk character: `*`  See https://url.spec.whatwg.org/ for more info.
Note  The space character is escaped by the plus `+` sign instead of `%20`.

## Arguments
| | | |
|---|---|---|
| `const string` | `query_part` |  A query part.  |

## Return values
The URL encoded query part.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Example
```

string  encoded_str(100)

encoded_str = url.encode_query_part("a=1&b=3&a\b/c=!")
|* encoded_str now contains: "a%3D1%26b%3D3%26a%5Cb%2Fc%3D%21"

encoded_str = url.encode_query_part("hello world")
|* encoded_str now contains: "hello+world"
```

## Availability
This function is available in the following TIV level ranges:
- 2153 - 2199 (ES 10.5.2.1)
- 2231 - 2299 (ES 10.6.1.1)
- 2393 - 2399 (ES 10.7.4.1)
- 2451 and above (ES 10.8.5)

## Related topics
- [URL Functions Overview](overview.md)
