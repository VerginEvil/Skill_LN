# progressbar.set.clickable()

## Syntax:
`function long progressbar.set.clickable( boolean i.is.clickable )`

## Description
Sets the Progress bar to be clickable or not clickable.
On a click event a function progressbar.'fieldname'.clicked in the 4gle script will be called.
| | |
|---|---|
| True | Progress bar is clickable, a click will result in a visible action by the script |
| False | Progress bar is not clickable, no action. |

## Arguments
| | | |
|---|---|---|
| `boolean` | `i.is.clickable` |  True: Progress bar is clickable, a click will result in a visible action by the script. False: Progress bar is not clickable, no action.  |

## Return values
| | |
|---|---|
| 0 | Success, the clickable state of the Progress bar has been updated. |
| -1 | Failure, current field is not of type Progress bar. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2610.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "before.display" section for the field that is set as a Progress bar by calling the function progressbar.set.field.

## Related topics
- [Progress bar overview and synopsis](overview_and_synopsis.md)
