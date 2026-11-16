# to.form()

## Syntax:
`function void to.form( long form_number )`

## Description
This forces a switch from the current form to the specified form. The *form_number* argument must specify an existing form in the session, and must be in the range one to the value of the predefined variable *number.forms*. During the switch operation, the [4GL form sections](../4gl_features/4gl_form_sections.md) subsection of the current form is executed and the [4GL form sections](../4gl_features/4gl_form_sections.md) and [4GL form sections](../4gl_features/4gl_form_sections.md) subsections of the new form are executed. The *init.form* subsection is executed only the first time a form becomes current.
The following predefined variables are relevant to this function:
| | |
|---|---|
| number.forms | indicates the total number of forms in the session |
| form.prev | indicates the previous form number |
| form.curr | indicates the current form number |
| form.next | indicates the next form number |

## Arguments
| | | |
|---|---|---|
| `long` | `form_number` |    |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  In a well-designed GUI, users (and not the application) select and initiate the actions to be performed. Using *to.form()* removes control from the user. Therefore it does not conform to good GUI design principles.
This function is not relevant for dynamic forms.

## Example
```

| Suppose there is a special form (form 4) for a form command.
| When the user chooses this command, form 4 is started.

declaration:
        long old_curr_form

function extern my.form.command()
{
        old_curr_form = form.curr
        to.form( 4 )
. . .   | perform some action(s)
        to.form( old_curr_form )
}
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
