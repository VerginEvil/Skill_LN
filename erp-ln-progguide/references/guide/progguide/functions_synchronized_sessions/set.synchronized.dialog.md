# set.synchronized.dialog()

## Syntax:
`function void set.synchronized.dialog( string sess_code, [ boolean editable.grid, boolean use.dialog.for.insert ] )`

## Description
This defines for the current session the dialog to synchronize with. Both sessions act on the same maintable.
When the user double-clicks on an occurrence in the parent session, the synchronized dialog is updated with information from the selected record. The synchronized dialog also automatically opens when the user initiates any of the following actions: insert record, edit record or duplicate record. When a record is saved in the synchronized dialog, the [4GL engine](../glossary/glossary.md#fourgl_engine) updates the occurrence in the parent window.
When the synchronized dialog is opened or updated, the *synchronized.reason* variable (read-only) is set. This indicates the command that caused the synchronization. The possible values are: ADD.SET, DUPL.OCCUR, MODIFY.SET, and DISPLAY.SET. This variable is available in all sections in the synchronized dialog session.

## Arguments
| | | |
|---|---|---|
| `string` | `sess_code` |  The session code of the single-occurrence dialog session.  |
| `[ boolean` | `editable.grid ]` |  Specifies whether or not this parent session should allow an editable grid. The default is `false`. This parameter is irrelevant in case this parent session is a MMT controller.  |
| `[ boolean` | `use.dialog.for.insert ]` |  Specifies whether or not the dialog should be started for inserting or duplicating records. The default is `false`.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

- If this function is used, then, by default, the overview session will automatically become read-only.

- If you want to combine a synchronized dialog with an editable grid, then you must set the `editable.grid` argument to `true`.

- As of [TIV 1000](../tiv/tiv_1000.md), by default, an insert or duplicate in an editable grid or MMT controller session with a synchronized dialog will *not* start the dialog. This can be overridden by specifying `true` for the `use.dialog.for.insert` argument.

- Preferably fill the 'Synchronized Dialog' property of the session, use this function only when the synchronized dialog is conditionally.

## Context
4GL library function.
You call the function in the *before.program* section of the multioccurrence parent session.

## Related topics
- [Synchronized sessions overview](overview.md)

- [Synchronized sessions synopsis](synopsis.md)

- [Child synchronization sample program](example.md)
