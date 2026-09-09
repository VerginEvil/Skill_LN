# standard.commands.off()

## Syntax:
`function void standard.commands.off( long command,... )`

## Description
In session Standard Commands (ttadv3110s000) you can define which standard commands are available to the user. E.g. you can permanently disable the File | New (ADD.SET) command by unchecking its check box.
With function standard.commands.off(), you can turn off standard commands programmatically. That makes it possible to turn off standard commands based on a certain parameter setting.

## Arguments
| | | |
|---|---|---|
| `long` | `command,...` |  The IDs of one or more standard commands that must be turned off. E.g. ADD.SET, MODIFY.SET, DEF.FIND.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

- Standard commands that have been turned off cannot be turned on again.

- You can use this function only in the *after.form.read* section.

## Example
```

after.form.read:
    if <some parameter has a certain value> then
        standard.commands.off(ADD.SET, MARK.DELETE)
    endif
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
