# Predefined variables
The following is a list of the predefined variables available to programmers. Variables specific to a particular function or group of functions are listed with those functions.
4 = 4GL only; R = Read-only; D = Deprecated (do not use anymore)
**
**
**
| | | | |
|---|---|---|---|
| Type | Name | Attr. | Description |
| long | actual.occ | 4R | Occurrence currently selected on form. |
| string | attr.adju(1) | 4 |   |
| long | attr.bitset.mask | 4 D | In general: bitsets are deprecated in the UI. The available values for a bitset field (see also [Enumerates overview and synopsis](../functions_enumerates/overview_and_synopsis.md)).  |
| boolean | attr.changed | 4R | Indicates if the current field has changed. |
| string | attr.conv(1) | 4 |   |
| string | attr.currency$(3) | 4R | Current currency (see [set.currencies()](../functions_currency_tables/set.currencies.md)).  |
| boolean | attr.currkey | 4R |   |
| boolean | attr.dbase | 4R |   |
| long | attr.dbmaxlen | 4R | Maximum length of database field. |
| string | attr.deflt$(512) | 4R | Default value of current field. When the [TIV](../tiv/tiv_overview.md) level is less than [2040](../tiv/tiv_2040.md), then the length of this string is 100.  |
| string | attr.descr$(60) | 4 | Description of current field. |
| long | attr.diga | 4 | Number of digits after decimal sign. For strings, this is the maximum input length.  |
| long | attr.digv | 4 | Number of digits before decimal sign. |
| long | attr.divf | 4 | Division factor. (For entering numeric values without a decimal point.)  |
| string | attr.domain$(16) | 4R | Domain of the current field. |
| string | attr.domm$(14) | 4 | Domain message code of current field. |
| long | attr.dorp | 4 |  Fill field with default or previous value:  |
|  boolean  | attr.echo | 4 D |   |
| long | attr.element | 4 | Current array index (if field is an array element).  |
| string | attr.enum.mask$(128) | 4 D |  The values available for an enumerate field. Also the enumerate values available for the [ask.enum()](../functions_enumerates/ask.enum.md) function. See also [set.enum.values.for.field()](../functions_enumerates/set.enum.values.for.field.md) function.  |
| string | attr.format.addition$(3) | 4 | Currency to be used for an amount format. Language to be used for a date format.  |
| string | attr.helpfile$(10) |  | Help file of current field. |
| string | attr.ille$(30) | 4 | Illegal characters. |
| long | attr.imax | 4R | Maximum input length. |
| long | attr.inpfld | 4R |   |
| boolean | attr.input | 4 D |   |
| string | attr.lega$(30) | 4 | Legal characters. |
| boolean | attr.mandatory | 4R | Mandatory input (true or false). |
| long | attr.maxlen | 4R | Maximum display length of current field. |
| string | attr.message$(132) |  | Message to be displayed when a field is filled after a *before.input* event.  |
| long | attr.minlen | 4 | Minimum length of current field. |
| boolean | attr.multioccur | 4R |   |
| string | attr.nowait$(30) | 4RD | Characters that start a field command. This variable is supported for backward compatibility only. In Infor Enterprise Server, field command functionality is replaced by form commands.  |
| string | attr.oformat$(30) | 4 | Output format of field. |
| long | attr.permission | 4R |  Permissions for current field:  |
| string | attr.previous$(30) | 4R | Previous value of field. |
| long | attr.rang | 4R | Compiled expression ID for *attr.rang$*.  |
| string | attr.rang$(100) | 4R | Defines a range; values are automatically checked against this range.  |
| long | attr.reallen | 4R | Real database length of field. |
| string | attr.refpath(100) | 4 | Reference path. |
| long | attr.rndm | 4 | Rounding method (see also [round()](../functions_mathematical_operations/round.md) function).  |
| long | attr.rotate | 4 | Current index in currency table (see [set.currencies()](../functions_currency_tables/set.currencies.md) function).  |
| long | attr.sttp | 4 D | Start position in current field. |
| string | attr.textfield$(17) | 4 | Name of the text field. Used by the Text Manager.  |
| string | attr.textkw1$(17) to attr.textkw4$(17) | 4 | Keywords of text. Used by the Text Manager. The output string is multibyte. |
| string | attr.textlang$(1) | 4 | Language for text editing. Used by the Text Manager.  |
| long | attr.textmaxlines | 4 | Maximum number of lines in the text editor. Used by the Text Manager.  |
| long | attr.textmode | 4 |   |
| string | attr.textopt$(25) | 4 | Name of default option for editor window options. Used by the Text Manager.  |
| boolean | attr.textstart | 4 |   |
| string | attr.textzoomsession$(18) | 4 | Session zoomed to by text editor zoom command. The default is "Display Texts" session. Used by the Text Manager.  |
| long | attr.type | 4R | Database type (DB.ENUM, DB.STRING, DB.TIME, DB.DATE, and so on)  |
| long | attr.zoomcode | 4 |  Field zoomcode. Possible values are:  |
| string | attr.zoomreturn$(18) | 4 | Name of return field of zoom session on current field.  |
| string | attr.zoomsession$(18) | 4 | Session zoomed to from field. |
| long | attr.zoomindex | 4 | Number of table-index to start session zoomed to from a field.  |
| boolean | auto.nextform | 4 D |   |
| boolean | background | R |   |
| boolean | before.update.check | 4RD |   |
| boolean | break.view | 4 | When searching for records in type 3 forms, break to next view when no records found and group fields match with old values. (true or false).  |
| long | chartgrp |  | Current chart group. |
| string | chm.name(128) | 4 | Name of the current chart. |
| string | chm.owner(14) | 4 | Owner/creator of current chart. |
| string | chm.title(128) | 4 | Description of current chart. |
| string | chm.user(14) | 4 | Name of user of current chart. |
| long | choice | 4 | Command ID of active command. |
| long | curr.key | 4R | Current key number of main table. Not available in before.program.  |
| string | curr.pacc$(8) | R | Current package combination. |
| string | dal.error.file | R | The name of the source file where the last dal.set.error.message was called. This variable can be used in the debugger. If you trace this variable, the debugger will stop when the function [dal.set.error.message(), dal.set.warning.message(), dal.set.info.message()](../functions_message_handling/dal.set.error.message.md) has been called.  |
| long | dal.error.line | R | The line number in the code where the last dal.set.error.message was called. See dal.error.file above.  |
| long | date | R | Number of days since 01-01-0001 (local time). |
| string | date$(6) | R | Current system date (DDMMYY). |
| boolean | dis.parent | 4R | Identification number of the (original) parent process. If the session is restarted due to dynamic index switching, it still points to the original parent process.  |
| boolean | dis.restarted | 4R | Indicates whether the session is restarted due to dynamic index switching (true or false).  |
| long | dynamic.index.switching | 4 |  Can be set in before.program for non-integrated sessions. Indicates the way the session should use dynamic index switching. Possible values: This functionality is deprecated. Dynamic index switching should be enabled in the session properties. If a session only enables Dynamic Index Switching in the before.program section this will not work in WebUI and LN UI.  |
| long | e | R | Error code of last file action. |
| long | error.bypass | 4 D | Indicates which database errors can be detected in your program script, see the [Database operations overview](../functions_db_operations/overview.md) for a detailed description.  |
| string | exit.val$(80) | R | String returned to the called program at the end of the process.  |
| string | fattr.currfld$(30) | 4R | Name of current field. |
| string | fattr.descr$(60) | 4 | Description of current form. |
| long | fattr.ftype | 4R | Type of current form (1, 2, 3, or 4). |
| string | fattr.helpfile$(14) | 4 | Name of help file for current form. |
| boolean | fattr.horizontal | 4R | True for horizontal occurrences. |
| boolean | fattr.init | 4R | Indicates if the form has been initialized. |
| long | fattr.nrtabs | 4R | Number of tabs on current form (dynamic forms only).  |
| long | fattr.occurnr | 4R | Number of occurrences on current form. |
| long | fattr.seqno | 4RD | Sequence number of current field in form. |
| long | fattr.toplines | 4 D | The number of lines above the multioccurrence fields (default: 3). Set in the *before.program* section.  |
| boolean | fattr.total.line | 4 | If set in *before.program* section, this indicates that a total line must be displayed in the grid (see also [display.total.fields()](../functions_form_and_form_field_operations/display.total.fields.md)). Can have the values true or false.  |
| string | filename$(16) | R | Name of most-recently accessed table. |
| long | filled.occ | 4R | Number of filled occurrences. |
| string | firstweek$(6) | R | Date of the first day in the first week of the current year.  |
| long | form.curr | 4R | Current form number. |
| long | form.next | 4R | Next form number. -1 if no next form |
| long | form.prev | 4R | Previous form number. -1 if no previous form |
| boolean | graphical.mode | 4 | Indicates whether the 3GL program runs in graphical mode (true) or in character mode (false). Default is false.  |
| boolean | ignore.first.event | 4 | Indicates whether the start command of the current session must be skipped. The start command is defined in the session data.  |
| string | job.code(32) | 4 | Name of the job. |
| string | job.device(14) | 4 | Default device used by job process. |
| long | job.device.requested | 4 | Indicates whether an output device must be specified when in job mode.  |
| boolean | job.process | 4R | Indicates if process is started by a job. |
| boolean | job.process.error | 4R | Indicates if an error occurred during the run of a job.  |
| string | job.report(15) | 4 | Report code of report to be used when in job mode.  |
| boolean | job.skip.date.question | 4 | Indicates if the question "Consider the difference between entered date and system date?" must be skipped.  |
| boolean | job.change.data | 4R |  Indicates if the session has been started by the Change Job option Available from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 1900](../tiv/tiv_1900.md)  |
| string | language$(1) | R | Current language code. |
| long | lattr.* |  | See [Report_scripts.](../report_scripts/predefined_variables.md) |
| string | logname$(8) | R | Current BAAN user name, which need not be identical to the OS user name. |
| string | main.table$(9) | 4R | Name of current main table. |
| boolean | mark.table() | 4R |  This array indicates which occurences are marked. The size of this array is set to *fattr.occurnr*. For example, if records 3 and 8 are marked, then: mark.table(3) = true mark.table(8) = true and other elements in the array are false. *Note that from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 1075](../tiv/tiv_1075.md) records outside the current window can be selected as well. These are not indicated as selected in the mark.table array. Read the [Record selection Overview](../functions_selection/overview.md) for more information.*  |
| long | marked | 4R |  Indicates the marked record. If multiple records are marked then this indicates the first one marked. Deprecated from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 1075](../tiv/tiv_1075.md).  |
| long | max.formtabs | 4 D | Defines the maximum number of form tabs to be displayed. Set in the *before.program* section.  |
| double | maxdouble | R | Maximum value of a double. |
| boolean | modify.prim.key | 4 |   |
| long | number.forms | 4R | Number of forms within current session. |
| long | number.of.marks | 4R |  Number of selected records in the grid. Note that from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 1075](../tiv/tiv_1075.md) you can also use [sel.num.selected()](../functions_selection/sel.num.selected.md)  |
| long | parent | R | Identification number of parent process. |
| long | pid | R | Identification number of current process. |
| long | previous.choice | 4R |  Possible values:  |
| string | procesinfo$(200) |  | Information passed to program at startup. |
| string | prog.name$(16) | R | Name of current session. |
| string | query.extension(512) | 4 D | A condition that is added to the WHERE clause of a query to be parsed by the 4GL engine (using AND operator). Set in *before.program* section. In preference, use the *query.extend* functions.  |
| string | report$ | 4 | Current report code. |
| long | reportgrp | 4 | Current report group. |
| long | reportno | R |  Reports are numbered (1..n) within a report group. This number indicates the *sequence number* within the report group. Note: The numbers (labeled "No.") in the session "Reports by Session" only match with reportno if these numbers are consecutive.  |
| string | sattr.descr$(80) | 4R | Description of the session. |
| boolean | select.only.fields.on.form |  |   |
| long | session.zoomindex | 4 | Number of table-index to start session started with start.session or start.synchronized.child.  |
| long | session.nr.view.fields | 4 | Dynamic index switching sessions only: number of view fields to show in started session started with start.session or start.synchronized.child. Use this in combination with session.zoomindex.  |
| long | session.current.index | R | The current index of the session (as selected in View/Sort by) this can differ from curr.key were curr.key is the current index of the main table that can temporary switch to an alternative index. Not available in before.program  |
| long | shell.type | R | Exec_perm from user file. |
|  | spool.* |  | See [spool.open()](../functions_spooling/spool.open.md).  |
| boolean | start.by.wfc | 4R | Session was started by workflow. |
| boolean | ssi.import.running | 4R | Boolean indicating if an Import from Excel is currently running. Questions and dialogs during Import from Excel cause a session to hang. Use this variable to check whether a question or a dialog must be skipped.  |
| boolean | ssi.export.running | 4R | Boolean indicating if an Export to Excel is currently running. |
| boolean | stp.abort.error | 4R | Boolean indicating if the function [abort.io()](../functions_db_operations/abort.io.md) has been called.  |
| boolean | stp.check.input.error | 4RD |  Boolean indicating if the function [set.input.error()](../functions_message_handling/set.input.error.md) has been called. Valid only in *check.input* section.  |
| boolean | stp.skip.error | 4R | Boolean indicating if the function [skip.io()](../functions_db_operations/skip.io.md) has been called.  |
| boolean | subdal | 4R | Indicates if the invocation of this [Data Access Layer](../functions_dal/overview.md) was caused by another DAL. Note that subdal is true does not necessarily mean that its table is a child table of the invoking DAL's table.  |
| long | synchronized.reason | 4R | This indicates the command that started the dialog synchronization. In case of MMT the satelites react on the synchronized reason of the parent to startup in the same mode ()including dis/enabling commands)  |
|  |  |  |   |
| long | update.status | 4R |   |
| boolean | text.updated.in.edit | 4R | Boolean indicating that the text is updated during the edit |
| string | user.locale$(14) | R | Locale from user file. |
| long | user.timer | R | Timer from user file. |
| string | user.type$(1) | 4R |  Current type of user. Possible values are: S super user N normal user  |
| long | win.* | 4R | See [get.window.attrs()](../functions_char_b_win/get.window.attrs.md).  |
| string | zoomfield$(18) | 4R | Variable set in the zoom session, indicating which field in the parent session was zoomed from.  |
| string | zoomreturn$(18) | 4R | Variable set in the zoom session, indicating which field's value is to be returned. In the parent session, the variable *attr.zoomreturn$* has the same value.  |
