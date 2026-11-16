# rsc.boolean(), rsc.double(), rsc.enum(), rsc.long(), rsc.string()

## Syntax:
`function void rsc.boolean( string variable )`
`function void rsc.double( string variable )`
`function void rsc.enum( string variable )`
`function void rsc.long( string variable )`
`function void rsc.string( string variable )`

## Description
These convert a specified program variable to the corresponding resource value format (boolean, double, enum, and so on).

## Arguments
| | | |
|---|---|---|
| `string` | `variable` |    |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
See [rsc.put()](rsc.put.md).

## Related topics
- [Resource sets overview](overview.md)

- [Resource sets synopsis](synopsis.md)
