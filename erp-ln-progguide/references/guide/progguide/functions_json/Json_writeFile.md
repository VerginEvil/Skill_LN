# Json.writeFile()

## Syntax:
`#include <bic_json>`
`function long Json.writeFile( long json_value, const string path, [ long options ] )`

## Description
Writes a JSON value to a file as JSON text.
By default, the JSON text is converted to UTF-8 and extra new-lines and indents are added to make the output human readable.

## Arguments
-
-
-
-
| | | |
|---|---|---|
| `long` | `json_value` |  A JSON value.  |
| `const string` | `path` |  The path to the file to write the JSON text to; if the file already exists it is overwritten.  |
| `[ long` | `options ]` |  The options to use when writing the JSON text; the following options can be specified: JSON_WRITE_UTF8 - converts the JSON text to UTF-8. JSON_WRITE_TSS - converts the JSON text to TSS. JSON_WRITE_PRETTY - adds new-lines and indents to make the output human readable. JSON_WRITE_COMPACT - no whitespace is added between JSON tokens. By default, the file is written in pretty mode and in UTF-8 format.  |

## Return values
>= 0: the number of bytes written to the file when successful
< 0: in case of a failure
variable 'e' contains an error code [e.g. ENOSPC]

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_value' is a JSON value.

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
