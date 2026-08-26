# display.curr.occ()

## Syntax:
`function void display.curr.occ( )`

## Description
Use this function to display all fields of the current occurrence on a form. Usually, the 4GL engine displays fields automatically, either when the form is opened or when data in a related input field is changed. However, there are situations when you need to use these functions to display fields. For example, to display fields that are not in the input field TAB sequence, or to send data to the form during batch processes.
| | |
|---|---|
| display.curr.occ() | Displays all fields of the current occurrence. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## See also
[display()](display.md), [display.all()](display.all.md), [display.fld()](display.fld.md), [display.occ()](display.occ.md)
Notes  This function always display the current value of the specified fields.
The current field pointer and form status are always saved when a display function is called and then restored when the function has terminated.
Non-database fields must be declared as extern in the program script.
The functions *display.fld()*, *display.occ()*, and *display.curr.occ()* are valid only for forms of type 2 or 3 (multioccurrence).
The functions *display.all()*, *display.occ()*, and *display.curr.occ()* do not affect stand-alone fields. To display a value for a stand-alone field use *display()* or *display.fld()*.

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
