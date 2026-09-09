# Json.setNumber()

## Syntax:
`#include <bic_json>`
`function [long] Json.setNumber( long json_object, const string key, long|double value )`

## Description
Convenience function for directly associating a 3GL long or double value with a key in a JSON object. The 3GL long or double value is first converted to a JSON number value, which is then associated with the specified key.
The function is a shorthand for: `Json.set(json, key, Json.newNumber(value))`

## Arguments
| | | |
|---|---|---|
| `long` | `json_object` |  A JSON object.  |
| `const string` | `key` |  The key to associate the JSON number value with.  |
| `long|double` | `value` |  The 3GL long or double value for which a JSON number value is created, which is then associated with the key.  |

## Return values
Optional, the new JSON number value that has been associated with the key.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_object' is a JSON value of type JSON_TYPE_OBJECT.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
