# url.parse()

## Syntax:
`#include <bic_web>`
`function long url.parse( const string encoded_str )`

## Description
Parses the specified URL-encoded string and creates a URL instance based on it.
See e.g. [https://docs.oracle.com/javase/7/docs/api/java/net/URI.html](https://docs.oracle.com/javase/7/docs/api/java/net/URI.html) for info regarding URIs/URLs and their components.
See also [https://url.spec.whatwg.org](https://url.spec.whatwg.org) for why we use the term URL instead of URI.

## Arguments
| | | |
|---|---|---|
| `const string` | `encoded_str` |  A URL encoded string. If an empty string is passed, an empty URL instance is returned.  |

## Return values
A new URL instance.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Examples
The URL `https://jdoe:123@infor.com:443/cloud?opt=123&a%3Abc=34#28` will be decoded to the following parts:
| | |
|---|---|
| scheme: | https |
| host: | infor.com |
| user info: | jdoe:123 |
| port: | 443 |
| path: | /cloud |
| query: | opt=123&a%3Abc=34 |
| fragment: | 28 |
The opaque URL (no slash after scheme) `mailto:jdoe@infor.com` will be decoded to the following parts:
| | |
|---|---|
| scheme: | mailto |
| host: |  |
| user info: |  |
| port: | -1 |
| path: | jdoe@infor.com |
| query: |  |
| fragment: |  |
A special case is the * which is used for the HTTP OPTIONS method. This URL is decoded to the following parts:
| | |
|---|---|
| scheme: |  |
| host: |  |
| user info: |  |
| port: | -1 |
| path: | * |
| query: |  |
| fragment: |  |

## Availability
This function is available in the following TIV level ranges:

- 2153 - 2199 (ES 10.5.2.1)

- 2231 - 2299 (ES 10.6.1.1)

- 2393 - 2399 (ES 10.7.4.1)

- 2451 and above (ES 10.8.5)

## Related topics
- [URL Functions Overview](overview.md)
