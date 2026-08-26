# bind.image()

## Syntax:
`function boolean bind.image( string fieldname, string guidField, [ string tablename ] )`

## Description
This function is used bind an image form field to the (table) field which holds the application GUID value. This function must be called from the *after.form.read* section or from the *before.display.object* section in the application UI script.

## Arguments
| | | |
|---|---|---|
| `string` | `fieldname` |  The name of the image field on the form. This field must be declared as an external field of domain: *ttdyf.picture*.  |
| `string` | `guidField` |  The name of the field which will hold the GUID value used to link an image set to the application table. Usually this is a field in the current maintable.  |
| `[ string` | `tablename ]` |  Optional argument in which the name of the table to which this image is linked is passed. The default value is the current maintable.  |

## Return values
| | |
|---|---|
| true | When successful |
| false | When an error occurred |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Note  In case the image is bound to a table field, you must bind the table as well to ensure that the image is read from the right company in case table sharing is applied.

## Related topics
- [Images on Forms Overview](overview.md)
- [Images on Forms synopsis](synopsis.md)
- [Images on Forms Examples](examples.md)
