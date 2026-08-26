# Json.write()

## Syntax:
`#include <bic_json>`
`function long Json.write( long json_value, long stream, [ long options ] )`

## Description
Writes a JSON value to a stream as JSON text. This can be an already opened file, or an in-memory stream.
By default, the JSON text is converted to UTF-8 and the output is written in compact mode (ie. no whitespace is added between JSON tokens).

## Arguments
-
-
-
-
| | | |
|---|---|---|
| `long` | `json_value` |  A JSON value.  |
| `long` | `stream` |  The stream to write the JSON text to.  |
| `[ long` | `options ]` |  The options to use when writing the JSON text; the following options can be specified: JSON_WRITE_UTF8 - converts the JSON text to UTF-8. JSON_WRITE_TSS - converts the JSON text to TSS. JSON_WRITE_PRETTY - adds new-lines and indents to make the output human readable. JSON_WRITE_COMPACT - no whitespace is added between JSON tokens. By default, the file is written in compact mode and in UTF-8 format.  |

## Return values
>= 0: the number of bytes written to the stream when successful
< 0: in case of a failure [e.g. when the string to write to is too small]
variable 'e' contains an error code, [e.g. ENOSPC]

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_value' is a JSON value.

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
