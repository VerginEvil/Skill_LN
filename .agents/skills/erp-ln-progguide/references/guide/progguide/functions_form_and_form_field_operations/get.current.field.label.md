# get.current.field.label()

## Syntax:
`function long get.current.field.label( const string fname, long element, ref string label1 to label3 )`

## Description
This retrieves the current label text associated with the specified field. The function is relevant to dynamic forms only.
The current label can only differ from the initial label if the function [change.field.label()](change.field.label.md) has been used.

## Arguments
| | | |
|---|---|---|
| `const string` | `fname` |  The field name.  |
| `long` | `element` |  For an array field, use this to specify the array element for which you wish to retrieve the current label.  |
| `ref string` | `label1 to label3` |  A field can have up to three labels. These return the text of the first, second, and third labels respectively (if they exist).  |

## Return values
&0 label of field found
-1 session is not dynamic
-2 field not found

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [get.initial.field.label()](get.initial.field.label.md)

- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
