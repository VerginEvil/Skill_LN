# text.defaults()

## Syntax:
`function long text.defaults( string text_field, ref string tgroup, ref string edit_opt, [ long comp_number ] )`

## Description
This retrieves the defaults for a specified text field.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field` |  The name of the text field. See [Text fields overview](overview.md). This returns the text number of the field.  |
| `ref string` | `tgroup` |  This returns the default text group of the text.  |
| `ref string` | `edit_opt` |  This returns the default window type for the text.  |
| `[ long` | `comp_number ]` |  This specifies the company number.  |

## Return values
0 success
-1 default textgroup not found
-2 no update permission in textgroup
-3 table does not exist in company

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Text fields overview](overview.md)
- [Text fields synopsis](synopsis.md)
