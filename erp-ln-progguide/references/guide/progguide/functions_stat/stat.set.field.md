# stat.set.field()

## Syntax:
`function long stat.set.field( const string i.fieldname, boolean i.selectable, [ const string i.title, const string i.commandname ] )`

## Description
This function changes the type of the field to Stat. The field will be displayed as a Stat on the form.
If the field is displayed, the before.display section of the field will be called. In this section the values of the Stat should be set.

## Arguments
| | | |
|---|---|---|
| `const string` | `i.fieldname` |  The name of the field on the form.  |
| `boolean` | `i.selectable` |  Tells whether the Stat is selectable. A selectable Stat cannot have an icon status.  |
| `[ const string` | `i.title ]` |  i.title will be displayed as the title of the Stat. May be empty. If i.title is empty or not set, the short description of the command i.commandname will be used, if a i.commandname has been given. If no i.commandname is given and i.title is empty, the label defined on the form will be used.  |
| `[ const string` | `i.commandname ]` |  The name of the command that should be triggered on a click event on the Stat.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | i.fieldname was not found on the form. |
| -2 | error, i.fieldname is not of type long. |
| -3 | error, function should be called from after.form.read section. |
| -4 | i.commandname was not found on the form. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2492.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "after.form.read" section

## Related topics
- [Stat overview and synopsis](overview_and_synopsis.md)
