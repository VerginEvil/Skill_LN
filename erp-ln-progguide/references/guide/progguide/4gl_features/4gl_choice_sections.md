# 4GL choice sections
You use choice sections to program actions that you want to be executed when standard commands or form commands are activated or ended. Choice sections consist of a main section and a subsection. The main section specifies the standard command or form command for which the actions must be executed. The subsections specify when the actions must be executed.

## Main section

## choice.<standard command>:
The subsections associated with this main section are executed for the specified command. You can enable standard commands and specify form commands from the session *Sessions* (ttadv2500m000). A list of standard commands appears at the end of this help topic. For form commands, the session, menu or function name is used.

## Subsections

## before.choice:
The actions programmed in this subsection are executed immediately before the specified command is executed. You can use this subsection, for example, to test data before the command process continues. You can use the [choice.again()](../functions_form_and_form_field_operations/choice.again.md) function to stop the command.

## on.choice:
The actions programmed in this subsection are executed when the specified command is activated. These actions are executed instead of the standard action associated with the command. This subsection is not always available. For details, see the list at the end of this help topic.

## after.choice:
The actions programmed in this subsection are executed immediately after the specified command has been executed. This subsection is not available for the *end.program* and *abort.program* commands.
A programmed action of choice first.view, next.view, prev.view or last.view overrules the execution of first.set

## Example
```

choice.first.view:      | standard command
after.choice:
    execute(first.set)

choice.ttadv2111m000:       | form command
before.choice:
    export_var = "some value"
```

## Standard commands
The following table lists the available standard commands and the types of program in which the various choice subsections can be programmed for each command.
| | | | | | |
|---|---|---|---|---|---|
| No | Section name *choice.* <...>  | Description | Before | On | After |
| 01 | start.set | Add/start a new group in main table | 1234 | ---4 | 1234 |
| 02 | first.view | View first group of main table | 1234 | ---4 | 1234 |
| 03 | next.view | View next group of main table | 1234 | ---4 | 1234 |
| 04 | prev.view | View previous group of main table | 1234 | ---4 | 1234 |
| 05 | last.view | View last group of main table | 1234 | ---4 | 1234 |
| 06 | def.find | Find a specific record on key | 1234 | ---4 | 1234 |
| 07 | find.data | Start the set from the current data in the program script. Use: after import of data in a zoom process. (refresh)  | 1234 | ---4 | 1234 |
| 08 | first.set | View first set of main table | 1234 | ---4 | 1234 |
| 09 | next.set | First execute an update.db and then view next set of main table  | 1234 | ---4 | 1234 |
| 10 | display.set | Open read-only details | 1234 | ---4 | 1234 |
| 11 | prev.set | First execute an update.db and then view previous set of main table  | 1234 | ---4 | 1234 |
| 12 | rotate.curr | Show amounts in other currency (on.choice subsections are available for this command only if no currencies are set)  | 1234 | 1234 | 1234 |
| 13 | last.set | View last set of main table | 1234 | ---4 | 1234 |
| 14 | add.set | Insert a new record | 1234 | ---4 | 1234 |
| 15 | update.db | First test consistency of data and then (re)write record or set (save)  | 1234 | ---4 | 1234 |
| 16 | dupl.occur | Copy the record to a new one | 1234 | ---4 | 1234 |
| 17 | recover.set | Undo modifications which are not yet written to the database | 1234 | ---4 | 1234 |
| 18 | mark.delete | Delete selected records | 1234 | ---4 | 1234 |
| 19 | mark.occur | Select a record on the screen | 1234 | ---4 | 1234 |
| 20 | change.order | Change the search key | 1234 | ---4 | 1234 |
| 21 | modify.set | Change a record stored in the database | 1234 | ---- | 1234 |
| 23 | print.data | Make a report with the current data on the form | 1234 | 1234 | 1234 |
| 24 | create.job | Add session in job | 1234 | ---- | 1234 |
| 25 | change.frm | Go to another form in session. The command mnemonic (as used by the *execute()* command is form.tab.change.  | 1234 | ---- | 1234 |
| 26 | first.frm | Go to first form | 1234 | ---- | 1234 |
| 27 | next.frm | Go to next form | 1234 | ---- | 1234 |
| 28 | prev.frm | Go to previous form | 1234 | ---- | 1234 |
| 29 | last.frm | Go to last form | 1234 | ---- | 1234 |
| 31 | resize.frm | Resize the current form | 1234 | 1234 | 1234 |
| 34 | zoom | Out dated: use form commands instead. Zoom to another session/menu | 1234 | ---- | 1234 |
| 35 | interrupt | Do an action each time interval | 1234 | 1234 | 1234 |
| 36 | end.program | End execution of the session; the main table will be updated | 1234 | ---- | ---- |
| 37 | abort.program | Cancel execution of the session. The main table is not updated  | 1234 | ---- | ---- |
| 38 | cont.process | Continue process. Supported only for running Print/Update sessions in job mode. When the session runs in job mode and this choice section is not implemented, the default form command will be executed.  | ---4 | ---4 | ---4 |
| 39 | text.manager | Start the text manager | 1234 | ---- | 1234 |
| 40 | run.job | Run job of session | 1234 | 1234 | 1234 |
| 41 | global.delete | Delete range of records | 1234 | 1234 | 1234 |
| 42 | global.copy | Copy range of records | 1234 | 1234 | 1234 |
| 43 | save.defaults | Save values as defaults | 1234 | ---- | 1234 |
| 44 | get.defaults | Get previous stored defaults | 1234 | ---- | 1234 |
| 45 | chm | Chart Manager is started. The command mnemonic (as used by the *execute()* command is start.chart.  | 1234 | ---4 | 1234 |
| 46 | start.query | Start query by form | 1234 | ---4 | 1234 |
| 47 | select.all | Select All records | -23- | ---- | -23- |
| 64 | bms | A broadcast message is received | 1234 | 1234 | 1234 |
| 91 | cmd.ssi.import | Import Records from Excel | 123- | ---- | 123- |
| 93 | cmd.ssi.export.q | Quick Export Records to Excel | 123- | ---- | 123- |
| 94 | cmd.ssi.export.a | Advanced Export Records to Excel | 123- | ---- | 123- |
| 108 | cmd.insert.in.detail | Insert record via detail session | -23- | ---- | -23- |
The following commands are supported for backward compatibility only. Support is not guaranteed in future versions of the software.
- calendar
- user.0
- user.1
- user.2
- user.3
- user.4
- user.5
- user.6
- user.7
- user.8
- user.9

## Related topics
- [Programming a UI Script overview](overview.md)
- [4GL event sections](4gl_event_sections.md)
- [Flow of 4GL engine](flow_of_standard_program.md)
