# rbhp.query.extend.where()

## Syntax:
`#pragma used dll "ottstprbhp"`
`function void rbhp.query.extend.where( const string where.extension )`

## Description
Set the *WHERE* clause extension to be used when starting the session. No syntax checking on the passed extension will be done. This extension will be appended to the extension set by the session. This function can only be called from the application function: tcint.dll0001.drill.back().

## Arguments
| | | |
|---|---|---|
| `const string` | `where.extension` |  A string containing *WHERE* clause extension.  |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Role Based Home Pages overview](overview.md)

- [Role Based Home Pages synopsis](synopsis.md)
