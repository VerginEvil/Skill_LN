# curl.download.string()

## Syntax:
`#include <bic_curl>`
`function long curl.download.string( const string url, ref string data, [ long header.list ] )`

## Description
Downloads data from the specified url and writes it to the specified string buffer. Note that the string buffer must be large enough to store all data. The data will be null terminated, if possible.

## Arguments
| | | |
|---|---|---|
| `const string` | `url` |  the url from where the data must be downloaded; this can be an http(s) or an ftp(s) address.  |
| `ref string` | `data` |  the string buffer to write the downloaded data to  |
| `[ long` | `header.list ]` |  optional cURL slist handle containing HTTP headers; this can be created by [curl.slist.append()](curl.slist.append.md) or [curl.slist.append_encrypted()](curl.slist.append_encrypted.md)  |

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
string data(64 * 1024) | 64 Kb

ret = curl.download.string("http://www.infor.com", data)
| data now contains the Infor homepage as a string
```

## Related topics
- [cURL handling overview](overview.md)
