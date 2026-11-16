# 4GL event sections
A 4GL script can contain one or more of the following types of sections:

- [program sections](4gl_program_sections.md)

- [4GL zoom.from sections](4gl_zoomfrom_sections.md)

- [4GL form sections](4gl_form_sections.md)

- [4GL group sections](4gl_group_sections.md)

- [4GL choice sections](4gl_choice_sections.md)

- [4GL field sections](4gl_field_sections.md)

- [4GL main table i/o sections](4gl_main_table_io_sections.md)

With the exception of program sections, each section consists of a main section and one or more subsections. A main section indicates the object for which the programmed actions must be executed. A subsection specifies when the actions must be executed. Program sections consist of a main section only.
If you do not include a main section immediately before a subsection, the subsection is assigned to the previous main section in the script. For example:
```

choice.print.data:      | main section
before.choice:          | subsection of print.data
    ...
    ...
after.choice:           | subsection of print.data
    ...
    ...
```
The following rules apply to the ordering of sections within a script:

- The *declaration* section (a program sections) must be the first section in the script.

- The *functions* section (also a program section) must be the last section in the script.

- Other sections can occur in any order, but the preferred order is: program sections, zoom.from sections, form sections, group sections, choice sections, field sections, main table sections.

- Do not mix sections of different types. For example, do not define a choice section, followed by a field section, and then a choice section again.

Variables declared in the *declaration* section are global variables that you can use in all sections. Variables declared within any other section are local variables that you can use in that section only.

## Related topics
- [Programming a UI Script overview](overview.md)

- [Flow of 4GL engine](flow_of_standard_program.md)
