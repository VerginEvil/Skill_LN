# mb.rev$()

## Syntax:
`function string mb.rev$( string string_expr, [ long flags ] )`

## Description
*Deprecated.* This function is supported for backward compatibility reasons only. As of [object TIV](../tiv/tiv_overview.md) [level 2200](../tiv/tiv_2200.md) (specified with the -T option of the [compiler](../3gl_features/compiler.md)) using this function will trigger a compilation error.

## Arguments
| | | |
|---|---|---|
| `string` | `string_expr` |  |
| `[ long` | `flags ]` |  TSS_REVERSE TSS_FORCE_REVERSE  |

## Return values
The supplied *string_expr*.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
