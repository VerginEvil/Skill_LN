# curl.upload.string()

## Syntax:
`#include <bic_curl>`
`function long curl.upload.string( const string url, const string data, long response.stream, [ long header.list, const string method ] )`

## Description
Uploads a (null terminated) string to the specified url.

## Arguments
| | | |
|---|---|---|
| `const string` | `url` |  the url to where the string must be uploaded; this can be an http(s) or an ftp(s) address.  |
| `const string` | `data` |  the (null terminated) string to upload  |
| `long` | `response.stream` |  the stream (file or memory stream) to which the response of the upload must be written to  |
| `[ long` | `header.list ]` |  optional cURL slist handle containing HTTP headers; this can be created by [curl.slist.append()](curl.slist.append.md) or [curl.slist.append_encrypted()](curl.slist.append_encrypted.md). Specify 0 if no headers must be sent.  |
| `[ const string` | `method ]` |  optional HTTP method, specify "PUT" or "POST". "POST" is the default method.  |

## Return values
| | |
|---|---|
| 0 | Ok |
| < 0 | Stream IO error |
| > 0 | A cURL code; use [curl.strerror$()](curl.strerror$.md) to get a descriptive message |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

long	ret
long	opt
string	data(64)
long	response
string	response.data(128)
string	err.msg(256)

data = "the quick brown fox jumps over the lazy dog"
response = ims.openvba("w+)
| upload using the HTTP POST method
ret = curl.upload.string("http://www.example.com/upload/info.txt", data, response)
if ret = 0 then
	ims.rewind(response)
	while ims.gets(response.data, 128, opt, response) = 0
		| process response data, if any
	endwhile
else
	| handle the error
	err.msg = curl.strerror$(ret)
endif
ims.close(response)
```

## Related topics
- [cURL handling overview](overview.md)
