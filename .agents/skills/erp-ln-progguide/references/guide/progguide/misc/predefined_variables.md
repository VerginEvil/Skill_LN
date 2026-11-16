# Predefined variables
The following is a list of the predefined variables available to programmers. Variables specific to a particular function or group of functions are listed with those functions.
4 = 4GL only; R = Read-only; D = Deprecated (do not use anymore)
| | |
|---|---|
| "l" | align left |
| "r" | align right |
| "c" | align center |
| | |
|---|---|
| "u" | convert to upper case |
| "l" | convert to lower case |
| | |
|---|---|
| true | current field is a key field |
| false | current field is not a key field |
| | |
|---|---|
| true | current field is a database field |
| false | current field is not a database field |
| | |
|---|---|
| DORP.PREVIOUS (0) | use the previous value |
| DORP.DEFAULT (1) | use the default value |
| | |
|---|---|
| true | display value on form |
| false | do not display value on form |
This variable is supported for backward compatibility only. In preference, use the [inputfield.visible()](../functions_form_and_form_field_operations/inputfield.visible.md), [inputfield.invisible()](../functions_form_and_form_field_operations/inputfield.invisible.md) and [inputfield.password()](../functions_form_and_form_field_operations/inputfield.password.md) functions.
| | |
|---|---|
| 0 | display field |
| 1 | input field |
| 2 | input only field |
| 3 | display only field |
| | |
|---|---|
| false | input disabled |
| true | input enabled |
This variable is supported for backward compatibility only. In preference, use [disable.fields()](../functions_form_and_form_field_operations/disable.fields.md) and [enable.fields()](../functions_form_and_form_field_operations/enable.fields.md) functions.
| | |
|---|---|
| true | multioccurrence field |
| false | not multioccurrence field |
| | |
|---|---|
| NO.PERMISSION | 1 |
| PERM.READ | 2 |
| PERM.MODIFY | 4 |
| PERM.WRITE | 8 |
| PERM.DELETE | 16 |
| NO.RESTRICTION | 30 |
| PERM.UNKNOWN | 32 |
| NO.PERM.DEFINED | 64 |
See also [db.permission()](../functions_db_operations/db.permission.md) function.
| | |
|---|---|
| 1 | display mode |
| 3 | read/write mode |
Used by the Text Manager.
| | |
|---|---|
| true | When new text is created, start text manager directly (default). |
| false | When new text is created, fill keywords first. |
Used by the Text Manager.
| | |
|---|---|
| 0 | No zoom |
| Z.MENU (1) | Zoom to a menu |
| Z.SESSION (2) | Zoom to a session |
| | |
|---|---|
| true | When modifying form data, automatically display next form when all occurrences on current form have been filled. |
| false | When modifying form data, do not automatically display next form when all occurrences on current form have been filled (default). |
It is not good GUI practice to use this variable.
| | |
|---|---|
| true | current session is modal |
| false | current session is modeless |
| | |
|---|---|
| true | field is checked during update |
| false | field is checked during input |
Valid only in subsection *check.input*.
| | | |
|---|---|---|
| 0 | No dynamic index switching. |  |
| -1 | Restart when view fields differ. |  |
| -2 | Always restart session when switching indices. |  |
| | |
|---|---|
| true | Primary key can be modified during modify. Set in programs of type 1, 2, and 3. |
| false | Primary key cannot be modified. |
| | |
|---|---|
| 0 |  |
| add.set | dupl.occur |
| modify.set | mark.delete |
| global.copy | global.delete |
Valid only in field sections and *main.table.io*.
| | |
|---|---|
| true | all reference tables are read (default) |
| false | only reference tables of fields on form are read |
Use in *before.program* section.
| |
|---|
| 0 |
| DISPLAY.SET |
| ADD.SET |
| MODIFY.SET |
| DUPL.OCCUR |
| END.PROGRAM |
| ABORT.PROGRAM |
| | |
|---|---|
| 0 | no update |
| ADD.SET | during add |
| MODIFY.SET | during modify |
| MARK.DELETE | during delete |
