# set.fields.default()

## Syntax:
`function void set.fields.default( )`

## Description
It is possible to define default values for form fields with the form editor. For all fields of the current form, this function sets the corresponding script variables to the default form values.
The function is often used before batch or print programs, where the user must specify some parameters for the batch run.

## Context
This function is implemented in the porting set and can be used in all script types.

## See also
[get.screen.defaults()](get.screen.defaults.md)

## Example
```

form.1:
init.form:
  set.fields.default()
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
