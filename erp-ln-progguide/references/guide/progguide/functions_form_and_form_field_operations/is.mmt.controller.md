# is.mmt.controller()

## Syntax:
`function boolean is.mmt.controller( )`

## Description
This function checks whether the current session is running as a multi-main table controller session or not. This function can be useful when a session can be run in standalone mode or as a controller within a multi-main table session.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.

## Example
```

|Check whether running as MMT controller session
    if is.mmt.controller() then
        ....
    endif
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
