# curl.download.stream()

## Syntax:
`#include <bic_curl>`
`function long curl.download.stream( const string url, long response.stream, [ long header.list ] )`

## Description
Downloads data from the specified url and writes it to the specified stream, which can be either a file or a memory stream.
Note that you have to rewind the stream first before reading data from the `response.stream`.

## Arguments
| | | |
|---|---|---|
| `const string` | `url` |  the url from where the data must be downloaded; this can be an http(s) or an ftp(s) address.  |
| `long` | `response.stream` |  the stream to write the downloaded data to  |
| `[ long` | `header.list ]` |  optional cURL slist handle containing HTTP headers; this can be created by ` [curl.slist.append()](curl.slist.append.md)` or ` [curl.slist.append_encrypted()](curl.slist.append_encrypted.md)`  |

## Return values
| | |
|---|---|
| 0 | Ok |
| < 0 | Stream IO error |
| > 0 | A cURL code; use ` [curl.strerror$()](curl.strerror$.md)` to get a descriptive message  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

long ret
long response
long header.list

header.list = 0
| tell the webserver to close the connection after downloading
header.list = curl.slist.append(header.list, "Connection: close")
| open a file stream to write the response to
response = seq.open("/home/user/app.exe", "w")
| now perform the download
ret = curl.download.stream("http://www.example.com/application.exe", response, header.list)
if ret = 0 then
	ret = seq.rewind(response)
	| process the data in the reponse stream.
endif
ret = seq.close(response)
| the HTML contents of the infor homepage is now stored in /tmp/infor.html
```

## Related topics
- [cURL handling overview](overview.md)
