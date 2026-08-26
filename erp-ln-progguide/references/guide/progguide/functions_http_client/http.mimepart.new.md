# http.mimepart.new()

## Syntax:
`#include <bic_httpclt>`
`function long http.mimepart.new( ... )`

## Description
Constructs a new http.mimepart object. Use the attributes as specified below to configure the MIME part.
Example:
```

        long	mimepart

        mimepart = http.mimepart.new(
           HTTP_MIME_CONTENTTYPE, "application/json",
           HTTP_MIME_NAME,        "part1",
           HTTP_MIME_STRING,      "{ ""key"": ""value"" }",
           HTTP_MIME_ENCODER,     "base64")
```

## Arguments
| | | |
|---|---|---|
| `` | `...` |  Attributes to configure the MIME part; the following HTTP_MIME attributes are supported:  |

## Return values
a new http.mimepart object, or 0 in case of an error

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2220.

## Preconditions
- passed number of arguments must be valid
- passed argument types must be valid
- passed attributes/flags must be known

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
