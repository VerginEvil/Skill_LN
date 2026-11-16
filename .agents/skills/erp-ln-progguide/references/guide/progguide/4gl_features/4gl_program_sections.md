# program sections
Program sections have no subsections.
Note  The on.display.total.line section is available as of [porting set TIV](../tiv/tiv_overview.md) [level 1075](../tiv/tiv_1075.md).
The following program sections are available:

## Main sections

## declaration:
Use this section to declare tables and global variables that you want to use in other sections in the script. See [Declarations](../3gl_features/declarations.md) and [Tables](../3gl_features/tables.md) for details of the declaration syntax. You also use this section to define macros and function prototypes. You can put your #idents for solution identification here as well.

## before.program:
Use this section to program actions that must be executed when the session starts. For example, you can use this section to initialize or import variables or to read a special record.

## after.form.read:
Use this section to change form data at run time after it has been read in memory. Typical functionality is the removal of fields, groups or commands

## on.error:
Use this section to program actions that must be executed at the end of the session, before the *after.program* section. If the session is canceled, the actions in this section are not executed. If an error is detected, you can check the predefined variable *e* for the error code.

## after.program:
Use this section to program actions that must be executed at the end of the session, after the *on.error* section.

## after.update.db.commit:
Use this section to program actions that must be executed immediately after a [commit.transaction()](../functions_db_operations/commit.transaction.md) call, if the database is updated.

## before.display.object:
Use this section to program actions that must be executed each time the entire record is displayed.

## before.new.object:
Use this section to program actions that must be executed once before the input of the first field of the new created record. It is used for setting the default values of the record fields.

## on.display.total.line:
Use this section to calculate and display the total line fields. The function [display.total.fields()](../functions_form_and_form_field_operations/display.total.fields.md) must be called from this section to display the actual total fields values. This section will be called when the variable *fattr.total.line* is set in the before.program section. By default the 4GL-Engine will call this section after a (new) set of records is read from the database. In addition an application can trigger this section to be called by calling the function: [refresh.total.line()](../functions_form_and_form_field_operations/refresh.total.line.md).

## functions:
Use this section to define the functions used in the other sections. This must be the last section in the script. The function syntax is the same as for [3GL programming language features: overview](../3gl_features/overview.md).

## Example
```

declaration:
        table       tpctst999
        long        var01, ret

before.program:
        if read_parameter() then
                mess("pctsts0001", 1) | Parameter not present
                stop()
        endif

on.error:
        mess("........", 1)

functions:
        function long read_parameter()
        {
            select pctst999.*
            from pctst999
            order by pctst999._index1
            as set with 1 rows
            selectdo
                    return(0)
            selectempty
                    return(1)
            endselect
        }
```

## Related topics
- [Programming a UI Script overview](overview.md)

- [4GL event sections](4gl_event_sections.md)

- [Flow of 4GL engine](flow_of_standard_program.md)
