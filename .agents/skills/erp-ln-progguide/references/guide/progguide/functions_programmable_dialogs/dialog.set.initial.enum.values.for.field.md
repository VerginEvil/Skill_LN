# dialog.set.initial.enum.values.for.field()

## Syntax:
`function long dialog.set.initial.enum.values.for.field( long dlg, const string field.name, long ALL_ENUMS_EXCEPT, enum enum_value,... )`

## Description
This function applies to enumerated fields that are displayed as listbox or optionset. It limits the number of options to the specified set of enum constants. Any options not specified will be *hidden*.

## Arguments
| | | |
|---|---|---|
| `long` | `dlg` |  The identifier of the dialog. The identifier must be created with the function [dialog.new()](dialog.new.md).  |
| `const string` | `field.name` |  The name of the optionset field. For example, "ttadv996.type". For an array field, include the array element. For example, "tttadv996.type(5)".  |
| `long` | `ALL_ENUMS_EXCEPT` |  This optional macro specifies that the succeeding list of enumerate values represents those values that are to be *excluded* from the enumerate set. Otherwise, the list of enumerate values represents the values that are to be *included*.  |
| `enum` | `enum_value,...` |  The options to be displayed on the form, separated by commas [,]. This is an optional argument. If not included, all enumerate values (= all options) defined for the field are available.  |

## Return values
| | |
|---|---|
| 0 | Success |
| < 0 | Field not found in the dialog |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Notes  This function can only be called after the field is added to the dialog.

## Example
```

	long	dlg

	dlg = dialog.new("Example Dialog", DLG_STATUSBAR, true)
	dialog.add.field(dlg, "yeno", "Yes or No", DLG_DOMAIN, "tcyesno"))
	dialog.set.initial.enum.values.for.field(dlg, "yeno", ALL_ENUMS_EXCEPT, etol(tcyesno.yes))
```

## Related topics
- [Programmable dialogs synopsis](synopsis.md)

- [Enumerate and set constants](../3gl_features/enumerate_and_set_constants.md)
