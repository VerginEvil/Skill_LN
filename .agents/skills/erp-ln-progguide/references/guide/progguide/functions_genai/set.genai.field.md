# set.genai.field()

## Syntax:
`function void set.genai.field( const string i.form.field )`

## Description
Tells that the field must shown GenAI processing animation if GenAI processing is busy.

## Arguments
| | | |
|---|---|---|
| `const string` | `i.form.field` |  Name of the field.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Failure, unknown field. Field is not part of the session. |
| -2 | Failure, field is not of type Text. Only Text fields are currently supported. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2590.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "after.form.read" section

## Related topics
- [GenAI Functionality on Form](overview_and_synopsis.md)
