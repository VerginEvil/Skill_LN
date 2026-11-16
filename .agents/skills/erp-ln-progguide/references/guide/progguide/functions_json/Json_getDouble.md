# Json.getDouble()

## Syntax:
`#include <bic_json>`
`function double Json.getDouble( long json_object, const string key )`

## Description
Convenience function for directly returning the 3GL double value of the JSON number value associated with the specified key of a JSON object.
The function is an alias for: `Json.getNumber(json, key)`

## Arguments
| | | |
|---|---|---|
| `long` | `json_object` |  A JSON object.  |
| `const string` | `key` |  The key of the number value to get.  |

## Return values
The JSON number value associated with the specified key, as a 3GL double value.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2370.

## Preconditions
- Parameter 'json' is a JSON value of type JSON_TYPE_OBJECT.

- The specified key exists.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
