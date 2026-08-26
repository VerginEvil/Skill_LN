# http.oauth1params.new()

## Syntax:
`#include <bic_httpclt>`
`function long http.oauth1params.new( ... )`

## Description
Constructs a new http.oauth1params object. Use the attributes as specified below to specify the OAuth1 parameters.
Example:
```

        long	oauth1params

        oauth1params = http.oauth1params.new(
           HTTP_OAUTH1_SIGNATUREMETHOD, "HMAC-SHA1",
           HTTP_OAUTH1_CONSUMERKEY,     "some_key",
           HTTP_OAUTH1_CONSUMERSECRET,  "some_secret")
```

## Arguments
| | | |
|---|---|---|
| `` | `...` |  The following HTTP_OAUTH1 attributes can be specified:  |

## Return values
a new http.oauth1params object, or 0 in case of an error

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2340.

## Preconditions
- passed number of arguments must be valid
- passed argument types must be valid
- passed attributes/flags must be known

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
