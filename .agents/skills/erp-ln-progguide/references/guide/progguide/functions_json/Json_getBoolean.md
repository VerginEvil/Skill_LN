# Json.getBoolean()

## Syntax:
`#include <bic_json>`
`function boolean Json.getBoolean( long json_object, const string key )`

## Description
Convenience function for directly returning the 3GL boolean value of the JSON boolean value associated with the specified key of a JSON object.
The function is a shorthand for: `Json.boolean(Json.get(json, key))`

## Arguments
| | | |
|---|---|---|
| `long` | `json_object` |  A JSON object.  |
| `const string` | `key` |  The key of the boolean value to get.  |

## Return values
The 3GL boolean value associated with the specified key, true or false.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_object' is a JSON value of type JSON_TYPE_OBJECT.

- The specified key exists.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
