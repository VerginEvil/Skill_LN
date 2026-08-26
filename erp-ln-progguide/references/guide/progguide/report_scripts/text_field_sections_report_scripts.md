# Text field sections (report scripts)
You use a text field section to apply certain actions to all instances of a particular text field that are included in the report. A text field section consists of a main section and a subsection. The main section specifies the particular text field to which the actions must be applied. The subsection specifies that the actions are to be performed before the text field is printed.
For example, you could include the [Report script functions](functions_in_report_scripts.md), [Report script functions](functions_in_report_scripts.md), and [Report script functions](functions_in_report_scripts.md) functions in a text field section to enforce a page break or to skip a specified number of lines before the text field is printed. Or you could set *lattr.print* in the section in order to skip one text line before printing the text field.

## Main field

## field.<text_field>:
Actions programmed in this section are executed for all instances of the specified text field that are included in the report. The text field must have been defined as a report input field in the data dictionary.

## Subsection

## before.print:
Actions programmed in this section are executed before the specified text field is printed.

## Related topics
- [Report scripts overview](overview.md)
- [Report script sections](sections.md)
- [Predefined variables](predefined_variables.md)
- [Report script functions](functions_in_report_scripts.md)
- [Expanding text variables](expanding_text_variables.md)
