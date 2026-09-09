# Json.has()

## Syntax:
`#include <bic_json>`
`function boolean Json.has( long json_object, const string key )`

## Description
Tests whether a JSON object contains the specified key.

## Arguments
| | | |
|---|---|---|
| `long` | `json_object` |  A JSON object.  |
| `const string` | `key` |  The key to check.  |

## Return values
*true* if the specified key exists, else *false*

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_object' is a JSON value of type JSON_TYPE_OBJECT.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
