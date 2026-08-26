# not.curr()

## Syntax:
`function void not.curr( string variable )`

## Description
This switches the current and previous values of the specified variable. This is considered a value change by the checking mechanism. So if you subsequently call [changed()](changed.md), that function will return TRUE.

## Arguments
| | | |
|---|---|---|
| `string` | `variable` |  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Variables (checking changes) overview](overview.md)
- [Variables (checking changes) synopsis](synopsis.md)
- [Variables (checking changes): sample program](example.md)
