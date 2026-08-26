# display.fld()

## Syntax:
`function void display.fld( long occurrence, string field )`

## Description
Use this function to display a specified field of a specific occurrence on a form. Usually, the 4GL engine displays fields automatically, either when the form is opened or when data in a related input field is changed. However, there are situations when you need to use these functions to display fields. For example, to display stand-alone fields, to display fields that are not in the input field TAB sequence, or to send data to the form during batch processes.
| | |
|---|---|
| display.fld() |  Displays a specified field of a specified occurrence. To display a field for all occurrences, use the following construction: for i= 1 to filled.occ display.fld( i, field ) endfor  |

## Arguments
```

	display.fld( actual.occ, "pctstqqq.item" )
```
| | | |
|---|---|---|
| `long` | `occurrence` |  The occurrence for which the field(s) are to be displayed. You can use the predefined variable *actual.occ* here. This always contains the number of the current occurrence.  |
| `string` | `field` |  Indicates the field to be displayed. This can be the field number or a string containing the field name. For example:  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## See also
[display()](display.md), [display.all()](display.all.md), [display.curr.occ()](display.curr.occ.md), [display.occ()](display.occ.md)
Notes  This function always display the current value of the specified field.
The current field pointer and form status are always saved when a display function is called and then restored when the function has terminated.
Non-database fields must be declared as extern in the program script.
The functions *display.fld()*, *display.occ()*, and *display.curr.occ()* are valid only for forms of type 2 or 3 (multioccurrence).
The functions *display.all()*, *display.occ()*, and *display.curr.occ()* do not affect stand-alone fields. To display a value for a stand-alone field use *display()* or *display.fld()*.

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
