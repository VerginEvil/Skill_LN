# create.extra.toolbar()

## Syntax:
`function long create.extra.toolbar( string form_command, string gif_file, [ string form_command, string gif_file ] )`

## Description
Worktop: This adds a secondary toolbar to a session.
LN-UI: This adds the default icons to the commands. No secondary toolbar will be created.

## Arguments
| | | |
|---|---|---|
| `string` | `form_command` |    |
| `string` | `gif_file` |  A gif file is the default. If a svg or png file is wanted, the extension should be added to the file name (e.g. "confirmed.svg")  |
| `[ string` | `form_command ]` |    |
| `[ string` | `gif_file ]` |    |

## Return values
> 0 success
0 toolbar not allowed in this type of session
-1 incorrect number of arguments

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Example
```

create.extra.toolbar( "check.out","checkout",
                                  "", "",
                                  "edit.script", "modify1",
                                  "compile", "compile",
                                  "", "",
                                  "check.in", "checkin" )
```

## Related topics
- [Secondary toolbars overview and synopsis](overview_and_synopsis.md)
