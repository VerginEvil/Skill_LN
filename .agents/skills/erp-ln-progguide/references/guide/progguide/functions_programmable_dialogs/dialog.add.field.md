# dialog.add.field()

## Syntax:
`#include <bic_dialog>`
`function long dialog.add.field( long dlg, const string fldName(), const string fldLabel(), [ long attribute, value,... ] )`

## Description
This function creates a new field on the dialog.

## Arguments
| | | |
|---|---|---|
| `long` | `dlg` |  The identifier of the dialog. The identifier must be created with the function [dialog.new()](dialog.new.md).  |
| `const string` | `fldName()` |  Name of the field. Preferably, there should also be a variable declared as extern in the script with the same name. The value of the dialog field will then be set in this variable. If such a variable does not exist, the attribute DLG_FIELD_DYNAMIC should be set to *true* and it will be created at runtime. Then, the value can be accessed with the function [get.var()](../functions_variables_interprocess_transfer/get.var.md).  |
| `const string` | `fldLabel()` |  The label used for the field.  |
| `[ long` | `attribute, value,... ]` |  Use these optional arguments to set the dialog field's attributes. For each attribute you specify, you must include the attribute type (for example, DLG_DOMAIN or DLG_MANDATORY), and the attribute value.  |

## Return values
| | |
|---|---|
| 0 | Success |
| < 0 | The negative sequence number of the erroneous argument. E.g. a return value of -7 indicates an error in the 7th argument. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Attributes
| | | |
|---|---|---|
| Attribute | Type | Description |
| DLG_FORM_FIELD | String | Copy the properties of the specified form field. Only possible in UI-script of a session |
| DLG_DOMAIN | String | Copy the properties of the specified domain. Properties are: Database type Alignment (strings) Upper/lower case conversion Size |
| DLG_FIELD_TYPE | Long | DLG_TYPE_STRINGDLG_TYPE_LONG,DLG_TYPE_MULTI_LINE,DLG_TYPE_MB,DLG_TYPE_DATE,DLG_TYPE_UTC,DLG_TYPE_CHECKBOX,DLG_TYPE_LISTBOX orDLG_TYPE_PASSWORD.Only checkbox and password are really necessary. Others can be derived from the variable type or domain. |
| DLG_ALIGNMENT | Long | RDI.LEFT, RDI.RIGHT, RDI.CENTER or RDI.NONE for left, right, center and no alignment. |
| DLG_CASE_CONVERT | Long | RDI.UPPER, RDI.LOWER or RDI.NONE for uppercase, lowercase and no conversion. |
| DLG_FIELD_DYNAMIC | Long | If set to true, the variable indicated by *fldName* need not exist. It will be created at runtime. The value of the variable can be access with the function [get.var()](../functions_variables_interprocess_transfer/get.var.md). |
| DLG_FIELD_SIZE | Long | Number of characters that can be entered in the field (input length). Default is taken from the domain info or variable info (string). This property is not needed in normal circumstances. |
| DLG_FIELD_WIDTH | Long | Width of the field in characters (display length). Default is the size of the string. |
| DLG_FIELD_HEIGHT | Long | Height of the multi-line edit box in lines. Default is 3 |
| DLG_MANDATORY | Long | Mandatory enum: no empty selection possible |
| DLG_ZOOM_PROG | String | Session code for browsing. If the string starts with an "@", the value refers to a function to be called instead of a zoom session. The function should be in the same object as the dialog.new function. |
| DLG_ZOOM_RETURN | String | Name of field to be returned from browse session |
| DLG_ZOOM_FROM | String | Name of field where the zoom was started from (used for zoom.from section in the called session) |
| DLG_FIELD_CHECK | String | Name of the function that checks the input of the field. This function should return false if the input is incorrect. |
| DLG_RANGE_FIELD | String | Name of the second variable in a range. This second field will have the same properties as the original field. |
| DLG_FIELD_STATE | Long | The state of the field: ENABLED(default), READONLY or DISABLED. |
| DLG_DESC | String | Description field. The value should be set in the function that checks the value of the input field (see DLG_FIELD_CHECK) |
| DLG_HELPCODE | String | The code to by used by the help system. Normally, the code of the corresponding table field is entered here. If this argument is skipped, the *fieldName* will be taken. |

## Related topics
- [Programmable dialogs synopsis](synopsis.md)

- [Programmable Dialogs Example](example.md)
