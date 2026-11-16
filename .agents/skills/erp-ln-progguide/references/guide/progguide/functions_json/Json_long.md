# Json.long()

## Syntax:
`#include <bic_json>`
`function long Json.long( long json_value )`

## Description
Returns a JSON number value as a 3GL long value.
Note that if the actual value stored in the JSON number is a double value, the value is truncated. E.g. 1.234 becomes 1.
This function is a shorthand for: `int(Json.number(json))`

## Arguments
| | | |
|---|---|---|
| `long` | `json_value` |  A JSON number value.  |

## Return values
The value contained in the JSON number value as a long.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2370.

## Preconditions
- Parameter 'json_value' is a JSON value of type JSON_TYPE_NUMBER.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
