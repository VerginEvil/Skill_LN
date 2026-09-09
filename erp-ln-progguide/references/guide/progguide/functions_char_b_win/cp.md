# cp$()

## Syntax:
`function string cp$( long column, long row )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
Use this to position the cursor at the specified column and row. The cursor position is always relative to the upper left corner of the current window.

## Arguments
| | | |
|---|---|---|
| `long` | `column` |    |
| `long` | `row` |    |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
