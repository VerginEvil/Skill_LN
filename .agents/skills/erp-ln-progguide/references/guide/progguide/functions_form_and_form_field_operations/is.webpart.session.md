# is.webpart.session()

## Syntax:
`function boolean is.webpart.session( )`

## Description
This function checks whether the current session is running as a primary session in a Workspace WebPart. This function can be useful when a session can be run in different modes.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

|Check whether running as WebPart session
    if is.webpart.session() then
        ....
    endif
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
