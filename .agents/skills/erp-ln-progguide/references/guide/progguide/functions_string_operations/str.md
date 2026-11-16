# str$()

## Syntax:
`function string str$( void input.value )`

## Description
The function str$ converts the supplied input value from its original type to type string.
Typical usage of this function includes (but is not restricted to) the conversion of an integer or floating point value to its decimal string representation.

## Arguments
| | | |
|---|---|---|
| `void` | `input.value` |    |

## Return values
[Implicit conversion](../3gl_features/type_conversions.md#implicit_type_conversion) of the input value from its original type to type string is performed. The resulting string value is returned.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [lval()](lval.md)

- [string.to.bounded.long()](string.to.bounded.long.md)

- [val()](val.md)

- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
