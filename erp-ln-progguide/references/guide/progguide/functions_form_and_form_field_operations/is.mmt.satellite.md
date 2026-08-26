# is.mmt.satellite()

## Syntax:
`function boolean is.mmt.satellite( )`

## Description
This function checks whether the current session is running as a multi-main table satellite session or not. This function can be useful when a session can be run in standalone mode or as a satellite within a multi-main table session.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
```

|Check whether running as satellite session
    if is.mmt.satellite() then
        ....
    endif
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
