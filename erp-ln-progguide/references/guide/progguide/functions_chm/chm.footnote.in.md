# chm.footnote.in()

## Syntax:
`function long chm.footnote.in( long footnoote_no, string footnote_text(80) )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This function defines a footnote that can be used to annotate a data point or projection point.

## Arguments
| | | |
|---|---|---|
| `long` | `footnoote_no` |  The footnote number.  |
| `string` | `footnote_text(80)` |  The footnote text.  |

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
