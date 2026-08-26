# set.checked.command()

## Syntax:
`function void set.checked.command( string command, boolean checked )`

## Description
Use this to check or uncheck a command in the menubar or the toolbar. This can be used to indicate to the user that the command is activated. Example:
Passing TRUE as the 2nd argument to this function will place a check mark in front of the command in the menubar. If the command is also shown as a toolbar icon then the icon will appear pressed.

## Arguments
| | | |
|---|---|---|
| `string` | `command` |  The name of the form command that must appear checked or unchecked.  |
| `boolean` | `checked` |  Specify TRUE if you want the command to appear checked. Specify FALSE to show the command unchecked.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Example
```

functions:

function extern void toggle.filter()        | Form command
{
static  boolean filter.active

    | Toggle the filter
    filter.active = not filter.active

    | Change the appearance of the form command
    set.checked.command("toggle.filter", filter.active)

    | The filter implementation...
    if filter.active then
        ...
    else
        ...
    endif
}
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
