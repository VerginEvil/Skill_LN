# tt.short.field.desc()

## Syntax:
`function string tt.short.field.desc( string field(17), long length, ref string desc() mb )`

## Description
This returns the description (in the user's current language) of a specified table field. It is returned, and optionally also stored in the *desc* argument. (The optional argument is only present for backward compatibility.)

## Arguments
| | | |
|---|---|---|
| `string` | `field(17)` |  The field name.  |
| `long` | `length` |  The number of characters of the description that must be returned.  |
| `ref string` | `desc() mb` |  This returns the field description. Only the first *length* characters of the description are returned.  |

## Return values
The description is returned.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
