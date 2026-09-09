# change.field.label()

## Syntax:
`function long change.field.label( const string fname, long element, const string label1, [ const string label2, const string label3 ] )`

## Description
Use this to set the label for a specified field. A field can have up to three lines of text (label-lines). The new label-line(s) replace the current label-line(s). The function requires that the specified field already has a (dummy) label in the form-definition. When the field is not in the grid, the label in the form-definition should have at least the same number of label-lines, as specified with this function.
This function is may be used for dynamic sessions only!
This function may not be used in the before.program section.

## Arguments
| | | |
|---|---|---|
| `const string` | `fname` |  The name of the field whose label must be set.  |
| `long` | `element` |  For an array field, use this to specify the array element for which you want to set the label. For multi-currency fields the element number must be -1.  |
| `const string` | `label1` |  The first (top) label-line.  |
| `[ const string` | `label2 ]` |  The second label-line. (optional)  |
| `[ const string` | `label3 ]` |  The third label-line. (optional)  |

## Return values
0 success
-1 session is not dynamic
-2 field not found

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Note  The old label determines default the space reserved for the label. However when the function is called from after.form.read, space for the new label is reserved. When the new text is not known yet in after.form.read, change.field.label() can be used to set a dummy text, just for reservation of space for the label.
```

after.form.read:
change.field.label("ttadv200.cpac",1,"01234567890123456789")
     | Now 20 characters will be reserved for the label of
     | the specified field, later the new value can be set.
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
