# enable.save.on.occ.change()

## Syntax:
`function void enable.save.on.occ.change( )`

## Description
Use this function to force the 4GL Engine to save an occurrence at the time the user selects or moves to another occurrence. Any unsaved changes to the occurrence, will be automatically saved. I.e. the UPDATE.DB choice is executed and the 4GL engine will continue in the previous mode (MODIFY.SET or ADD.SET).

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Notes  Use this function only in the `after.form.read` section.

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
