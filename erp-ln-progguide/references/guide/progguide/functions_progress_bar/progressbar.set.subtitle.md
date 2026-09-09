# progressbar.set.subtitle()

## Syntax:
`function long progressbar.set.subtitle( const string i.title )`

## Description
This function updates the Progress bar's subtitle to match the subtitle argument.

## Arguments
| | | |
|---|---|---|
| `const string` | `i.title` |  Subtitle of the Progress bar displayed left aligned below the Progress bar. Only applicable for a stand-alone Progress bar field. If the Progress bar field is part of the grid or in the details area behind another field then the title will be ignored.  |

## Return values
| | |
|---|---|
| 0 | Success, the subtitle of the Progress bar has been updated. |
| -1 | Failure, current field is not of type Progress bar. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2610.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "before.display" section for the field that is set as a Progress bar by calling the function progressbar.set.field.

## Related topics
- [Progress bar overview and synopsis](overview_and_synopsis.md)
