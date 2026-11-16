# disable.group()

## Syntax:
`function void disable.group( long group.nr, [ long type, long occurrence ] )`

## Description
This disables all the fields of the specified (dynamic) group. See [disable.fields()](disable.fields.md).
There is a second, optional, argument that can have two possible values:
| | |
|---|---|
| DISABLE | The default mode, it does not need to be specified. |
| READONLY | In this mode the fields become read-only and cannot be edited by the user. |
This function is relevant to dynamic forms only.

## Arguments
| | | |
|---|---|---|
| `long` | `group.nr` |  The group number.  |
| `[ long` | `type ]` |  Type.  |
| `[ long` | `occurrence ]` |  The occurrence.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
```

|Disable group
disable.group(7)
disable.group(5,READONLY)
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
