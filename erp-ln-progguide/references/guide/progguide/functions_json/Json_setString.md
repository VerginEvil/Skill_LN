# Json.setString()

## Syntax:
`#include <bic_json>`
`function long Json.setString( long json_object, const string key, const string value )`

## Description
Convenience function for directly associating a 3GL string value with a key in a JSON object. The 3GL string value is first converted to a JSON string value, which is then associated with the specified key.
The function is a shorthand for: `Json.set(json, key, Json.newString(value))`

## Arguments
| | | |
|---|---|---|
| `long` | `json_object` |  A JSON object.  |
| `const string` | `key` |  The key to associate the JSON string value with.  |
| `const string` | `value` |  The 3GL string value for which a JSON string value is created, which is then associated with the key.  |

## Return values
Optional, the new JSON string value that has been associated with the key.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_object' is a JSON value of type JSON_TYPE_OBJECT.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
