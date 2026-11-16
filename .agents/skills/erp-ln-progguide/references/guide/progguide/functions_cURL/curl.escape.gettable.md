# curl.escape.gettable()

## Syntax:
`function void curl.escape.gettable( ref string(2,128) EscapeTable )`

## Description
Returns a string array with an escapetable.

## Arguments
| | | |
|---|---|---|
| `ref string(2,128)` | `EscapeTable` |  Two dimensional array with escape table  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [cURL handling overview](overview.md)
