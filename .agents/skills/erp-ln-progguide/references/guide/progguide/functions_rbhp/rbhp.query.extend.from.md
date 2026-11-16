# rbhp.query.extend.from()

## Syntax:
`#pragma used dll "ottstprbhp"`
`function void rbhp.query.extend.from( const string from.extension )`

## Description
Set the *FROM* clause extension to be used when starting the session. No syntax checking on the passed extension will be done. This extension will be appended to the extension set by the session. This function can only be called from the application function: tcint.dll0001.drill.back().

## Arguments
| | | |
|---|---|---|
| `const string` | `from.extension` |  A string containing *FROM* clause extension.  |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Role Based Home Pages overview](overview.md)

- [Role Based Home Pages synopsis](synopsis.md)
