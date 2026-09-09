# dialog.add.listbox()

## Syntax:
`#include <bic_dialog>`
`function long dialog.add.listbox( long dlg, const string fldName(), const string fldLabel(), const long no.items, long enum.vals(), string enum.desc(,), [ string attribute, value,... ] )`

## Description
This function creates a dynamic list box (not representing an enum domain) on the dialog. If there is an enum domain, use the function [dialog.add.field()](dialog.add.field.md).

## Arguments
| | | |
|---|---|---|
| `long` | `dlg` |  The identifier of the dialog. The identifier must be created with the function [dialog.new()](dialog.new.md).  |
| `const string` | `fldName()` |  Name of the field. This field must be declared as an extern long in the script. In case of a drop-down combo box (see possible attributes of last argument) this field must be declared as an extern string in the script instead.  |
| `const string` | `fldLabel()` |  The label used for the field.  |
| `const long` | `no.items` |  Number of items in the arrays enum.vals and enum.desc.  |
| `long` | `enum.vals()` |  Array of longs, representing the return values.  |
| `string` | `enum.desc(,)` |  Array of strings, representing the descriptions of the list items.  |
| `[ string` | `attribute, value,... ]` |  Possible attributes are: DLG_FIELD_SIZE: see [dialog.add.field()](dialog.add.field.md) DLG_MANDATORY: see [dialog.add.field()](dialog.add.field.md) DLG_FIELD_TYPE: Create a drop-down combo box (DLG_TYPE_COMBOBOX), in stead of the default drop-down list box (DLG_TYPE_LISTBOX).  |

## Return values
None.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [dialog.add.field()](dialog.add.field.md)

- [Programmable dialogs synopsis](synopsis.md)

- [Programmable Dialogs Example](example.md)
