# set.ask.enum.values()

## Syntax:
`function void set.ask.enum.values( enum_constant,... enum_constant )`

## Description
This restricts the values valid for the ask.enum() function. Only the values specified are shown as buttons.

## Arguments
| | | |
|---|---|---|
| `enum_constant,...` | `enum_constant` |  List of enum_constants.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Notes  This function replaces the function set.enum.values().
In the case of enumerated fields, use [set.enum.values.for.field()](set.enum.values.for.field.md) or [set.enum.array.for.field()](set.enum.array.for.field.md).
After execution of *ask.enum()*, the specified enum values are cleared again. So you have to call *set.ask.enum.values()* again before calling *ask.enum()*. This also happens when the [4GL engine](../glossary/glossary.md#fourgl_engine) calls *ask.enum()*.

## Related topics
- [Enumerates overview and synopsis](overview_and_synopsis.md)

- [Enumerate and set constants](../3gl_features/enumerate_and_set_constants.md)
