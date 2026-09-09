# Json.writeString()

## Syntax:
`#include <bic_json>`
`function long Json.writeString( long json_value, ref string str, [ long options ] )`

## Description
Writes a JSON value object to a string as JSON text.
By default, no UTF-8 conversion is done and no additional formatting is done.

## Arguments
| | | |
|---|---|---|
| `long` | `json_value` |  A JSON value.  |
| `ref string` | `str` |  The string to write the JSON text to; as of TIV 2300, if a BASED string is passed, the string will be resized such that the complete JSON text will fit in the string. If the TIV is less than 2300 or when a non-BASED string is passed, the string should be large enough to contain the complete JSON text; in case it is hard to tell the size upfront, it is advised to use function Json.write() instead.  |
| `[ long` | `options ]` |  The options to use when writing the JSON text; the following options can be specified: JSON_WRITE_UTF8 - converts the JSON text to UTF-8. JSON_WRITE_TSS - converts the JSON text to TSS. JSON_WRITE_PRETTY - adds new-lines and indents to make the output human readable. JSON_WRITE_COMPACT - no whitespace is added between JSON tokens. By default none of these options are enabled, meaning the JSON text is written in TSS encoding, not pretty and not compact.  |

## Return values
>= 0: the number of bytes written to the string when successful
< 0: in case of a failure [e.g. when the string to write to is too small]
variable 'e' contains an error code, [e.g. ENOSPC]

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_value' is a JSON value.

- Parameter 'str' has been allocated (either statically or dynamically).

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
