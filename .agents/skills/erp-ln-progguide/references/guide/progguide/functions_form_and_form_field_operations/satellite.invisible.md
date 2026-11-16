# satellite.invisible()

## Syntax:
`function void satellite.invisible( const string session.code )`

## Description
This hides the specified satellite. This function can only be used in section: *after.form.read*.
This function is relevant in multi-main table controller sessions only.

## Arguments
| | | |
|---|---|---|
| `const string` | `session.code` |    |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Notes  Use the function [disable.satellite()](disable.satellite.md) to temporary disable a satellite TAB.

## Example
```

|Hide satellite
after.form.read:
    satellite.invisible("tssoc2110m000")
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
