# Exporting variables
When the browse list session ends, data of the selected record needs to be returned to the parent session. In case of automatic export, the name of the return field (or fields) can be defined by means of the predefined variable *attr.zoomreturn$*, or by filling the Return field property in DFE.

## Automatic export of a single field
If the application sets the predefined variable *attr.zoomreturns$* in the *before.zoom* sub-event, or when the Return field property in DFE is filled, the [4GL engine](../glossary/glossary.md#fourgl_engine) will automatically export the right field value to the parent session on exit of the browse list session. The [4GL engine](../glossary/glossary.md#fourgl_engine) also copies the value of the return field in the current field of the parent session.
Example:
```

field.ppmm999.bpid:
before.zoom:
        attr.zoomreturn$ = "tccom100.bpid"
after.zoom:
        |* The 4GL engine will export the value of tccom100.bpid of the
        |* browse list session to this session, stores its value in
        |* the current field (ppmmm999.bpid) and displays it.
```

## Automatic export of all key fields
It is also possible to return all fields of a key. This can be defined in DFE, but also in the script. In this situation however, the script has to copy the exported values to the right fields in the parent session.
Example:
```

field.ppmm999.bpid:
before.zoom:
        tccom100.prbp = ppmmm999.prbp
        tccom100.bpid = ppmmm999.bpid
        attr.zoomindex = 2
        attr.zoomreturn$ = "tccom100._index2"

after.zoom:
        ppmmm999.prbp = tccom100.prbp
        ppmmm999.bpid = tccom100.bpid
        display("ppmmm999.prbp") | Not automatically done
        display("ppmmm999.bpid") | Not automatically done
```
If tccom100._index2 consists of the fields tccom100.prbp and tccom100.bpid, then both fields will be exported by the [4GL engine](../glossary/glossary.md#fourgl_engine) to the parent process, just before the browse list session exits. In the *after.zoom* sub event you can assign these values to the fields of the parent session and do a display of these fields.

## No automatic export
When no return field is defined, the [4GL engine](../glossary/glossary.md#fourgl_engine) will not export anything. In this case the browse list session has to do the export itself. This can be programmed in the *zoom.from.*: on.exit:* event section. It is up to the browse list session to define what will be exported.
Example:
Parent session:
```

declaration:

extern  domain  tccom.bpid      zoom.bpid

field.ppmmm999.bpid:
before.zoom:
        zoom.bpid = ppmmm999.bpid
after.zoom:
        ppmmm999.bpid = zoom.bpid
```
browse list session:
```

declaration:

        table   ttccom100

zoom.from.all:
on.exit:
        export("zoom.bpid", tccom100.bpid)
```

## Related topics
- [Definition](browsing_definition.md)

- [Overview of browsing](browsing_overview.md)

- [Importing variables](browsing_importing.md)

- [Starting a browse list session](browsing_starting.md)
