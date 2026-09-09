# Json.set()

## Syntax:
`#include <bic_json>`
`function long Json.set( long json_object, const string key, long json_value )`

## Description
Associates a JSON value with a key in a JSON object. If the key does not yet exist, it is created first. If the key already exists, its current JSON value is deleted and replaced by the new value.

## Arguments
| | | |
|---|---|---|
| `long` | `json_object` |  A JSON object.  |
| `const string` | `key` |  The key to associate a JSON value with.  |
| `long` | `json_value` |  The new JSON value to associate with the key.  |

## Return values
Optional, the new JSON value that has been associated with the key.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_object' is a JSON value of type JSON_TYPE_OBJECT.

- Parameter 'json_value' is a JSON value.

- Parameter 'json_value' is detached (i.e. not assigned to a member of another JSON object or JSON array)

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
