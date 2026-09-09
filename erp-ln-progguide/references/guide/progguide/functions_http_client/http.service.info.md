# http.service.info()

## Syntax:
`#include <bic_httpclt>`
`function string http.service.info( const string service, const string info )`

## Description
Retrieves information about a webservice. It depends on the service what information can be retrieved.
Here follows a list of known services and the information that can be retrieved about them:
| | | | |
|---|---|---|---|
| Service | Property | Description | TIV |
| cpq | url | The CPQ URL. | 2530 |
|  | consumerKey | The CPQ OAuth 1.0 consumer key. | 2530 |
|  | consumerSecret | The CPQ OAuth 1.0 consumer secret. | 2530 |
| ionapi | endpoint | The IONAPI endpoint | 2530 |
Examples:
```

string  ionapi.url(256)

ionapi.url = http.service.info("ionapi", "url")
```

## Arguments
| | | |
|---|---|---|
| `const string` | `service` |  A webservice name, e.g. "ionapi"  |
| `const string` | `info` |  The information that is requested, e.g. "endpoint"  |

## Return values
The requested information as a string, or an empty string if the information was not found

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2530.

## Preconditions
- the specified webservice must be known

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
