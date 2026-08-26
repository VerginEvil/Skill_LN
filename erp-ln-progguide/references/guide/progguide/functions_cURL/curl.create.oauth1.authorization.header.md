# curl.create.oauth1.authorization.header()

## Syntax:
`#include <bic_curl>`
`function long curl.create.oauth1.authorization.header( const string method, const string url, const string consumer.key, const string consumer.secret, ref string header )`

## Description
Creates an OAuth 1.0 authorization header. Note that this function returns the header value, it must added to the HTTP request with header name "Authorization".

## Arguments
| | | |
|---|---|---|
| `const string` | `method` |  the HTTP method, specify "GET" or "POST".  |
| `const string` | `url` |  the URL of the request.  |
| `const string` | `consumer.key` |  the Consumer Key for OAuth 1.0.  |
| `const string` | `consumer.secret` |  the Consumer Secret for OAuth 1.0.  |
| `ref string` | `header` |  the created Authorization header  |

## Return values
| | |
|---|---|
| 0 | Ok |
| > 0 | A cURL code; use ` [curl.strerror$()](curl.strerror$.md)` to get a descriptive message  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2100.

## Example
```

long ret
string header(2048) mb

ret = curl.create.oauth1.authorization.header("POST",
        "https://ws.infor.com:2600/ca/api/connection",
        "CD8o-UECnqgy2Jv~t9uD",
        "tLT.llmm1tR5lHBBBDEM", header)
| header now contains (in one line):
| OAuth oauth_signature="DhDNmvGmqkxC8S30c5TOAuKaCCo%3D",
|       oauth_version="1.0",
|       oauth_nonce="2b3a390f-2d31-4864-a73e-a4977c7124b8",
|       oauth_signature_method="HMAC-SHA1",
|       oauth_consumer_key="CD8o-UECnqgy2Jv~t9uD",
|       oauth_timestamp="1457103048"
```

## Related topics
- [cURL handling overview](overview.md)
