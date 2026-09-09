# Report script functions
The statements programmed in a report script section consist of a combination of [3GL programming language features: overview](../3gl_features/overview.md) and the following 4GL report functions:
| | |
|---|---|
| layout.again() | Evaluate and print layout again. |
| need( expr ) | Force a page break if the number of free lines is less than *expr*. |
| page() | Start a new page. |
| reset.suppress() | It is possible to suppress printing a value when it is the same as the previous value. You can use this function to suppress the value once (that is, for one value). |
| skip( expr ) | Skip *expr* number of lines before printing the next layout. |
| skip.to( expr ) | Skip to the line number indicated by *expr*. Intervening lines are left blank. If the specified line number is less than the current page number, a new page is started. |
| to.page( expr ) | Start a new page with number *expr*. |
You cannot use *need()*, *page()*, *skip()*, *skip.to()*, or *to.page()* in header and footer layouts.

## Related topics
- [Report scripts overview](overview.md)

- [Report script sections](sections.md)

- [Predefined variables](predefined_variables.md)

- [Expanding text variables](expanding_text_variables.md)
