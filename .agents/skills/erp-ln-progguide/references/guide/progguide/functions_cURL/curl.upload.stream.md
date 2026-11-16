# curl.upload.stream()

## Syntax:
`#include <bic_curl>`
`function long curl.upload.stream( const string url, long request.stream, long data.size, long response.stream, [ long header.list, const string method ] )`

## Description
Uploads data from a stream (a file or a memory stream) to the specified url.

## Arguments
| | | |
|---|---|---|
| `const string` | `url` |  the url to where the data must be uploaded; this can be an http(s) or an ftp(s) address.  |
| `long` | `request.stream` |  the stream data to upload  |
| `long` | `data.size` |  the size of the data to upload, in bytes; specify -1 to enforce sending the request in chunks  |
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

long ret
long xmlrequest
long xmlresponse
long data.size
long request
long response
string response.data(128)
string err.msg(256)

| construct an xml tree
xmlrequest = xmlNewNode("Root")
| add nodes and attributes ...

| open a request stream buffer
request = ims.openvba("w+")
| write the xml tree to the request stream
data.size = xmlWrite(request, xmlrequest)
| rewind, so the stream pointer points to the beginning of the stream
ims.rewind(request)
| open a response stream buffer
response = ims.openvba("w+)
| upload using the HTTP POST method
ret = curl.upload.stream("http://www.example.com/upload/info.txt", request, data.size, response)
if ret = 0 then
	ims.rewind(response)
	xmlresponse = xmlRead(response, err.msg)
	if xmlresponse <> 0 then
		| do something with the xml response tree
	else
		| handle error
	endif
else
	| handle the curl error
	err.msg = curl.strerror$(ret)
endif
| cleanup
ims.close(request)
ims.close(response)
xmlDelete(xmlrequest)
xmlDelete(xmlresponse)
```

## Related topics
- [cURL handling overview](overview.md)
