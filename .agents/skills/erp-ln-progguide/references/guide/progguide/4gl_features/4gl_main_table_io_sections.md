# 4GL main table i/o sections
Note that main.table.io sections (except the *read.view* subsection) are ignored when the corresponding [Data Access Layer](../functions_dal/overview.md) hooks are programmed in a DAL script. For conversion see related topics.
You use main table i/o sections to program actions that you want to be executed when read or write actions occur on the main table. These sections are not relevant to type 4 programs, as such programs do not have a main table. Main table i/o sections consist of a main section and a subsection. The main section is always *main.table.io*. The subsection indicates when the actions must be executed.

## Main section

## main.table.io:
The subsections associated with this main section are executed either before or after input to or output from the main table. The main table for the current session is defined in the data dictionary.

## Subsections

## read.view:
The actions programmed in this subsection are executed immediately after a view action on the main table (start.set, first.view, next.view, prev.view or last.view). You can use this subsection to call [disable.commands()](../functions_form_and_form_field_operations/disable.commands.md)

## before.read:
The actions programmed in this subsection are executed immediately before each read action on the main table.

## after.read:
The actions programmed in this subsection are executed after each read action on the main table.

## before.write: and before.rewrite:
The actions programmed in this subsection are executed before each (re)write action on the main table. A write action occurs when a record is inserted. A rewrite action occurs when a record is changed.

## after.write: and after.rewrite:
The actions programmed in this subsection are executed after each (re)write action on the main table. A write action occurs when a record is inserted. A rewrite action occurs when a record is changed. You can use this subsection, for example, to write data to tables other than the main table.

## after.skip.write: and after.skip.rewrite:
The actions programmed in these subsection are executed if a (re)write action on the main table has been skipped as a result of actions programmed in the *before.(re)write* subsection. The actions are executed immediately after the skip action.

## before.delete:
The actions programmed in this subsection are executed immediately before each delete action on the main table.

## after.delete:
The actions programmed in this subsection are executed immediately after each delete action on the main table. You can use this subsection, for example, for deleting references, if this is not done automatically.

## after.skip.delete:
The actions programmed in this subsection are executed if a delete action on the main table has been skipped as a result of actions programmed in the *before.delete* subsection. The actions are executed immediately after the skip action.

## Example
```

main.table.io:
read.view:
    if strip$(pctst099.cprj) = "" then
        skip.io("")
    endif
```

## Related topics
- [Programming a UI Script overview](overview.md)

- [4GL event sections](4gl_event_sections.md)

- [Flow of 4GL engine](flow_of_standard_program.md)

- [Transition issues (BAAN IV to Infor Enterprise Server)](../functions_dal/transition_issues_baan_iv_to_baanerp.md)
