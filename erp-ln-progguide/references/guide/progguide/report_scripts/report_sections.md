# Report sections (report scripts)
A report consists of a number of layouts, which define the content and organization of the various parts of a report (for example, the header, footer, and body of the report). There are a number of possible layout types, as follows:
- *before.report* – printed once at beginning of the report (a title page, for example)
- *after.report* – printed once at the end of the report
- *header* – printed at the top of each page
- *footer* – printed at the bottom of each page
- *before.field* – printed before each group of records in reports of type 3; if a group of records spans more than one page, the before.field layout is repeated at the top of the new page
- *after.field* – printed immediately after each group of records in reports of type 3
- *detail* – used for the individual records included in the body of the report   The content and arrangement of these layouts are defined in the data dictionary.
In the report sections in a report script, you can program actions to be performed before and/or after execution of individual layouts of these types. Report sections consist of a main section and a subsection. You use a main section to specify the particular layout for which the programmed actions are to be executed. You must follow a main section with either a *before.layout* or an *after.layout* subsection. These latter specify whether the actions are to be executed before or after the particular layout is printed.

## Main sections

## before.report.<layout_number>:
Actions programmed in this section are executed for a specified layout of type before.report.

## after.report.<layout_number>:
Actions programmed in this section are executed for a specified layout of type after.report.

## header.<layout_number>:
Actions programmed in this section are executed for a specified layout of type header.

## detail.<layout_number>:
Actions programmed in this section are executed for a specified layout of type detail.

## before.<field name>.<layout_number>:
Actions programmed in this section are executed for a specified layout of type before.field.

## after.<field name>.<layout_number>:
Actions programmed in this section are executed for a specified layout of type after.field.

## footer.<layout_number>:
Actions programmed in this section are executed for a specified layout of type footer.

## Subsections

## before.layout:
Actions programmed in this subsection are executed before the specified layout is printed.
When *lattr.print* is set to false, the layout is not printed and the *before.layout* and *after.layout* sections are not executed. If you set *lattr.print* to falsein the *before.layout* section itself, the layout is not printed and the *after.layout* section is not executed.

## after.layout:
Actions programmed in this subsection are executed after the specified layout is printed.

## Related topics
- [Report scripts overview](overview.md)
- [Report script sections](sections.md)
- [Predefined variables](predefined_variables.md)
- [Report script functions](functions_in_report_scripts.md)
- [Expanding text variables](expanding_text_variables.md)
