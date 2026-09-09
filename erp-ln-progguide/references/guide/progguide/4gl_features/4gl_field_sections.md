# 4GL field sections
You use field sections to program actions that you want to be executed for a variety of field events. Field sections consist of a main section and a subsection. The main section specifies the field(s) for which the actions must be executed. The subsections specify when the actions must be executed.

## Main sections

## field.field name:
The subsections associated with this main section are executed for the specified field. The field name you specify must correspond with the name on the form.

## field.all:
The subsections associated with this main section are executed for all fields on the form

## field.other:
A subsection associated with this section is executed for all fields for which the particular subsection has not been programmed in a *field.**<**field name**>* section.

## Subsections

## init.field:
The actions programmed in this subsection are executed the first time that the form on which the field occurs becomes current. The subsection is executed immediately before the *init.form* section of the form. You can use this section to change field attributes.

## before.field:
The actions programmed in this subsection are executed each time the focus moves to the specified field. The subsection is executed immediately before the *before.input* or *before.display* subsections.

## before.input:
This section is supported for backward compatibility only. The actions programmed in this subsection are executed immediately before input to an input field commences. In Infor Enterprise Server programs, use [enable.fields()](../functions_form_and_form_field_operations/enable.fields.md) and [disable.fields()](../functions_form_and_form_field_operations/disable.fields.md) in the when.field.changes of another field to enable and disable fields.

## before.display:
The actions programmed in this subsection are executed each time that the specified field is displayed. You can use this subsection, for example, to set the value of a display field or to change the output format of currencies and dates (by using *attr.oformat$*).

## selection.filter:
In this section you can set the query extensions for filtering the selection. (See [query.extend.where()](../functions_sql_query_extensions/query.extend.where.md)). This section is triggerd when a zoom process is started or when autocomplete is started on the specified field. If this section was triggered by the start of a zoom process, the before.zoom section is called hereafter immediately.

## before.zoom:
When a zoom process is started on the specified field, the actions programmed in this subsection are executed immediately before the zoom process is executed. You can use this subsection to change the zoom attributes. For example, in the field definition in the form manager, a default zoom code can be specified. You can then use this subsection to change the zoom code (by setting the predefined variable *attr.zoomcode*). In order to cancel the zoom, use the [input.again()](../functions_form_and_form_field_operations/input.again.md) function.

## before.checks:
For non-enum fields the actions programmed in this subsection are executed when the field looses focus. I.e.: the TAB key has been pressed or the user clicked on another field. The subsection is executed immediately before the domain and references are checked. You can use this section, for example, to change the value of the field before the domain and reference checks.
For enum fields (type DB.ENUM or DB.BITSET) the actions programmed in this subsection are executed in two cases:

- when the user changes the value of the field; in this case the subsection is executed just before the *when.field.changes* subsection

- when the field looses focus, but only in case the field's value was not changed

## domain.error:
The actions programmed in this subsection are executed if the domain check causes an error after data has been entered in the field. You can use this section to provide your own error message instead of the standard message.

## ref.input:
The actions programmed in this subsection are executed if a reference error occurs. If you program this section, the [4GL engine](../glossary/glossary.md#fourgl_engine) does not display a message.

## ref.display:
The actions programmed in this subsection are executed if there is an error in the reference display.

## check.input:
This section is replaced by [Data Access Layer](../functions_dal/overview.md) functionality (if a DAL exists for the table).
The actions programmed in this subsection are executed immediately after the domain and reference checks. You can use this section to test for errors that are not detected automatically. If the [4GL engine](../glossary/glossary.md#fourgl_engine) detects an error, the focus remains on the field. In a script, you can use [set.input.error()](../functions_message_handling/set.input.error.md) to display an error message and start input again.

## on.input:
This section is supported for backward compatibility. Functionality has been replaced by Form Commands.
The actions programmed in this subsection are executed immediately after the *check.input* subsection. You can use this section, for example, to perform some appropriate action when the user enters a special character or to display a warning message in certain cases.

## when.field.changes:
The actions programmed in this subsection are executed when the new value entered in the specified field differs from the old value.

## after.zoom:
The actions programmed in this subsection are executed when the zoom process on a specified field ends. You can use this subsection, for example, to redisplay any field that has changed as a result of the zoom process.

## after.input:
The actions programmed in this subsection are executed after all checks have been performed on input to the specified field and after the *when.field.changes* subsection has been executed. In this subsection, you can use the *to.field()* function if the sequence deviates from the default.

## after.display:
The actions programmed in this subsection are executed just after display of the specified field. You can use this subsection, for example, to read reference tables.

## after.field:
This is the last subsection for a field. The actions programmed in this subsection are executed after input to or display of the specified field. This section is always executed, even if the user left the field by pressing ESC, one of the arrow keys, or a mouse button. You can use this subsection to perform special actions before leaving the field.

## Example
```

field.ttgfd500.cmnd:
before.zoom:
    ttadv470.type = ttadv.type.standard.commands

field.ttgfd500.wint:
when.field.changes:
    on case ttgfd500.wint
    case ttgfd.wint.overview:
        set.enum.values.for.field(.......)
        break
    .....
    endcase

field.ttadv470.optc:
before.display:
    on case ttgfd500.optn
    case CMD.CASCADE:
        ttadv470.optc = "CASCADE"
        break
    case CMD.SEPARATOR:
        ttadv470.optc = "--------"
        break
    endcase
    for i = 2 to ttgfd500.levl
        ttadv470.optc = "   " & ttadv470.optc
    endfor
```

## Related topics
- [Programming a UI Script overview](overview.md)

- [4GL event sections](4gl_event_sections.md)

- [Flow of 4GL engine](flow_of_standard_program.md)
