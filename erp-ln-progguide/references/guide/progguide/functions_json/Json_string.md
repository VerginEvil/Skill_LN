# Json.string()

## Syntax:
`#include <bic_json>`
`function string Json.string( long json_value )`

## Description
Returns the 3GL string value of a JSON string value.

## Arguments
| | | |
|---|---|---|
| `long` | `json_value` |  A JSON string value.  |

## Return values
The string contained in the JSON string value.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_value' is a JSON value of type JSON_TYPE_STRING.

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
