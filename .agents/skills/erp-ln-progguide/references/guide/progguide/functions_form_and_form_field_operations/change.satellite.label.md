# change.satellite.label()

## Syntax:
`function void change.satellite.label( const string session.code, const string description )`

## Description
Use this to change the text shown on the tab of a satellite session.
This function can only be used in the `after.form.read` section of an MMT Controller.

## Arguments
| | | |
|---|---|---|
| `const string` | `session.code` |  The session code of the satellite.  |
| `const string` | `description` |  The new text to show on the tab of the satellite.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2110.

## Example
```

after.form.read:
	change.satellite.label("tirpt4121m100", tt.label.desc("act.material", ttadv.cont.general))
	|* Actual Materials
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
