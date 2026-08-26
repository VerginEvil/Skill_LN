# get.field.label()

## Syntax:
`function long get.field.label( const string fname, long element, ref string label1 to label3 )`

## Description
This retrieves the label text associated with the specified field. The function is relevant to dynamic forms only.
*NOTE:* For historical reasons this function sometimes returns the *initial* label, and sometimes the *current* label (as changed using [change.field.label()](change.field.label.md)). The initial label is returned for grid fields, and the current label is returned for non-grid-fields. Therefore this function is deprecated. Please use [get.initial.field.label()](get.initial.field.label.md) or [get.current.field.label()](get.current.field.label.md) instead.

## Arguments
| | | |
|---|---|---|
| `const string` | `fname` |  The field name.  |
| `long` | `element` |  For an array field, use this to specify the array element for which you wish to retrieve the label.  |
| `ref string` | `label1 to label3` |  A field can have up to three labels. These return the text of the first, second, and third labels respectively (if they exist).  |

## Return values
&0 label of field found
-1 session is not dynamic
-2 field not found

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
```

group.1:
before.group:
           form.hcur = attr.currency$
           lines = get.field.label("tfacp200.amth", 1, label1, label2, label3 )
        | if tfacp200.amth is shown in a grid, this retrieves the initial field label
        | if it is shown outside a grid, this retrieves the current field label.
           newlabel = label1 & " [" &form.hcur & "]"
           change.field.label("tfacp200.amth", 1, newlabel )
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
