# Importing variables
The browse list session needs to import one or more variables from the parent session. Based on the imported values, the browse list session reads records from the maintable and displays them.

## Automatic import
The [4GL engine](../glossary/glossary.md#fourgl_engine) automatically imports variables (i.e. the primary key values). This happens in the following 5 situations:

## 1. Table reference exists from parent field to main table of child session

## Situation
A browse list session with main table Y is started from a parent session with main table X. Table X has a reference (foreign key) to table Y.

## Result
The [4GL engine](../glossary/glossary.md#fourgl_engine) imports the browse field(s) from table X and stores them in the primary key fields of table Y.

## Consequences for programming in UI script
None

## Example
The Currency field in the Business Partner table refers to the Currency table.
When the Currencies browse session is started by browsing from the Currency field on the Business Partner session, the [4GL engine](../glossary/glossary.md#fourgl_engine) imports the Currency field from the Business Partner to the Currency field of the Currency table.

## 2. Table reference exists from main table of child session to main table of parent session

## Situation
A browse list session with main table Y is started from a parent session with main table X. A field in table Y refers to table X. (In most cases, there is an identifying relationship between table X and table Y, e.g. order header (table X) and order lines (table Y).)

## Result
The [4GL engine](../glossary/glossary.md#fourgl_engine) imports the primary key fields from table X and stores them in the primary key fields of table Y.

## Example
Primary key of table X is order number. Primary key of table Y is order number, position number.
The 4GL engine imports the order number from table Orders to the corresponding field of table Order Lines. The position number field remains empty.

## Consequences for programming in UI script
None
Note  Automatic import is not possible if two or more main table fields of the child session have a reference to the main table of the parent session. In this case the bshell will import one of the fields. From application development point of view, it is unpredictable which field.

## 3. Same main table for parent session and child session

## Situation
A browse list session with main table X is started from a parent session with with the same main table.

## Result
The [4GL engine](../glossary/glossary.md#fourgl_engine) imports the primary key values from the parent session of table X and stores them in the primary key fields of table X in the browse list session.

## Example
The user browses from the Business Partner Details session to the Business Partners browse list session to select a Parent Business Partner.

## Consequences for programming in UI script
Often a hierarchical structure exists in the same table. In those cases you want to override the automatic import by the 4GL engine, since not the primary key values should be imported, but the value of the browse field (e.g. the Business Partner Parent field) and that value should be stored in the primary key fields of the maintable of the browse list session. You should also take care of saving and restoring the primary key values, otherwise the record pointer of the parent session is set incorrectly.
```

declaration:

        table   ttcom100 |* Business Partners

        domain  tccom.bpid      hold.bpid

field.tccom100.prbp: |* Parent business partner
before.zoom:
        |* Save the primary key field
        hold.bpid = tccom100.bpid
        tccom100.bpid = tccom100.prbp
after.zoom:
        |* Restore the primary key field
        tccom100.bpid = hold.bpid
```

## 4. Parent session without main table

## Situation
A browse list session with main table X is started from a parent session without a main table (e.g. a print session).

## Result
The [4GL engine](../glossary/glossary.md#fourgl_engine) imports the primary key values of table X (if available) from the parent process and stores them in the primary key fields of the browse list sessions' main table.

## Example
Browse list session Business Partners is started from the parent session Print Business Partners. The main table of the browse list session is tccom100. The 4GL engine tries to import tccom100.bpid from the print session and stores it in the tccom100.bpid field of the main table of the browse list session.

## Consequences for programming in UI script
In many cases you will have to re-program the parent session in such a way that the primary key fields of the main table of the browse list session are filled.
```

declaration:

        table   ttcom100 |* Business Partners

field.bpid.f:
before.zoom:
        tccom100.bpid = bpid.f
```

## 5. No relationship between tables

## Situation
A browse list session with main table Y starts from a parent session with main table X. There is no relationship between table X and table Y (e.g. in case of an integration between packages).

## Result
The [4GL engine](../glossary/glossary.md#fourgl_engine) imports the primary key values of table Y from the parent session and stores them in the primary key fields of table Y of the browse list session.

## Consequences for programming in UI script
In many cases you will have to re-program the parent session in such a way that the primary key fields of the main table of the browse list session are filled.

## Example: browsing to Freight Service Levels from Warehousing Orders
```

declaration:

        table   tfmfmd070

field.whinh200.serv:
before.zoom:
        fmfmd070.serv = whinh200.serv
```
Note  For purposes of clarity the example does not use integration DLLs, nor does it use start.session() to start the browse list.

## Overriding Automatic Import
Automatic import only works when the browse list starts with the primary key. With dynamic index switching it is also possible to start the browse list with other keys. In that case automatic import can give wrong results.
Because of this and other reasons the application wants to override automatic import. The application might implement browsing as mentioned above at point 5. However the application can also choose to use zoom.* variables in these cases. (The name of these variables does not matter, however it is common practice to name them zoom.*).

## Example
Parent session UI script
```

declaration:

extern  domain  tccom.bpid      zoom.bpid

field.whinh200.stco: |* Ship to BP
before.zoom:
        zoom.bpid = whinh200.stco
```
Browse list session UI script
```

declaration:

        table   ttccom111

zoom.from.all:
on.entry:
        import("zoom.bpid", tccom111.stbp)
```

## Example: browsing to session with other than primary key
E.g. browsing to Business Partners by Parent Business Partner.
Parent session UI script
```

declaration:

extern  domain  tccom.bpid      zoom.bpid |* BP id
extern  domain  tccom.bpid      zoom.prbp |* Parent BP

field.ppmmm999.bpid:
before.zoom:
        attr.zoomindex = 2 |* Start with index 2
        zoom.prbp = ppmmm999.prbp
        zoom.bpid = ppmmm999.bpid
```
Browse list session UI script
```

declaration:

        table   ttccom100

zoom.from.all:
on.entry:
        on case curr.key
        case 1:
                |* Automatic import
                break
        case 2:
                import("zoom.prbp", tccom100.prbp)
                import("zoom.bpid", tccom100.bpid)
                break
        endcase
```
Note  Note that the start option of the browse list session can cause this not to work (e.g. when this is set to get.defaults). It is recommended to use the default start option instead.

## Related topics
- [Definition](browsing_definition.md)

- [Overview of browsing](browsing_overview.md)

- [Exporting variables](browsing_exporting.md)

- [Starting a browse list session](browsing_starting.md)
