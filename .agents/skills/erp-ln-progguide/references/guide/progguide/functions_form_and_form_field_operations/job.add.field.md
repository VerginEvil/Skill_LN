# job.add.field()

## Syntax:
`function void job.add.field( string fld_name, [ long fld_element, long fld_type, string fld_descr ] )`

## Description
Save other fields in the jobdata which are not on the form. All form fields are stored in the jobdata with their values at the moment this function is called.

## Arguments
| | | |
|---|---|---|
| `string` | `fld_name` |  The name of the field to be added, this must be declared as an external variable in the script.  |
| `[ long` | `fld_element ]` |  Use this to specify a particular array element to be saved. For simple fields element can be omitted or set to 1.  |
| `[ long` | `fld_type ]` |  The database type of the field to be added to be saved. When this function is called for a field of type DB.DATE or DB.TIME a question is asked to the user whether a relative or absolute date/time value must be saved. Note: this question is skipped when: 1) external variable job.skip.date.question is true (absolute values are saved) 2) this question was answered by the user with "no to all" or "yes to all" before.  |
| `[ string` | `fld_descr ]` |  Use this to specify the description shown in the question for relative or absolute date/time.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Note  This function should only be used in the choice.create.job sections

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
