# Starting a browse list session
In order to understand how to start browse list sessions from the application directly, it is good to see how the [4GL engine](../glossary/glossary.md#fourgl_engine) does this.

## Using the 4GL engine
The [4GL engine](../glossary/glossary.md#fourgl_engine) uses the following predefined variables while starting a browse list session:
| | |
|---|---|
| Variable | Description |
| attr.zoomcode | Defines whether a session or a menu should be started. Possible values: 0, Z.MENU, Z.SESSION |
| attr.zoomreturn$ | Name of the field of the browse list session to return. In case an index is specified all fields of this index are returned. |
| attr.zoomsession$ | Name of the session or menu to start. |
| attr.zoomindex | The index to start the browse list session with. |
Based on these variables the [4GL engine](../glossary/glossary.md#fourgl_engine) basically performs the following:
Parent session:
```

    <attr.* variables get their values from corresponding DFE properties>
    <call before.zoom section>
    | attr.* variables may have changed by application

    if attr.zoomcode = 0 or do.input.again then
        return
    endif

    value.after = start.session(
        MODAL,                       | MODAL for browse lists
        attr.zoomsession$,           | session to start
        fattr.currfld$,              | current field name
        attr.zoomreturn$             | the return field
    )
    if not isspace(value.after) then
        | A value is selected
        put.indexed.var(
            pid,
            fattr.currfld$,
            val.after,
            attr.element
        )
    endif

    <call after.zoom section>
```
Note: Here you can see that the [4GL engine](../glossary/glossary.md#fourgl_engine) is not able to handle the situation where a complete index should be returned. Function *start.session()* will return e.g. "tccom100._index2" and this value is stored in the current field. The application has to correct this in the *after.zoom* section. See [Exporting variables](browsing_exporting.md) for more information.
Browse list session:
When the browse list session starts the [4GL engine](../glossary/glossary.md#fourgl_engine) imports the *attr.zoomindex* variable. Based on that variable values, the session starts up with the correct key.

## Using start.session directly
Based on how the [4GL engine](../glossary/glossary.md#fourgl_engine) starts a browse session, the application can do this generally as follows:
Parent session:
```

field.ppmmm999.bpid:
before.zoom:
        tccom100.prbp = ppmmm999.prbp
        tccom100.bpid = ppmmm999.bpid
        session.zoomindex = 2
        exit.val$ = start.session(        | exit.val$ is a predefined 4gl var
                MODAL,                    | start as browse list
                "tccom4500m000",          | the session code
                prog.name$,               | just a default value
                "tccom100._index2"        | fields to return
        )
        if not isspace(exit.val$) then
                ppmmm999.prbp = tccom100.prbp
                ppmmm999.bpid = tccom100.bpid
        endif
        input.again()                     | Skip automatic zoom
```
For purposes of re-use this part can be implemented in a separate DLL:
Parent session:
```

field.ppmmm999.bpid:
before.zoom:
        tccom.dll4500.browse.bus.partners.by.parent(
                ppmmm999.prbp,
                ppmmm999.bpid
        )
        input.again()
```
tccom DLL:
```

        table   ttcom100

        string  ret$

function extern void tccom.dll4500.browse.bus.partners.by.parent(
ref     domain  tccom.bpid      io.parent,
ref     domain  tccom.bpid      io.bus.partner
)
{
        tccom100.prbp = io.parent
        tccom100.bpid = io.bus.partner
        session.zoomindex = 2
        ret$ = start.session(
                MODAL,
                "tccom4500m000",
                prog.name$,
                "tccom100._index2"
        )
        if not isspace(ret$) then
                io.parent = tccom100.prbp
                io.bus.partner = tccom100.bpid
        endif
}
```
Notes on the zoomname argument of start.session():

- This argument should not be an empty string, otherwise the browse list session will not call the *zoom.from.** sections, nor will it export the return field(s) when the browse list session ends.

- You can also pass *fattr.currfld$* as the zoomname argument of *start.session()*, but then you should use *attr.zoomindex* instead of *session.zoomindex*, like this:It is recommended to pass *prog.name$* by default.
```

        attr.zoomindex = 2
        ret$ = start.session(
                MODAL,
                "tccom4500m000",
                fattr.currfld$,
                "tccom100._index2"
        )
```

## Related topics
- [Definition](browsing_definition.md)

- [Overview of browsing](browsing_overview.md)

- [Importing variables](browsing_importing.md)

- [Exporting variables](browsing_exporting.md)

- [Predefined variables](../misc/predefined_variables.md)

- [start.session()](../functions_starting_and_stopping_programs/start.session.md)
