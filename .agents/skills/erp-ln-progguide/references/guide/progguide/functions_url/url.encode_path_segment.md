# url.encode_path_segment()

## Syntax:
`#include <bic_web>`
`function string url.encode_path_segment( const string path_segment )`

## Description
Encodes a path segment (i.e. a part of a path between path separators) according to [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986), so it can be safely used in a URL.
If a path segment contains one or more path separators (i.e. the forward-slash) then these will be encoded as %2F.
The following characters are not escaped:

- The 'pchar' set of characters. This set consists of:

- The 'unreserved' set of characters: `a-zA-Z0-9-._~`

- The 'sub-delims' set of characters: `!$&'()*+,;=`

- The characters: `:@`

## Arguments
| | | |
|---|---|---|
| `const string` | `path_segment` |  A path segment.  |

## Return values
The URL encoded path segment.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Example
```

string  encoded_str(100)

encoded_str = url.encode_path_segment("/hello, world!/file\name.doc")
|* encoded_str now contains: "%2Fhello%2C%20world%21%2Ffile%5Cname.doc"
```

## Availability
This function is available in the following TIV level ranges:

- 2153 - 2199 (ES 10.5.2.1)

- 2231 - 2299 (ES 10.6.1.1)

- 2393 - 2399 (ES 10.7.4.1)

- 2451 and above (ES 10.8.5)

## Related topics
- [URL Functions Overview](overview.md)
