# get.screen.defaults()

## Syntax:
`function void get.screen.defaults( )`

## Description
The *save.defaults* standard command enables users to save the current field values of a session as the default values for that session. The *get.screen.defaults()* function displays the default values for all fields on all forms of the current session. It is often used at the start of update or print programs, where the user must specify some parameters before executing the session.
If no user defaults are defined, [set.fields.default()](set.fields.default.md) is executed automatically.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
```

form.1:
init.form:
    get.screen.defaults()
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
