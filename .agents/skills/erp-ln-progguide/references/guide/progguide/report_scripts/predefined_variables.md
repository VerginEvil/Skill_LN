# Predefined variables
You can use the following predefined variables in a report script.
R = read-only R/W = read and write
| | | |
|---|---|---|
| lattr.autobefores | R/W | A boolean indicating whether or not before.field layouts are automatically repeated at the top of a page if the page break does not correspond with a sort break. The default value is true. |
| lattr.autoreset | R/W | A boolean indicating whether or not [Report script functions](functions_in_report_scripts.md) is automatically performed in the case of breaks of layouts in sorting fields. The default value is true. |
| lattr.break | R | A boolean that is set to true during printing of before.field layouts when the layout is printed as the result of a sort field change. It is set to false when a before.field layout is printed because of a page break. |
| lattr.enddata | R | A boolean indicating whether or not the end of the data has been reached. |
| lattr.header | R | A boolean that is set to true during printing of header layouts and during printing of before.field layouts at the top of a page. |
| lattr.language$ | R | The language code of the report. |
| lattr.lineno | R | The current line number. |
| lattr.multicol | R/W | Indicates whether or not multiple columns are used when more than one layout fits on a line. Possible values are: MULTICOL_NONE Normal output; no columns are used. MULTICOL_ORDER_HORIZONTAL Output is arranged in multiple columns, ordered horizontally. For example: rec_1 rec_2 rec_3 rec_4 rec_5 rec_6 MULTICOL_ORDER_VERTICAL Output is arranged in multiple columns, ordered vertically (per page). For example: rec_1 rec_3 rec_5 rec_2 rec_4 rec_6 |
| lattr.multicol.count | R/W | Specifies the number of columns to use when multiple columns are specified (see *lattr.multicol*). The default value is 0. In this case, the report manager calculates the number of columns based of the report width and the layout width. |
| lattr.multicol.repeat | R/W | A boolean indicating whether headers and footers are automatically repeated for each column. The default value is true. The width of the header and footer layouts width must be equal to or less than the width of the detail layout. |
| lattr.pageno | R/W | Current page number. |
| lattr.print | R/W | Indicates whether or not a layout is to be printed. |
| lattr.prline | R/W | After expansion of a variable in a report, this is filled with the text line that is printed. |
| lattr.recordtimes | R/W | Indicates the number of times the layout will be printed. |
| lattr.textexpand | R/W | A boolean indicating whether or not variables included in text fields can be expanded. The default is false. |
| lattr.textlang$ | R/W | The language code for printing text. The default is the language code of the report. |
| lattr.textline | R | A string containing the source text line from the text manager. |
| lattr.textlineno | R | The number of the line that must be printed. |
| lattr.textlines.max | R/W | The maximum number of lines in the layout. |
| lattr.textlines.min | R/W | The minimum number of lines in the layout. |

## Related topics
- [Report scripts overview](overview.md)

- [Report script sections](sections.md)

- [Predefined variables](predefined_variables.md)

- [Report script functions](functions_in_report_scripts.md)

- [Expanding text variables](expanding_text_variables.md)
