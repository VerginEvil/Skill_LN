# url.decode()

## Syntax:
`#include <bic_web>`
`function string url.decode( const string encoded_str )`

## Description
Decodes a URL encoded string. Any percent encoded characters, like %20 (space) are converted to their decoded form.

## Arguments
| | | |
|---|---|---|
| `const string` | `encoded_str` |  A URL encoded string.  |

## Return values
the decoded form of the URL encoded string.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Example
```

string  decoded_str(100)

decoded_str = url.decode("http://example.com/hello%2C%20world%21")
|* decoded_str now contains: "http://example.com/hello, world!"
```

## Availability
This function is available in the following TIV level ranges:
- 2153 - 2199 (ES 10.5.2.1)
- 2231 - 2299 (ES 10.6.1.1)
- 2393 - 2399 (ES 10.7.4.1)
- 2451 and above (ES 10.8.5)

## Related topics
- [URL Functions Overview](overview.md)
