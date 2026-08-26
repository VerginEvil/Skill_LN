# chm.next.footnote.out()

## Syntax:
`function long chm.next.footnote.out( ref long footnote_no, ref string footnote_text() )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
Use [chm.first.footnote.out()](chm.first.footnote.out.md) to retrieve information information about the first footnote in the current chart. Use *chm.next.footnote.out()* to retrieve information about the next footnote in the current chart. To retrieve information about all subsequent footnotes in the chart, you can place this function in a loop that executes as long as the return value is CHM_OK.
If the client application modifies the information and saves it to the source table or file, the new information is included the next time the chart is started.

## Arguments
| | | |
|---|---|---|
| `ref long` | `footnote_no` |  This returns the footnote number.  |
| `ref string` | `footnote_text()` |  This returns the footnote text.  |

## Return values
| | |
|---|---|
| CHM_OK | Success. |
| CHM_ERROR | Error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Chart manager overview](overview.md)
- [Chart manager synopsis](synopsis.md)
- [Creating a chart manager client application](creating_a_chart_manager_client_application.md)
- [Chart manager example](example.md)
