# get.cp()

## Syntax:
`function void get.cp( ref long x, ref long y )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
This stores the coordinates of the current cursor position in the *x* and *y* arguments.

## Arguments
| | | |
|---|---|---|
| `ref long` | `x` |  |
| `ref long` | `y` |  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
