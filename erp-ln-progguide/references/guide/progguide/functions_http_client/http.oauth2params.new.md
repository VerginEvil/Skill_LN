# http.oauth2params.new()

## Syntax:
`#include <bic_httpclt>`
`function long http.oauth2params.new( ... )`

## Description
Constructs a new http.oauth2params object. Use the attributes as specified below to specify the OAuth2 parameters.
Typically an http.oauth2params object is reused for several HTTP requests to the same web service.
Examples:
```

        long	oauth2params

        |* you can use an OAuth 2.0 Parameter Set from session ttaad0108m000
        oauth2params = http.oauth2params.new(
           HTTP_OAUTH2_PARAMSET,        "Param Set 001")

        |* or specify the OAuth 2.0 attributes yourself
        oauth2params = http.oauth2params.new(
           HTTP_OAUTH2_GRANTTYPE,       HTTP_OAUTH2_PASSWORD_CREDENTIALS,
           HTTP_OAUTH2_CLIENTAUTH,      HTTP_OAUTH2_AS_BASIC_AUTH_HEADER,
           HTTP_OAUTH2_CLIENTID,        "<client_id>",
           HTTP_OAUTH2_CLIENTSECRET,    "<client_secret>",
           HTTP_OAUTH2_USERNAME,        "<username>",
           HTTP_OAUTH2_PASSWORD,        "<password>",
           HTTP_OAUTH2_ACCESSTOKENURL,  "https://example.com/oauth2/token",
           HTTP_OAUTH2_SCOPE,           "<scope>")
```

## Arguments
| | | |
|---|---|---|
| `` | `...` |  The following HTTP_OAUTH2 attributes can be specified:  |

## Return values
a new http.oauth2params object, or 0 in case of an error

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2470.

## Preconditions
- passed number of arguments must be valid
- passed argument types must be valid
- passed attributes/flags must be known

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
