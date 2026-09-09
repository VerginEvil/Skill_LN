# Program sections (report scripts)
You use program sections to define functions, and to declare tables and global variables, that you want to use in the other sections in the script. You also use program sections to program actions that you want executed at the start and end of the report and after the report writer receives a record.
The following program sections are available. They are all main sections. There are no subsections associated with program sections.

## declaration:
Use this section to declare tables and global variables that you want to use in other sections in the report script. See [Declarations](../3gl_features/declarations.md) and [Tables](../3gl_features/tables.md) for details of the declaration syntax. Note that there is no need to declare a table if a field of that table is defined in the report writer as an input field. The report writer declares such tables automatically.

## before.program:
Use this section to program actions that must be executed when the report is started. For example, you can use this section to initialize or import variables.

## after.program:
Use this section to program actions that must be executed at the end of the report. For example, you can use this section to close files that were opened during execution of the report.

## after.receive.data:
Use this section to program actions that must be executed whenever the report writer receives a record. For example, you can use this section to read or modify a variable.

## functions:
Use this section to define functions that you want to use in other sections in the report script. The syntax of functions used in a report script is the same as for [Functions](../3gl_features/functions.md).
When included, this section must be the last section in the report script.

## Related topics
- [Report scripts overview](overview.md)

- [Report script sections](sections.md)

- [Predefined variables](predefined_variables.md)

- [Report script functions](functions_in_report_scripts.md)

- [Expanding text variables](expanding_text_variables.md)
