# Json.readFile()

## Syntax:
`#include <bic_json>`
`function long Json.readFile( const string path, ref string error_str, [ long options ] )`

## Description
Reads JSON text from a file, parses it and creates a JSON value from it.
By default, the JSON text is interpreted as UTF-8 text.

## Arguments
| | | |
|---|---|---|
| `const string` | `path` |  The path to the file to read the JSON text from.  |
| `ref string` | `error_str` |  A description of the error in case a parsing error occurs. This is an english text which can be used for logging and debugging purposes. You can use JSON_ERRSTR_SIZE to declare a string of the correct size.  |
| `[ long` | `options ]` |  The options to use when reading the JSON text; the following options can be specified: JSON_READ_UTF8 - specify this when the JSON text is encoded as UTF-8. JSON_READ_TSS - specify this when the JSON text is encoded as TSS. By default, the data is interpreted as UTF-8 text.  |

## Return values
A JSON value, or 0 in case of an error.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
