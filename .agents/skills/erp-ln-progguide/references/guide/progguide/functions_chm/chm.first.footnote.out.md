# chm.first.footnote.out()

## Syntax:
`function long chm.first.footnote.out( ref long footnote_no, ref string footnote_text() )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This returns information about the first footnote in the current chart. Use [chm.next.footnote.out()](chm.next.footnote.out.md) to retrieve information about subsequent footnotes in the chart.

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
