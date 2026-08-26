# tt.session.desc()

## Syntax:
`function string tt.session.desc( string session(13), [ ref string desc() mb, string language ] )`

## Description
This retrieves the description of a specified session ( *session*). It is returned, and optionally also stored in the *desc* argument. (The optional argument is only present for backward compatibility.)
Optional the language code for the description can be specified. Default the description will be retrieved in the user's current language

## Arguments
| | | |
|---|---|---|
| `string` | `session(13)` |  |
| `[ ref string` | `desc() mb ]` |  |
| `[ string` | `language ]` |  |

## Return values
The description is returned.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
