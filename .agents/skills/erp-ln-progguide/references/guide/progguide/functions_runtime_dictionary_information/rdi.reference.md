# rdi.reference()

## Syntax:
`function long rdi.reference( string column_name(18), ref string ref_column(18), ref long ref_mode, ref string ref_mess(), [ ref boolean check_by_db, ref long ref_update_mode, ref long ref_delete_mode ] )`

## Description
If a database column references a column in another table, use this function to retrieve information about the referenced column.

## Arguments
| | | |
|---|---|---|
| `string` | `column_name(18)` |  The name of the column which references the column about which you want to retrieve information.  |
| `ref string` | `ref_column(18)` |  This returns the name of the column to which the column specified in *column_name* refers.  |
| `ref long` | `ref_mode` |  This returns the relation type. Possible values are: 1 mandatory 2 mandatory unless empty 3 not mandatory  |
| `ref string` | `ref_mess()` |  This returns the error message of the referenced column.  |
| `[ ref boolean` | `check_by_db ]` |  This indicates whether or not a referential integrity check is performed by the database driver. Possible values are: false check ignored true check performed by database driver  |
| `[ ref long` | `ref_update_mode ]` |  This returns the action to be done by the system, if an occurrence in the table referred to (= parent table) is updated. Possible values are: DB.REF.RESTRICTED DB.REF.CASCADE DB.REF.NULLIFY DB.REF.CHK.RUNTIME DB.REF.NOP  |
| `[ ref long` | `ref_delete_mode ]` |  This returns the action to be done by the system, if an occurrence in the table referred to (= parent table) is deleted. Possible values are: DB.REF.RESTRICTED DB.REF.CASCADE DB.REF.NULLIFY DB.REF.CHK.RUNTIME DB.REF.NOP  |

## Return values
0 success
-1 error

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
