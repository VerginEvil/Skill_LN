# disable.save.on.occ.change()

## Syntax:
`function void disable.save.on.occ.change( )`

## Description
Use this function in a extension to disable the save on occ change in a standard session. The [enable.save.on.occ.change()](enable.save.on.occ.change.md) will force the 4GL Engine to save an occurrence at the time the user selects or moves to another occurrence.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2591.

## Example
```

function after.form.read()
{
	disable.save.on.occ.change()
}
```
Notes  Use this function only in the `after.form.read` section from an extension.
When using this function, it may conflict with other standard session logic, that rely on direct saved changes (like updating totals, data issues). It is up to the Extender to verify and test the session thoroughly.

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
