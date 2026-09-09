# text.window()

## Syntax:
`function long text.window( string edit_opt, ref long start_column, ref long start_row, ref long number_columns, ref long number_rows )`

## Description
This returns information about a specified window type.

## Arguments
| | | |
|---|---|---|
| `string` | `edit_opt` |  The name of the window type.  |
| `ref long` | `start_column` |  This returns the number of the column where the  |
| `ref long` | `start_row` |  This returns the number of the row where the window  |
| `ref long` | `number_columns` |  This returns the number of rows in the window.  |
| `ref long` | `number_rows` |  This returns the number of rows in the window.  |

## Return values
0 success
-1 error; *edit_opt* not found

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Text fields overview](overview.md)

- [Text fields synopsis](synopsis.md)
