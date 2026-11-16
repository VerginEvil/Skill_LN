# Flow of 4GL engine
This section presents the general flow of the [4GL engine](../glossary/glossary.md#fourgl_engine). It is not complete, but the most important actions are included. The flow is similar for programs of types 1, 2, 3, and 4. Any differences are indicated by comments.

## Main routine
The main routine displays the first form on the screen and waits for a command.
```

 function main()
    {
            before.program
            read.form()
            after.form.read
            init.references
            create.sql.queries
            if background then
                get.ref.var(parent)
                    read record
            endif
            db.bind(tmain)                | Not in type 4
            if job.process then           | Only type 4
                        before.choice.run.job
                        execute(cont.process) or on.choice.run.job
                        after.choice.run.job
                        execute(end.program)
            endif
            zoom.from.on.entry
            for each field on form
                        init.field
                        put.attributes()
            endfor
            change to start index               | Not in type 4
            init.form
            for each group on current form      | Only dynamic sessions
                        init.group
            endfor
            execute start event
            before.form
            for each group on current form      | Only dynamic sessions
                        before.group
            endfor

            while true
                input.choice()
                    if update.status and choice <> ... then   | Not in type 4
                                on.update.db()
                                        | See "update database" section
                    endif
                        on case choice
                        case <choice.option>
                            before.<choice.option>
                            on.<choice.option>
                            after.<choice.option>
                            break
                         case ...
                         ....
                     endcase
             endwhile
```

## Choice sections
The choice sections above are given as before. *choice.option* and after. *choice.option*. In a 4GL program, a choice section consists of the main section choice. *choice.option* and one of the subsections before.choice, on.choice, or after.choice.

## Field sections
There are two groups of field sections:

- init.field

- before.field

- before.input

- before.display

- before.checks

- selection.filter

- before.zoom

- check.input | if not in DAL

- on.input

- after.input

- after.display

- after.zoom

- ref.input

- ref.display

- domain.error

- when.field.changes

- after.field

The general flow of input fields is as follows:
```

Field.input:
                before.field
                if not input.field then
                        read.reference
                        if error.reference then
                                ref.display
                        else
                                before.display
                                display.field()
                                after.display
                        endif
                        return
                endif
                before.input
                if input disabled then
                        read.reference
                        if error.reference then
                                ref.display
                        else
                                before.display
                                display.field()
                                after.display
                        endif
                        return
                endif

zoom.ret:
                do.input.field()
                if in.ret = ZOOM then
            selection.filter
                        before.zoom
                        zoom.to ...
                        after.zoom
                        goto zoom.ret
                endif
                if choice = f.to.choice or
                                in.ret = arrow.up/down/left/right/tab then
                        goto after.field
                endif
                before.checks
                check.domain()

                if domain.error then
                        domain.error
                        error.message
                        goto field.input
                endif
                check.reference

                if reference.error then
                        ref.input
                        error.message
                        goto field.input
                endif
                check.input | DAL section
                if check.input.error then
                        error.message
                        goto field.input
                endif
                on.input
                ....
                ....
                when.field.changes
                after.input
                after.field
```

## End of program
The flow of the end of the program is as follows. The function *end.of.program()* is called when executing the standard command END.PROGRAM.
```

function end.of.program()
        {
                before.end.program
                if e then
                        on.error
                endif
                for each group on form                 | Only dynamic sessions
                        after.group
                endfor
                after.form
                after.program
                if zoomfield  = "" then
                        fill.zoomreturn
                        zoom.from.on.exit
                        if record.marked then
                                commit.transaction()   | Not in type 4
                                exit(exit.val)
                        endif
                endif
                commit.transaction()                   | Not in type 4
                exit()
 }
```

## Zoom.from sections
The zoom.from.on.entry and zoom.from.on.exit sections are used in the main routine and in the *end.of.program()* function. In a 4GL program, a zoom.from section consists of a main section (zoom.from.all, zoom.from.<zoomname>, or zoom.from.other) and a subsection (on.entry or on.exit).
The sequences in which the sections are executed differ for on.entry and on.exit. For on.entry, zoom.from.all is executed first and then zoom.from.<zoomname> or zoom.from.other. For on exit, it is the other way around.

## Update database
An update of the database is necessary if a record is added, changed or deleted. The actual update is executed if one of the following actions is activated after a record has been added, changed or deleted: start.set, def.find, find.data, first.set, next.set, prev.set, last.set, change.order and form commands that save data.
All these actions first call *on.update.db()* if a record is added, changed or deleted. The general flow of the *on.update.db()* is as follows. Note that this function is not relevant to programs of type 4.
```

on.update.db()
{
    if update.status = add.set or modify.set then
        for all occurrences
            check.domains()
            if domain.error then
                domain.error
                error.message
                return
            endif
            check.references
            if reference.error then
                ref.input
                error.message
                return
            endif
            for each field of occurrence
                check.input
                if check.input.error then
                    error.message
                    return
                endif
            endfor
        endfor
    endif
    before.update.db
    db.retry.point()
    for all occurrences
        before.save.object / before.destroy.object
        if not skip then
            insert / update / delete record
            after.save.object / after.destroy.object
        endif
    endfor
    back.to.old.key
    after.update.db
    commit.transaction()
    after.update.db.commit
}
```

## Main table i/o section
Most of the main table i/o are mentioned above. They are not available in programs of type 4.
The read.view section is executed immediately after any view action on the main table (only in type 3 programs). The function *skip.io("messcode")* can be used in this section. This implies that the next or previous view is read.

## Related topics
- [Programming a UI Script overview](overview.md)

- [4GL event sections](4gl_event_sections.md)
