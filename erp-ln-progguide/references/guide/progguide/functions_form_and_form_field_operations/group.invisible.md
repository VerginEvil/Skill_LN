# group.invisible()

## Syntax:
`function void group.invisible( long group.nr )`

## Description
This hides the specified group completely, including all associated fields, labels, and subgroups. The *group.nr* argument specifies the group number, as defined in the form editor. The group cannot be made visible again.
This function is relevant to dynamic forms only and can be used only in the before.program and in the after.form.read section of 4GL scripts.

## Arguments
| | | |
|---|---|---|
| `long` | `group.nr` |   |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
```

before.program:
    group.invisible(3)
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
