# Json.type()

## Syntax:
`#include <bic_json>`
`function long Json.type( long json_value )`

## Description
Returns the type of a JSON value.

## Arguments
| | | |
|---|---|---|
| `long` | `json_value` |  A JSON value.  |

## Return values
The type of the JSON value. One of { JSON_TYPE_OBJECT, JSON_TYPE_ARRAY, JSON_TYPE_BOOLEAN, JSON_TYPE_NUMBER, JSON_TYPE_STRING, JSON_TYPE_NULL, JSON_TYPE_UNKNOWN }.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
