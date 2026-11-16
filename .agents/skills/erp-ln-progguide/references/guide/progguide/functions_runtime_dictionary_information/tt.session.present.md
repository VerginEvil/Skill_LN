# tt.session.present()

## Syntax:
`function long tt.session.present( string session(13) )`

## Description
This checks if the specified session is present in the runtime dictionary.

## Arguments
| | | |
|---|---|---|
| `string` | `session(13)` |    |

## Return values
0 session not present
1 session present but not in the user configuration
2 session present and in the configuration of the user

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
