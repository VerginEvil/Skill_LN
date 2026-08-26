# rsc.setboolean() *

## Syntax:
`function void rsc.setboolean( string variable, string value(40) )`
`function void rsc.setdouble( string variable, string value(40) )`
`function void rsc.setenum( string variable, string value(40) )`
`function void rsc.setlong( string variable, string value(40) )`
`function void rsc.setstring( string variable, string value(40) )`

## Description
These store a resource value of a particular type in a specified program variable.

## Arguments
| | | |
|---|---|---|
| `string` | `variable` |  |
| `string` | `value(40)` |  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## rsc.setdouble(), rsc.setenum(), rsc.setlong(),rsc.setstring()

## Example
See [rsc.get()](rsc.get.md).

## Related topics
- [Resource sets overview](overview.md)
- [Resource sets synopsis](synopsis.md)
