# rprt_close()

## Syntax:
`function void rprt_close( [ long mess_flag ] )`

## Description
This is a short version of [brp.close()](brp.close.md). It closes the report writer for the current report. You can use the function in a 4GL script in the subsection *on.choice* of the section *choice.print.data*. In this section, the predefined variable *spool.report* is available. This variable stores the name of the current report.

## Arguments
| | | |
|---|---|---|
| `[ long` | `mess_flag ]` |  This optional argument can have one of the following values (default is 0): 0 If no data is printed, the following message appears: “No data present within selection” 1 If no data is printed, the following message appears: “No data found for report, no report is printed” 2 If no data is printed, no message appears.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
See [rprt_open()](rprt_open.md).

## Related topics
- [Reports overview and synopsis](overview_and_synopsis.md)
- [Spooling overview and synopsis](../functions_spooling/overview_and_synopsis.md)
