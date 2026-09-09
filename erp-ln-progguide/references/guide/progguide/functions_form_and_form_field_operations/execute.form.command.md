# execute.form.command()

## Syntax:
`function void execute.form.command( const string form.command )`

## Description
This executes the specified form command. This function also executes the before/after command hooks in the extension (if defined).

## Arguments
| | | |
|---|---|---|
| `const string` | `form.command` |  The form command to be executed.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2391.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
