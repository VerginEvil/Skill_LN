# tt.field.desc()

## Syntax:
`function string tt.field.desc( string field(17), ref string desc() mb )`

## Description
This retrieves information about a specified table field. It is returned, and optionally also stored in the *desc* argument. (The optional argument is only present for backward compatibility.)

## Arguments
| | | |
|---|---|---|
| `string` | `field(17)` |  The field name.  |
| `ref string` | `desc() mb` |  This returns the field description in the user's current language.  |

## Return values
The description is returned.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
