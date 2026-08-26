# disable.personalize.form()

## Syntax:
`function void disable.personalize.form( )`

## Description
This function disables the personalize form functionality for the current session.
The function can be used for a session that has a very dynamically lay-out; fields are hidden, made visible, labels changed dependent on the data displayed.
Disabling of personalize form is not supported for a session of type Print-Processing

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  If the Form Personalization is disabled it will not be possible for a user to make initially hidden fields visible. So, it does not make sense to add initially hidden fields to the form if this function is called in the script.
This function should be used in the before program section.
This function is available from TIV 2450.

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
