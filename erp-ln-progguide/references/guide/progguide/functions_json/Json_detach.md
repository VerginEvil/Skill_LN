# Json.detach()

## Syntax:
`#include <bic_json>`
`function [long] Json.detach( long json_value )`

## Description
Detaches a JSON value from its parent JSON object or JSON array. After calling this function, the JSON value is no longer a member of its parent. The member of the parent JSON object or array is assigned the JSON null value.

## Arguments
| | | |
|---|---|---|
| `long` | `json_value` |  A JSON value.  |

## Return values
Optional, the detached JSON value.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_value' is a JSON value.

## Postconditions
- The passed JSON value is detached from its parent.
- The parent JSON value's member is assigned the JSON null value.

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
