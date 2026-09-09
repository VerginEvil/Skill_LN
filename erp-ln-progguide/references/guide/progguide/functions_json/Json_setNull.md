# Json.setNull()

## Syntax:
`#include <bic_json>`
`function long Json.setNull( long json_object, const string key )`

## Description
Convenience function for associating a JSON null value with a key in a JSON object.
The function is a shorthand for: `Json.set(json, key, Json.newNull())`

## Arguments
| | | |
|---|---|---|
| `long` | `json_object` |  A JSON object.  |
| `const string` | `key` |  The key to associate the JSON null value with.  |

## Return values
Optional, the new JSON null value that has been associated with the key.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_object' is a JSON value of type JSON_TYPE_OBJECT.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
