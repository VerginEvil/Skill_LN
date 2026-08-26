# 4GL form sections
Note  Only the form.all section is relevant to dynamic forms. For dynamic forms, use the [4GL group sections](4gl_group_sections.md) instead.
You use form sections to program actions that you want to be executed when forms are activated or ended. Form sections consist of a main section and a subsection. The main section specifies the particular form(s) for which the actions are to be executed. The subsections specify when the actions must be executed – for example, when the user navigates to a form (before.form), or navigates away from a form (after.form).

## Main sections
*form.<form number>:*
The subsections associated with this section are executed for the specified form. The <form number> is only available for static forms and is the sequence number of the form, as defined in the session *Forms* when started from the session *Sessions* (ttadv2500m000).

## form.all:
The subsections associated with this section are executed for all forms of the session.

## form.other:
A subsection associated with this section is executed for all forms for which the particular subsection has not been programmed in a *form.<form number* section.

## Subsections

## init.form:
The actions programmed in this subsection are executed the first time the specified form becomes current, immediately before the subsection *before.form*. You use this subsection to program the first action to be performed by the system – a *first.set* or *first.view*, for example.

## before.form:
The actions programmed in this subsection are executed each time the user navigates to the form.

## after.form:
The actions programmed in this subsection are executed each time the user navigates away from the form.

## Example:
```

form.1:
init.form:
    execute(first.set)
form.other:
init.form:
    | ONLY FOR STATIC FORMS!
    display("disp3")
form.all:
before.form:
    display("disp")
```

## Related topics
- [Programming a UI Script overview](overview.md)
- [4GL event sections](4gl_event_sections.md)
- [Flow of 4GL engine](flow_of_standard_program.md)
