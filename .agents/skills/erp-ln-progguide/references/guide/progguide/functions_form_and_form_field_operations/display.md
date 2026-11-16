# display()

## Syntax:
`function void display( string field )`

## Description
Use this function to display a specified field on a form. Usually, the [4GL engine](../glossary/glossary.md#fourgl_engine) displays fields automatically, either when the form is opened or when data in a related input field is changed. However, there are situations when you need to use these functions to display fields. For example, to display stand-alone fields, to display fields that are not in the input field TAB sequence, or to send data to the form during batch processes.
| | |
|---|---|
| display() | Displays a single-occurrence field. You cannot use this to display a field for all occurrences. |

## Arguments
```

display( "pctstqqq.item" )
```
| | | |
|---|---|---|
| `string` | `field` |  Indicates the field to be displayed. This can be the field number or a string containing the field name. For example:  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## See also
[display.all()](display.all.md), [display.curr.occ()](display.curr.occ.md), [display.fld()](display.fld.md), [display.occ()](display.occ.md)
Notes  This function always display the current value of the specified fields.
The current field pointer and form status are always saved when a display function is called and then restored when the function has terminated.
Non-database fields must be declared as extern in the program script.
To display a specific element of a multi-element field, set the attr.element attribute to the desired element before calling *display()*.
The function *display.all()*, *display.occ()*, and *display.curr.occ()* do not affect stand-alone fields. To display a value for a stand-alone field use *display()* or *display.fld()*.

## Example using display() for multiple elements
```

function void refresh.all.elements.of.addr()
{
	long	i

	for i = 1 to 3
		attr.element = i	|* The element number to be displayed
		display("addr")	|* after display() the attr.element is reset to 1
	endfor
}
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
