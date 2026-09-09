# http.oauth2params.new()

## Syntax:
`#include <bic_httpclt>`
`function long http.oauth2params.new(... )`

## Description
Constructs a new http.oauth2params object. Use the attributes as specified below to specify the OAuth2 parameters.
Typically an http.oauth2params object is reused for several HTTP requests to the same web service.
Examples:
```

        long	oauth2params

        |* 1. use an OAuth 2.0 Parameter Set from session ttaad0108m000
        oauth2params = http.oauth2params.new(
           HTTP_OAUTH2_PARAMSET,        "Param Set 001")

        |* 2. specify the OAuth 2.0 attributes yourself
        oauth2params = http.oauth2params.new(
           HTTP_OAUTH2_GRANTTYPE,       HTTP_OAUTH2_PASSWORD_CREDENTIALS,
           HTTP_OAUTH2_CLIENTAUTH,      HTTP_OAUTH2_AS_BASIC_AUTH_HEADER,
           HTTP_OAUTH2_CLIENTID,        "<client_id>",
           HTTP_OAUTH2_CLIENTSECRET,    "<client_secret>",
           HTTP_OAUTH2_USERNAME,        "<username>",
           HTTP_OAUTH2_PASSWORD,        "<password>",
           HTTP_OAUTH2_ACCESSTOKENURL,  "https://example.com/oauth2/token",
           HTTP_OAUTH2_SCOPE,           "<scope>")

        |* 3. use an OAuth 2.0 token based on a SAML Assertion string (as of TIV 2530)
        oauth2params = http.oauth2params.new(
           HTTP_OAUTH2_GRANTTYPE,       HTTP_OAUTH2_SAML2_BEARER,
           HTTP_OAUTH2_SAMLASSERTION,   "<saml_assertion_string>",
           HTTP_OAUTH2_CLIENTAUTH,      HTTP_OAUTH2_AS_BASIC_AUTH_HEADER,
           HTTP_OAUTH2_CLIENTID,        "<client_id>",
           HTTP_OAUTH2_CLIENTSECRET,    "<client_secret>",
           HTTP_OAUTH2_ACCESSTOKENURL,  "https://example.com/oauth2/token",
           HTTP_OAUTH2_SCOPE,           "<scope>")

        |* 4. (LN CE only) use a SAML based OAuth 2.0 for the current LN user to access
        |* e.g. IONAPI services (as of TIV 2530)
        oauth2params = http.oauth2params.new(
           HTTP_OAUTH2_GRANTTYPE,       HTTP_OAUTH2_CURRENT_SAML2_BEARER)
```

## Arguments
| | |
|---|---|
| Argument | Description |
| string | the OAuth 2.0 Parameter Set name to use |
| | |
|---|---|
| Argument | Description |
| string | the Grant Type |
| | |
|---|---|
| Argument | Description |
| string | the Client Authentication location |
| | |
|---|---|
| Argument | Description |
| string | the Client ID |
| | |
|---|---|
| Argument | Description |
| string | the Client Secret |
| | |
|---|---|
| Argument | Description |
| string | the Username |
| | |
|---|---|
| Argument | Description |
| string | the Password |
| | |
|---|---|
| Argument | Description |
| string | the Access Token URL |
| | |
|---|---|
| Argument | Description |
| string | the OAuth2 scope that applies |
| | |
|---|---|
| Argument | Description |
| string | the HTTP header to use to pass the OAuth2 bearer token |
| | |
|---|---|
| Argument | Description |
| string | a SAML Assertion string |

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
