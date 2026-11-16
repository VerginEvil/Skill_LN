# change.group.label()

## Syntax:
`function long change.group.label( const long groupId, const string label )`

## Description
Use this to set the label for a specified group. The new label replace the current label. The function requires that the specified group already has a (dummy) label in the form-definition.
This function may be used for dynamic sessions only!
This function may not be used in the before.program section.
It is recommended to use this function in the after.form.read.section.
The label is not read after the session is visible.

## Arguments
| | | |
|---|---|---|
| `const long` | `groupId` |  The Id of the group whose label must be set.  |
| `const string` | `label` |  The new label text.  |

## Return values
0 success
-1 session is not dynamic
-2 group not found

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
