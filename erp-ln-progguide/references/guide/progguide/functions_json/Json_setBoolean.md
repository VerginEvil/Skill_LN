# Json.setBoolean()

## Syntax:
`#include <bic_json>`
`function long Json.setBoolean( long json_object, const string key, boolean value )`

## Description
Convenience function for directly associating a 3GL boolean value with a key in a JSON object. The 3GL boolean value is first converted to a JSON boolean value, which is then associated with the specified key.
The function is a shorthand for: `Json.set(json, key, Json.newBoolean(value))`

## Arguments
| | | |
|---|---|---|
| `long` | `json_object` |  A JSON object.  |
| `const string` | `key` |  The key to associate the JSON boolean value with.  |
| `boolean` | `value` |  The 3GL boolean value for which a JSON boolean value is created, which is then associated with the key.  |

## Return values
Optional, the new JSON boolean value that has been associated with the key.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_object' is a JSON value of type JSON_TYPE_OBJECT.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
