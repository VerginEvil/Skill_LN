# rbhp.set.error.message()

## Syntax:
`#pragma used dll "ottstprbhp"`
`function void rbhp.set.error.message( const string mess.or.code, [ void arg... ] )`

## Description
Set error message and/or error code to be reported to the end user when during the tcint.dll0001.drill.back() function an error occurred. This function can only be called from the application function: tcint.dll0001.drill.back().

## Arguments
| | | |
|---|---|---|
| `const string` | `mess.or.code` |  Specifies either the data dictionary code for the message or a literal string. In the latter case, the value of *mess.or.code* must start with the at sign [@]. Note that using a literal string makes the script language dependent.  |
| `[ void` | `arg... ]` |  The literal string or message specified with *mess.or.code* can contain format characters for parameter substitution. The values which must be substituted are specified in the 2nd, 3rd,... arguments of the function. The number of these arguments is variable. For details about formatting a string see the [sprintf$()](../functions_formatting_io/sprintf.md).  |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Role Based Home Pages overview](overview.md)

- [Role Based Home Pages synopsis](synopsis.md)
