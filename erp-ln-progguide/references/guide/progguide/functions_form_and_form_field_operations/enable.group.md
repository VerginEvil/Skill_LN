# enable.group()

## Syntax:
`function void enable.group( long group.nr, [ long occurrence ] )`

## Description
This enables all the fields of the specified (dynamic) group. See [enable.fields()](enable.fields.md).
This function is relevant to dynamic forms only.

## Arguments
| | | |
|---|---|---|
| `long` | `group.nr` |   |
| `[ long` | `occurrence ]` |   |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Example
```

|Enable group
enable.group(7)
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
