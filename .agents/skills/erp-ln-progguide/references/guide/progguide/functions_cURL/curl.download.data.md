# curl.download.data()

## Syntax:
`#include <bic_curl>`
`function long curl.download.data( const string url, ref string data, ref long data.size, [ long header.list ] )`

## Description
Downloads data from the specified url and writes it to the specified data buffer. Note that the buffer must be large enough to store all downloaded data.

## Arguments
| | | |
|---|---|---|
| `const string` | `url` |  the url from where the data must be downloaded; this can be an http(s) or an ftp(s) address.  |
| `ref string` | `data` |  the data buffer to write the downloaded data to  |
| `ref long` | `data.size` |  the number of bytes downloaded  |
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
long data.size

ret = curl.download.data("http://www.example.com/presentation.ppt", data, data.size)
| the contents of the file presentation.ppt is now stored in 'data'
```

## Related topics
- [cURL handling overview](overview.md)
