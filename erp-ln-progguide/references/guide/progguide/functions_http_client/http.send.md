# http.send()

## Syntax:
`#include <bic_httpclt>`
`function long http.send( const string method, const string url,... )`

## Description
Sends an HTTP request to a URL.

## Arguments
| | |
|---|---|
| Argument | Description |
| string | a query parameter name |
| string | a query parameter value |
| | |
|---|---|
| Argument | Description |
| long | an http.queryparamlist object; if 0, this attribute is ignored |
| | |
|---|---|
| Argument | Description |
| string | a URL-encoded query parameter string |
| | |
|---|---|
| Argument | Description |
| string | a route parameter name |
| string | a route parameter value |
| | |
|---|---|
| Argument | Description |
| long | an http.routeparamlist object; if 0, this attribute is ignored |
| | |
|---|---|
| Argument | Description |
| string | an HTTP header name |
| string | an HTTP header value |
| | |
|---|---|
| Argument | Description |
| long | an http.headerlist object; if 0, this attribute is ignored |
| | |
|---|---|
| Argument | Description |
| string | a value for the Accept HTTP header |
| | |
|---|---|
| Argument | Description |
| string | a value for the Conent-Type HTTP header |
| | |
|---|---|
| Argument | Description |
| long | the size of the body contents; if the size is -1, chunked transfer mode is used |
| | |
|---|---|
| Argument | Description |
| long | a stream id; the stream must be open for reading; passing 0 is interpreted as no stream |
| | |
|---|---|
| Argument | Description |
| string | a string that will be used as the body of the request |
| | |
|---|---|
| Argument | Description |
| string | a file path; the file must exist |
| | |
|---|---|
| Argument | Description |
| long | an http.mimepart object |
| | |
|---|---|
| Argument | Description |
| long | an http.mimepartlist object; if 0, this attribute will be ignored |
| | |
|---|---|
| Argument | Description |
| long | An Authentication type HTTP_AUTH_NONE: None HTTP_AUTH_BASIC: Basic Authentication HTTP_AUTH_DIGEST: Digest HTTP_AUTH_NEGOTIATE: Negotiate and find the most secure HTTP_AUTH_NTLM: NTLM Authentication HTTP_AUTH_DIGEST_IE: Digest with an IE flavor HTTP_AUTH_NTLM_WB: NLTM delegating to winbind helper HTTP_AUTH_BEARER: (introduced with TIV 2392) HTTP Bearer token authentication, used primarily in the OAuth 2.0 protocol; the specified name is used as the Bearer token HTTP_AUTH_ONLY: OR this with one of the above to try unrestricted and if that fails, only that single auth algorithm is acceptable HTTP_AUTH_ANY: Convenience: find the most secure HTTP_AUTH_ANYSAFE: Convenience: Find the most secure but never BASIC |
| string | a user name; this is the token in case of HTTP_AUTH_BEARER |
| string | a user password; specify an empty string in case of HTTP_AUTH_BEARER |
| | |
|---|---|
| Argument | Description |
| long | an http.oauth1params object |
| | |
|---|---|
| Argument | Description |
| long | an http.oauth2params object |
| | |
|---|---|
| Argument | Description |
| string | a proxy address |
| | |
|---|---|
| Argument | Description |
| long | a proxy port |
| | |
|---|---|
| Argument | Description |
| boolean | whether to use tunneling |
| | |
|---|---|
| Argument | Description |
| long | an Authentication type: See the options for HTTP_AUTH for more info |
| string | a user name |
| string | a user password |
| | |
|---|---|
| Argument | Description |
| string | a cookie string |
| | |
|---|---|
| Argument | Description |
| string | file path to cookie file |
| | |
|---|---|
| Argument | Description |
| string | an http.cookiejar object; if 0 this attribute will be ignored |
| | |
|---|---|
| Argument | Description |
| boolean | is auto redirect allowed |
| | |
|---|---|
| Argument | Description |
| long | the number of max redirects |
| | |
|---|---|
| Argument | Description |
| string | path to a directory |
| | |
|---|---|
| Argument | Description |
| string | path to a file |
| | |
|---|---|
| Argument | Description |
| string | path to a client certificate file |
| string | path to a private key file |
| string | password to a private key file |
| | |
|---|---|
| Argument | Description |
| boolean | peer verification enabled? |
| | |
|---|---|
| Argument | Description |
| boolean | host verification enabled? |
| | |
|---|---|
| Argument | Description |
| long | a stream id opened for writing |
| | |
|---|---|
| Argument | Description |
| long | the timeout |
| | |
|---|---|
| Argument | Description |
| string | value for the User-Agent |

## Return values
an http.response object; check the response object for information about whether the request succeeded
Note  Do not forget to delete the http.response object with [http.response.delete()](http.response.delete.md)

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- passed number of arguments must be valid

- passed argument types must be valid

- passed attributes/flags must be known

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
