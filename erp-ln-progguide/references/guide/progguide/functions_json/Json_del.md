# Json.del()

## Syntax:
`#include <bic_json>`
`function void Json.del( long json_object, const string key )`

## Description
Deletes the specified key from a JSON object. The associated JSON value is deleted as well.

## Arguments
| | | |
|---|---|---|
| `long` | `json_object` |  A JSON object.  |
| `const string` | `key` |  The key to delete from the JSON object.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_object' is a JSON value of type JSON_TYPE_OBJECT.

- The specified key exists.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
