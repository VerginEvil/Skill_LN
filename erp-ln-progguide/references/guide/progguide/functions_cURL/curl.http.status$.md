# curl.http.status$()

## Syntax:
`#include <bic_curl>`
`function string curl.http.status$( long http.status )`

## Description
Returns a english descriptive text for a given HTTP Status Code. E.g. when 200 (HTTP_STATUS_OK) is passed "OK" is returned, or when 503 (HTTP_STATUS_SERVICE_UNAVAILABLE) is passed, "Service Unavailable" is returned.
The descriptive text is meant for logging and tracing purposes and/or technical error messages.

## Arguments
| | | |
|---|---|---|
| `long` | `http.status` |  a HTTP Status code, like `200 (HTTP_STATUS_OK), 404 (HTTP_STATUS_NOT_FOUND), or 500 (HTTP_STATUS_INTERNAL_SERVER_ERROR)`  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

long ret
string data(64 * 1024) | 64 Kb
long http.status
string http.status.msg(100)

ret = curl.download.string("http://www.infor.com", data)
if ret = 0 then
	| data now contains the Infor homepage as a string
else
	| error, e.g. because the webservice is unavailable (503)
	http.status = curl.getinfo.response_code()
	http.status.msg = curl.http.status$(http.status)
	| http.status.msg now contains "Service Unavailable"
endif
```

## Related topics
- [cURL handling overview](overview.md)
