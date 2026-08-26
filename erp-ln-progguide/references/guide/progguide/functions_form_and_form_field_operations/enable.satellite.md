# enable.satellite()

## Syntax:
`function void enable.satellite( const string session.code )`

## Description
This enables the specified satellite. The TAB on which the satellite is shown will become enabled when it was disabled. Initially all satellite TAB buttons are enabled.
This function is relevant in multi-main table controller sessions only.

## Arguments
| | | |
|---|---|---|
| `const string` | `session.code` |   |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
Notes  Use the function [disable.satellite()](disable.satellite.md) to disable a satellite TAB.
The focus will change to the first enabled satellite as defined by WorkTop. To avoid this behavior, enable satellites before disable satellites. Change the focus with [to.satellite()](to.satellite.md)

## Example
```

			|Enable satellite
			enable.satellite("tssoc2110m000")
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
