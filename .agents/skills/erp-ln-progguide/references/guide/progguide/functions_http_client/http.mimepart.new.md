# http.mimepart.new()

## Syntax:
`#include <bic_httpclt>`
`function long http.mimepart.new(... )`

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
| | |
|---|---|
| Argument | Description |
| string | the content type; e.g. HTTP_CTYPE_APPLICATION_JSON (application/json) |
| | |
|---|---|
| Argument | Description |
| string | the part name |
| | |
|---|---|
| Argument | Description |
| string | the remote file name |
| | |
|---|---|
| Argument | Description |
| string | the body of the part as string |
| | |
|---|---|
| Argument | Description |
| string | a file path |
| | |
|---|---|
| Argument | Description |
| long | a stream id |
| long | the size in bytes of the data in the stream |
| | |
|---|---|
| Argument | Description |
| long | an http.headerlist object |
| | |
|---|---|
| Argument | Description |
| string | an encoder scheme; the following schemes are supported: "binary" - the data is left unchanged, the header is added. "8bit" - header added, no data change. "7bit" - the data is unchanged, but is each byte is checked to be a 7-bit value; if not, a read error occurs. "base64" - data is converted to base64 encoding, then split in CRLF-terminated lines of at most 76 characters. "quoted-printable" - data is encoded in quoted printable lines of at most 76 characters. Since the resulting size of the final data cannot be determined prior to reading the original data, it is left as unknown, causing chunked transfer. This encoder targets text data that is mostly ASCII and should not be used with other types of data. |

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
