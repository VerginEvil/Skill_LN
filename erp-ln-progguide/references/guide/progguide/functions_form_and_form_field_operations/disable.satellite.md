# disable.satellite()

## Syntax:
`function void disable.satellite( const string session.code )`

## Description
This disables the specified satellite. The TAB on which the satellite is shown will become disabled. When this TAB is currently active, another TAB will be selected. Initially all satellite TAB buttons are enabled.
This function is relevant in multi-main table controller sessions only.

## Arguments
| | | |
|---|---|---|
| `const string` | `session.code` |  The index identifier. If this is 0, the field is not associated with any index. It is always a view field.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Notes  Use the function [enable.satellite()](enable.satellite.md) to enable a satellite TAB which was disabled.
The focus will change to the first enabled satellite as defined by WorkTop. To avoid this behavior, enable satellites before disable satellites. Change the focus with [to.satellite()](to.satellite.md)

## Example
```

			|Disable satellite
			disable.satellite("tssoc2110m000")
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
